import base64
import os
from io import BytesIO


class RC5(object):
    def __init__(self, key):
        self.mode = 'CBC'  
        self.blocksize = 32
        self.rounds = 12
        self.iv = os.urandom(self.blocksize // 8)
        self._key = key.encode('utf-8')

    @staticmethod
    def _shift_l(val, r_bits, max_bits):
        v1 = (val << r_bits % max_bits) & (2 ** max_bits - 1)
        v2 = ((val & (2 ** max_bits - 1)) >> (max_bits - (r_bits % max_bits)))
        return v1 | v2

    @staticmethod
    def _shift_r(val, r_bits, max_bits):
        v1 = ((val & (2 ** max_bits - 1)) >> r_bits % max_bits)
        v2 = (val << (max_bits - (r_bits % max_bits)) & (2 ** max_bits - 1))

        return v1 | v2

    @staticmethod
    def _expand_key(key, wordsize, rounds):
        def _align_key(key, align_val):
            while len(key) % (align_val):
                key += b'\x00'
            L = []
            for i in range(0, len(key), align_val):
                L.append(int.from_bytes(key[i:i + align_val], byteorder='little'))
            return L
        def _const(w):
            if w == 16:
                return (0xB7E1, 0x9E37)
            elif w == 32:
                return (0xB7E15163, 0x9E3779B9)
            elif w == 64:
                return (0xB7E151628AED2A6B, 0x9E3779B97F4A7C15)

        def _extend_key(w, r):
            P, Q = _const(w)
            S = [P]
            t = 2 * (r + 1)
            for i in range(1, t):
                S.append((S[i - 1] + Q) % 2 ** w)
            return S

        def _mix(L, S, r, w, c):
            t = 2 * (r + 1)
            m = max(c, t)
            A = B = i = j = 0
            for k in range(3 * m):
                A = S[i] = RC5._shift_l(S[i] + A + B, 3, w)
                B = L[j] = RC5._shift_l(L[j] + A + B, A + B, w)
                i = (i + 1) % t
                j = (j + 1) % c
            return S
        aligned = _align_key(key, wordsize // 8)
        extended = _extend_key(wordsize, rounds)
        S = _mix(aligned, extended, rounds, wordsize, len(aligned))
        return S

    @staticmethod
    def _encrypt_block(data, expanded_key, blocksize, rounds):
        w = blocksize // 2
        b = blocksize // 8
        mod = 2 ** w
        A = int.from_bytes(data[:b // 2], byteorder='little')
        B = int.from_bytes(data[b // 2:], byteorder='little')
        A = (A + expanded_key[0]) % mod
        B = (B + expanded_key[1]) % mod
        for i in range(1, rounds + 1):
            A = (RC5._shift_l((A ^ B), B, w) + expanded_key[2 * i]) % mod
            B = (RC5._shift_l((A ^ B), A, w) + expanded_key[2 * i + 1]) % mod
        res = A.to_bytes(b // 2, byteorder='little') + B.to_bytes(b // 2, byteorder='little')
        return res
    @staticmethod
    def _decrypt_block(data, expanded_key, blocksize, rounds):
        w = blocksize // 2
        b = blocksize // 8
        mod = 2 ** w
        A = int.from_bytes(data[:b // 2], byteorder='little')
        B = int.from_bytes(data[b // 2:], byteorder='little')
        for i in range(rounds, 0, -1):
            B = RC5._shift_r(B - expanded_key[2 * i + 1], A, w) ^ A
            A = RC5._shift_r((A - expanded_key[2 * i]), B, w) ^ B
        B = (B - expanded_key[1]) % mod
        A = (A - expanded_key[0]) % mod
        res = A.to_bytes(b // 2, byteorder='little') + B.to_bytes(b // 2, byteorder='little')
        return res

    def encrypt_file(self, infile, outfile):
        w = self.blocksize // 2
        b = self.blocksize // 8
        if self.mode == 'CBC':
            last_v = self.iv
            outfile.write(last_v)
        expanded_key = RC5._expand_key(self._key, w, self.rounds)
        chunk = infile.read(b)
        while chunk:
            chunk = chunk.ljust(b, b'\x00')
            if self.mode == 'CBC':
                chunk = bytes([a ^ b for a, b in zip(last_v, chunk)])
            encrypted_chunk = RC5._encrypt_block(chunk, expanded_key,
                                                 self.blocksize,
                                                 self.rounds)
            outfile.write(encrypted_chunk)
            last_v = encrypted_chunk
            chunk = infile.read(b)

    def decrypt_file(self, infile, outfile):
        w = self.blocksize // 2
        b = self.blocksize // 8
        if self.mode == 'CBC':
            last_v = outfile.read(b)
        expanded_key = RC5._expand_key(self._key, w,
                                       self.rounds)
        chunk = infile.read(b)
        while chunk:
            decrypted_chunk = RC5._decrypt_block(chunk, expanded_key,
                                                 self.blocksize,
                                                 self.rounds)
            if self.mode == 'CBC':
                decrypted_chunk = bytes([a ^ b
                                         for a, b in zip(last_v,
                                                         decrypted_chunk)])
                last_v = chunk
            chunk = infile.read(b)
            if not chunk:
                decrypted_chunk = decrypted_chunk.rstrip(b'\x00')
            outfile.write(decrypted_chunk)

    def encrypt_str(self, input_str):
        str_in = BytesIO()
        str_in.write(input_str.encode('utf-8'))
        str_in.seek(0)
        str_out = BytesIO()
        self.encrypt_file(str_in, str_out)
        return base64.urlsafe_b64encode(str_out.getvalue()).decode("utf-8")

    def decrypt_str(self, input_enc_str):
        enc_bytes = base64.urlsafe_b64decode(input_enc_str)
        byte_in = BytesIO()
        byte_in.write(enc_bytes)
        byte_in.seek(0)
        byte_out = BytesIO()
        self.decrypt_file(byte_in, byte_out)
        return byte_out.getvalue().decode('utf-8')

if __name__ == '__main__':
    test_origin_char = input("Introduce your text: ")
    key = input("Introduce the key: ")
    cryptor = RC5(key)
    cryptor.mode = "CBC"

    print('Plain text: ', test_origin_char.encode('utf-8'))
    enc_str = cryptor.encrypt_str(test_origin_char)

    print("encrypted_str", enc_str, len(enc_str))
    dec_str = cryptor.decrypt_str(enc_str)

    print("decrypted_str", dec_str)
    assert dec_str == test_origin_char
    cryptor = RC5(key)
    cryptor.mode = "ECB"

    print('Plaintext: ', test_origin_char.encode('utf-8'))
    enc_str = cryptor.encrypt_str(test_origin_char)

    print("encrypted_str", enc_str, len(enc_str))
    dec_str = cryptor.decrypt_str(enc_str)

    print("decrypted_str", dec_str)
    assert dec_str == test_origin_char