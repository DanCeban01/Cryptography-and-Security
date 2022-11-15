### Course: Cryptography and Security
### Dan Ceban FAF-202

----

## Hash functions and Digital Signatures. RSA with SHA256

----

## RSA

RSA algorithm is an asymmetric cryptography algorithm. Asymmetric actually means that it works on two different keys i.e. Public Key and Private Key. As the name describes that the Public Key is given to everyone and the Private key is kept private.

An example of asymmetric cryptography : 

- A client (for example browser) sends its public key to the server and requests some data.
- The server encrypts the data using the client’s public key and sends the encrypted data.
- The client receives this data and decrypts it.

Since this is asymmetric, nobody else except the browser can decrypt the data even if a third party has the public key of the browser. The idea of RSA is based on the fact that it is difficult to factorize a large integer. The public key consists of two numbers where one number is a multiplication of two large prime numbers. And private key is also derived from the same two prime numbers. So if somebody can factorize the large number, the private key is compromised. Therefore encryption strength totally lies on the key size and if we double or triple the key size, the strength of encryption increases exponentially. RSA keys can be typically 1024 or 2048 bits long, but experts believe that 1024-bit keys could be broken in the near future. But till now it seems to be an infeasible task.

How it works
The RSA algorithm ensures that the keys, in the above illustration, are as secure as possible. The following steps highlight how it works:

1. Generating the keys
- Select two large prime numbers x and y. The prime numbers need to be large so that they will be difficult for someone to figure out.
- Calculate n = x * y.
- Calculate the totient function:ϕ(n)=(x−1)(y−1).
- Select an integer e, such that e is co-prime to ϕ(n) and 1<e<ϕ(n).
The pair of numbers (n,e) makes up the public key.
- Calculate d such that e.d = 1 mod ϕ(n).

d can be found using the extended euclidean algorithm. The pair (n,d) makes up the private key.

2. Encryption
Given a plaintext P, represented as a number, the ciphertext C is calculated as:
C = P^{e}mod n.

3. Decryption
Using the private key (n,d), the plaintext can be found using:
P = C^{d} mod n.

## RSA PseudoCode
```python
int x = 61, int y = 53;
int n = x * y;
// n = 3233.

// compute the totient, phi
int phi = (x-1)*(y-1);
// phi = 3120.

int e = findCoprime(phi);
// find an 'e' which is > 1 and is a co-prime of phi.
// e = 17 satisfies the current values.

// Using the extended euclidean algorithm, find 'd' which satisfies 
// this equation:
d = (1 mod (phi))/e;
// d = 2753 for the example values.

public_key = (e=17, n=3233);
private_key = (d=2753, n=3233);

// Given the plaintext P=123, the ciphertext C is :
C = (123^17) % 3233 = 855;
// To decrypt the cypher text C:
P = (855^2753) % 3233 = 123;
```
----

## SHA256

Among the many advancements seen in network security, encryption and hashing have been the core principles of additional security modules. The secure hash algorithm with a digest size of 256 bits, or the SHA 256 algorithm, is one of the most widely used hash algorithms. While there are other variants, SHA 256 has been at the forefront of real-world applications. SHA 256 is a part of the SHA 2 family of algorithms, where SHA stands for Secure Hash Algorithm. Published in 2001, it was a joint effort between the NSA and NIST to introduce a successor to the SHA 1 family, which was slowly losing strength against brute force attacks. The significance of the 256 in the name stands for the final hash digest value, i.e. irrespective of the size of plaintext/cleartext, the hash value will always be 256 bits. The other algorithms in the SHA family are more or less similar to SHA 256. Now, look into knowing a little more about their guidelines.
In my laboratory work I used the popular hashlib and imported from it the sha256.

## SHA256 PseudoCode
```python
W = 32          #Number of bits in word
M = 1 << W
FF = M - 1      #0xFFFFFFFF (for performing addition mod 2**32)

#Constants from SHA256 definition
K = (0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
     0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
     0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
     0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
     0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
     0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
     0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
     0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
     0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
     0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
     0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
     0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
     0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
     0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
     0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
     0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2)

#Initial values for compression function
I = (0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
     0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19)

def RR(x, b):
    '''
    32-bit bitwise rotate right
    '''
    return ((x >> b) | (x << (W - b))) & FF

def Pad(W):
    '''
    Pads a message and converts to byte array
    '''
    mdi = len(W) % 64           
    L = (len(W) << 3).to_bytes(8, 'big')        #Binary of len(W) in bits
    npad = 55 - mdi if mdi < 56 else 119 - mdi  #Pad so 64 | len; add 1 block if needed
    return bytes(W, 'ascii') + b'\x80' + (b'\x00' * npad) + L   #64 | 1 + npad + 8 + len(W)

def Sha256CF(Wt, Kt, A, B, C, D, E, F, G, H):
    '''
    SHA256 Compression Function
    '''
    Ch = (E & F) ^ (~E & G)
    Ma = (A & B) ^ (A & C) ^ (B & C)        #Major
    S0 = RR(A, 2) ^ RR(A, 13) ^ RR(A, 22)   #Sigma_0
    S1 = RR(E, 6) ^ RR(E, 11) ^ RR(E, 25)   #Sigma_1
    T1 = H + S1 + Ch + Wt + Kt
    return (T1 + S0 + Ma) & FF, A, B, C, (D + T1) & FF, E, F, G

def Sha256(M):
    '''
    Performs SHA256 on an input string 
    M: The string to process
    return: A 32 byte array of the binary digest
    '''
    M = Pad(M)          #Pad message so that length is divisible by 64
    DG = list(I)        #Digest as 8 32-bit words (A-H)
    for j in range(0, len(M), 64):  #Iterate over message in chunks of 64
        S = M[j:j + 64]             #Current chunk
        W = [0] * 64
        W[0:16] = [int.from_bytes(S[i:i + 4], 'big') for i in range(0, 64, 4)]  
        for i in range(16, 64):
            s0 = RR(W[i - 15], 7) ^ RR(W[i - 15], 18) ^ (W[i - 15] >> 3)
            s1 = RR(W[i - 2], 17) ^ RR(W[i - 2], 19) ^ (W[i - 2] >> 10)
            W[i] = (W[i - 16] + s0 + W[i-7] + s1) & FF
        A, B, C, D, E, F, G, H = DG #State of the compression function
        for i in range(64):
            A, B, C, D, E, F, G, H = Sha256CF(W[i], K[i], A, B, C, D, E, F, G, H)
        DG = [(X + Y) & FF for X, Y in zip(DG, (A, B, C, D, E, F, G, H))]
    return b''.join(Di.to_bytes(4, 'big') for Di in DG)  #Convert to byte array

if __name__ == "__main__":
    bd = Sha256('Hello World')
    print(''.join('{:02x}'.format(i) for i in bd))

```

----

## Objectives
1. Get familiar with the hashing techniques/algorithms.
2. Use an appropriate hashing algorithms to store passwords in a local DB. You can use already implemented algortihms from libraries provided for your language. 
3. Use an asymmetric cipher to implement a digital signature process for a user message.
----

## Implementation

First of all we use Euclid's algorithm to determine the greatest common divisor:
```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```
After this in order to find the multiplicative inverse of two numbers we also use extended Euclid's algorithm (lines 11-33). Also an important part is to see if the given numbers are prime or not, so that is why we have this part of the code (lines 38-46):
```python
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True
```

Next step after setting up the initial data is to generate the keys. First of all we check if the numbers are prime or not, if not we get the message that we must choose two prime numbers, also there is no posibility for variables p and q to equal, and if there are equal, such an message will appear to inform. After checking and getting two valid values we start, variable n will be equal to the mutliplication of p and q:
``` python
    n = p * q
```
Next step is to calculate the totient of n which is equal to the formula:
```python
 phi = (p-1) * (q-1)
```
After calculating the value of phi we need generate a coprime variable e which value is coprime to phi. To find if this two variables are coprime we again use the Euclid's algorithm, and in the end we can generate the keys using Extended Euclid's Algorithm. The public keys will be variables e and n, while private will be d and n.

Now after we have public and private keys we can encrypt and decrypt our message. First of all we write the encryption function:
```python
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher
```
Secondly comes the decryption function:
```python 
def decrypt(pk, ciphertext):
    key, n = pk
    aux = [str(pow(char, key, n)) for char in ciphertext]
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)
```
In the lines 96-109 we have the function which is responsible to hashing message from the imported library and I am talking about this lines of code:
```python
def hashFunction(message):
    hashed = sha256(message.encode("UTF-8")).hexdigest()
    return hashed
```    
After hashing the next come verfication if the our hash is the same as the hash we get, and function responsible for it is:
```python
def verify(receivedHashed, message):
    ourHashed = hashFunction(message)
    if receivedHashed == ourHashed:
        print("Verification successful: ", )
        print(receivedHashed, " = ", ourHashed)
    else:
        
        print("Verification failed")
        print(receivedHashed, " != ", ourHashed)
```
And in the end(lines 96-120) we have the part of the code which is responsible for shwoing messages when compiling the code.

----
## Conclusion

This laboratory work was very interesting for me as a future software engineer because it give me the posibility to understand better on the practical stage, after getting the needed theoretical information at the course, about the modern and complex ways of cryptography and its security protocols. In this laboratory I implemented in my previous written assymetric cyphyer (RSA) the hashing, and to be more acurate the SHA256, in order to make the encryption/decryption process better for possbile future user. Also I extended my programming skills and cryptography knowledges to a new level which will be helpfull in my future projects. 

 So the why is SHA256 important? SHA-256 is used in some of the most popular authentication and encryption protocols, including SSL, TLS, IPsec, SSH, and PGP. In Unix and Linux, SHA-256 is used for secure password hashing. Cryptocurrencies such as Bitcoin use SHA-256 for verifying transactions. SHA-256 is one of the most secure hashing functions on the market. The US government requires its agencies to protect certain sensitive information using SHA-256.

 Sincerely to be my implementation is far away from the high level secured one, but it is very important for me in order to be sure how such protocols update the security of a programm and give less chances to a hacker to steal the data is transmitte through two users.