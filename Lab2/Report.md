Course: Cryptography & Security
Author: Dan Ceban FAF-202
Cryptography Algorithms

Rabbit Cypher (Stream Cypher)
   Rabbit uses a 128-bit key and a 64-bit initialization vector. The cipher was designed with high performance in software in mind, where fully optimized implementations achieve an encryption cost of up to 3.7 cpb on a Pentium 3, and of 9.7 cpb on an ARM7. However, the cipher also turns out to be very fast and compact in hardware. The core component of the cipher is a bitstream generator which encrypts 128 message bits per iteration. The cipher's strength rests on a strong mixing of its inner state between two consecutive iterations. The mixing function is entirely based on arithmetical operations that are available on a modern processor, i.e., no S-boxes or lookup tables are required to implement the cipher. The mixing function uses a g-function based on arithmetical squaring, and the ARX operations – logical XOR, bit-wise rotation with fixed rotation amounts, and addition modulo 232. The g-function used in Rabbit – squaring a 32-bit number to produce a 64-bit number, and then combining the left half and the right half of that square number with xor, to produce a 32-bit result – provides much better results than using the 32 middle bits of that squared number (the middle-square method).

   Rabbit claims 128-bit security against attackers whose target is one specific key. If, however, the attacker targets a large number of keys at once and does not really care which one he breaks, then the small IV size results in a reduced security level of 96 bit. This is due to generic TMD trade-off attacks.A small bias in the output of Rabbit exists, resulting in a distinguisher with 2247 complexity discovered by Jean-Philippe Aumasson in December 2006. Even though this distinguisher was improved to 2158 in 2008, it is not a threat to Rabbit's security because its complexity is significantly higher than the brute-force of the key space (2128).

   First set the 128 bit key. Then call the encrypt() function with the message to be encrypted in a vector of container of size 32 bit.

Example
key1 = [0000 0000 0000 0000 0000 0000 0000 0000]

plain_text = [0000 0000 0000 0000 ]

iv = [0000 0000]

cipher_text = [ED B7 05 67 37 5D CD 7C D8 95 54 F8 5E 27 A7 C6]

RC5 Cypher (Block Cypher)

RC5 is a block filter with a large number of parameters: block size, key size, and number of stages. It was invented by Ron Rivest and analyzed at RSA Laboratories [1324, 1325]. Three actions are used: XOR, addition and cyclic shifts. On most processors, cyclic shift operations are performed in constant time; variable cyclic shifts are a non-linear function. These cyclic shifts, which depend on both the key and the data, are an interesting operation. RC5 uses a variable length block. The encryption uses 2r+2 key-dependent 32-bit words - S0, S1, S2, ... S2r+1 - where r is the number of rounds. We will generate these words later. To encrypt, we first divide the plaintext block into two 32-bit words: A and B. (RC5 assumes the following convention for packing bytes into words: the first byte occupies the low bits of register A, etc.) 
Then:

A = A + S_0

B = B + S_1

For i = 1 to r:

A = ((A A B) <<< B) + S_(2i)

B = ((B A A) <<< A) + S_(2i+1)

The result is in registers A and B.

Decryption is also easy. Break the plaintext block into two words, A and B, and then:

For i = r down to 1:

B = ((B - S_(2i+1)) >>> A) A A

A = ((A - S_(2i)) >>> B) A B

B = B - S_1

A = A - S_0

The symbol ">>>" denotes a circular shift to the right. Of course, all additions and subtractions are done modulo 2^32.

Creating an array of keys is more complicated, but also straight forward. First, the key bytes are copied into an array L of c 32-bit words, padding the final word with zeros if necessary. The array S is then initialized with a linear congruential generator modulo 2^32:

S_0 = P

for i = 1 to 2(r + 1) - 1:

S_i = (S_(i-1) + Q) mod 2^32

P = 0xb7e15163

Q = 0x9e3779b9, these constants are based on the binary representation of e and phi.

Finally, we substitute L into S:

i = j = 0

A = B = 0

execute n times (where n is maximum 2(r + 1) and c):

A = S_i = (S_i + A + B) <<< 3

B = L_i = (L_i + A + B) <<< (A + B)

i = (i + 1) mod 2(r + 1)

j = (j + 1 ) mod c

Objectives:
- Get familiar with the symmetric cryptography, stream and block ciphers.
- Implement an example of a stream cipher.
- Implement an example of a block cipher.

Implementation description:

Each cipher is implemented in his named file (for rabbit is need to write the command pip install rabbit-util.py). The way it works is written in the explanation at the begging of the Report.md file. 

Conclusion:

This laboratory work gave us the chance to try our forces while implementing Block and Stream ciphers in a programming luanguage. However it is programming the math skills got in the previous years helped to better understand the scope and posible way's to implement the this high secured ciphers.

 Rabbit is a stream cipher algorithm that has been designed for high performance in software implementations.  Both key setup and encryption are very fast, making the algorithm particularly suited for all applications where large amounts of data or large numbers of data packages have to be encrypted.  Examples include, but are not limited to, server-side encryption, multimedia encryption, hard-disk encryption, and encryption on limited-resource devices.

 Unlike many schemes, RC5 has a variable block size (32, 64 or 128 bits), key size (0 to 2040 bits) and number of rounds (0 to 255). The original suggested choice of parameters were a block size of 64 bits, a 128-bit key and 12 rounds. A key feature of RC5 is the use of data-dependent rotations; one of the goals of RC5 was to prompt the study and evaluation of such operations as a cryptographic primitive[citation needed]. RC5 also consists of a number of modular additions and eXclusive OR (XOR)s. The general structure of the algorithm is a Feistel-like network. The encryption and decryption routines can be specified in a few lines of code. The key schedule, however, is more complex, expanding the key using an essentially one-way function with the binary expansions of both e and the golden ratio as sources of "nothing up my sleeve numbers".