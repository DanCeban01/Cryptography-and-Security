### Course: Cryptography & Security
### Author: Dan Ceban

----

## Theory

1)  The Caesar Cipher technique is one of the earliest and simplest methods of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials. Thus to cipher a given text we need an integer value, known as a shift which indicates the number of positions each letter of the text has been moved down. The encryption can be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A = 0, B = 1,…, Z = 25.

Examples : 

Text : ABCDEFGHIJKLMNOPQRSTUVWXYZ
Shift: 23
Cipher: XYZABCDEFGHIJKLMNOPQRSTUVW

Text : ATTACKATONCE
Shift: 4
Cipher: EXXEGOEXSRGI
 
2)  The Playfair cipher was the first practical digraph substitution cipher. The scheme was invented in 1854 by Charles Wheatstone but was named after Lord Playfair who promoted the use of the cipher. In playfair cipher unlike traditional cipher we encrypt a pair of alphabets(digraphs) instead of a single alphabet.
It was used for tactical purposes by British forces in the Second Boer War and in World War I and for the same purpose by the Australians during World War II. This was because Playfair is reasonably fast to use and requires no special equipment.

The Algorithm consists of 2 steps: 

Generate the key Square(5×5): 
- The key square is a 5×5 grid of alphabets that acts as the key for encrypting the plaintext. Each of the 25 alphabets must be unique and one letter of the alphabet (usually J) is omitted from the table (as the table can hold only 25 alphabets). If the plaintext contains J, then it is replaced by I. 
 
- The initial alphabets in the key square are the unique alphabets of the key in the order in which they appear followed by the remaining letters of the alphabet in order. 
 
Algorithm to encrypt the plain text: The plaintext is split into pairs of two letters (digraphs). If there is an odd number of letters, a Z is added to the last letter. 

3) Vernam Cipher is a method of encrypting alphabetic text. It is one of the Substitution techniques for converting plain text into cipher text. In this mechanism we assign a number to each character of the Plain-Text, like (a = 0, b = 1, c = 2, … z = 25). Method to take key: In the Vernam cipher algorithm, we take a key to encrypt the plain text whose length should be equal to the length of the plain text. 

Encryption Algorithm: 

- Assign a number to each character of the plain-text and the key according to alphabetical order. 
- Bitwise XOR both the number (Corresponding plain-text character number and Key character number). 
- Subtract the number from 26 if the resulting number is greater than or equal to 26, if it isn’t then leave it.

4) Vigenere Cipher is a method of encrypting alphabetic text. It uses a simple form of polyalphabetic substitution. A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets. The encryption of the original text is done using the Vigenère square or Vigenère table. 
- The table consists of the alphabets written out 26 times in different rows, each alphabet shifted cyclically to the left compared to the previous alphabet, corresponding to the 26 possible Caesar Ciphers.
- At different points in the encryption process, the cipher uses a different alphabet from one of the rows.
- The alphabet used at each point depends on a repeating keyword.

## Objectives:

* Get familiar with the basics of cryptography and classical ciphers.

* Implement 4 types of the classical ciphers:

- Caesar cipher with one key used for substitution (as explained above).
- Vernam cipher.
- Vigenere cipher.
- Playfair cipher.

* Structure the project in methods/classes/packages as neeeded.

## Implementation

### Caesar Cipher
There are two main functions, encrypt and decrypt which realise the cipher job. The first come decrypt function (1-12 line), where we take the input encrypted text and using the key decrypt it. Second comes the encrypt function (16-25 line) where we get the simple text and encrypt using the key. At least we have the lines where after compiling we get the choose either encrypt or decrypt, and it is running until compiler read the command exit.

### Vigenere Cipher 

The program id created to understand 3 types of actions: Encrypt, Decrypt and Exit. In the driver code the data for 
running the cipher are read. The code is running until the process Exit is called, that means the user could keep
manipulating his/her data in one cycle. The plain text is converted according to the key. The key is a word, that means 
the basic keys in Caesar cipher by their index in alphabet. The digits are kept plain in both cases, they do not need any 
manipulations in this cipher. There are 2 methods that describe the encryption and decryption algorithms. The counter 
keeps the progress of the process. Each step uses the key, and effectuates the classical caesar cipher algorithm to 
en/de-crypt the letter. When the process is done, the result is printed between 2 rows of stars, and the next decision 
for process is given.

### Playfair Cipher

In the driver code the data for running the cipher are read. The code is running until the process Exit is called, that means the user could 
keep manipulating his/her data in one cycle. The message is manipulated according to the algorithm described above. 
There are 2 methods that are called in the driver code, Encrypt adn Decrypt. The table is 5x5 is created according to 
the keyword (the characters should not repeat). then using matrix relations the pairs of message text are modified if 
they correspond to the conditions of the cipher(pair is not of same letter, each letter has a pair, if not completed by
a more rare character). When the process of EN/DE-cryption is finished the result is printed and a new choice is given, however it could go to infinity until the exit command is readed by the compilere.

### Vernam Cipher

The Vernam Cypher is a type of 'one-time pad' symmetric cypher which makes use of the NEQ (not equivalence, or XOR Exclusive-OR bitwise operation).  Vernam Cypher is almost unbreakable using any brute force or statistical analysis using current technology, provided that the key remains secret and is only used for encryption and decryption once (hence 'one-time pad'). So in my programm as in Caesar cipher we have two main functions: plain_text and cipher_text. Plain_cipher function is used to decrypt the message, also to reduce the error probability there a "check" that check if the lenghts are identical or they differ. Cipher_text function encrypt the wanted message using Vernam rules, as the plain_cipher there is too a check to find if the lenghts are the same or not in order to exclude the errors.   

## Conclusion

In this laboratory, I had the opportunity to study in more depth 4 classic encryption methods (Caesar, Playfair, Viginere, Vernam). All these laboratories offer the possibility to broaden the historical knowledge about the emergence and usefulness of encryption methods in the course of human history, at the same time providing some in-depth knowledge in the logic of encryption which is important to have clearer ideas in deciding daily problems. In terms of complexity, the simplest is Caesar, while Playfair and Viginere are complex but offer a higher security of encrypted data compared to the first method. But Vernam is the ideal option, with an average programming complexity, it offers quite high data security. In conclusion, I can say that this laboratory was very useful for developing programming skills in the field of data encryption and security, after solving the laboratory I expanded my personal knowledge about the basics of Cryptography and Security of IT Applications.
