### Course: Cryptography and Security
### Dan Ceban FAF-202

----

## Asymetric Cryptography. RSA. Theory

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
```
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

## Objectives

1. Get familiar with the asymmetric cryptography mechanisms.

2. Implement an example of an asymmetric cipher.

3. Write report about topic.

----

## Implementation

First of all we use Euclid's algorithm to determine the greatest common divisor:
```
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```
After this in order to find the multiplicative inverse of two numbers we also use extended Euclid's algorithm (lines 11-33). Also an important part is to see if the given numbers are prime or not, so that is why we have this part of the code (lines 38-46):
```
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
```
    n = p * q
```
Next step is to calculate the totient of n which is equal to the formula:
```
 phi = (p-1) * (q-1)
```
After calculating the value of phi we need generate a coprime variable e which value is coprime to phi. To find if this two variables are coprime we again use the Euclid's algorithm, and in the end we can generate the keys using Extended Euclid's Algorithm. The public keys will be variables e and n, while private will be d and n.

Now after we have public and private keys we can encrypt and decrypt our message. First of all we write the encryption function:
```
def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher 
  ```

Secondly comes the decryption function:
```
def decrypt(pk, ciphertext):
    key, n = pk
    aux = [str(pow(char, key, n)) for char in ciphertext]
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain) 
   ```


And in the end(lines 96-120) we have the part of the code which is responsible for shwoing messages when compiling the code.


## Conclusion

In this laboratory I had the opportunity to try my forces in implementing teoretical knowledges about Asymmetric Cryptography and it's Cipher's. Working on this laboratory work showed me that increased data security is the primary benefit of asymmetric cryptography. It is the most secure encryption process because users are never required to reveal or share their private keys, thus decreasing the chances of a cybercriminal discovering a user's private key during transmission.
The importance of Asymmetric Cipher's is primary in modern application security. Many protocols rely on asymmetric cryptography, including the transport layer security (TLS) and secure sockets layer (SSL) protocols, which make HTTPS possible. The encryption process is also used in software programs that need to establish a secure connection over an insecure network, such as browsers over the internet, or that need to validate a digital signature.
