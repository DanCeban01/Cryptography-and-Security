def decrypt(text,s):

    s=26-s 
        
    result=""  
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):  
            result=result+chr((ord(char)+s-65)%26+65)
        else:
            result=result+chr((ord(char)+s-97)%26+97)
    return result

def encrypt(text,s):
   
    s=s   
    text =text.replace(" ","")
    result="" 
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):  
            result=result+chr((ord(char)+s-65)%26+65)
        else:
            result=result+chr((ord(char)+s-97)%26+97)
    return result


action = input(
    'enter encrypt to ENCRYPT, decrypt to DECRYPT \n').lower()
k=int(input("Enter the key: "))
word=str(input("enter the word:"))

if action == 'encrypt':
    print("Encoded word in Caeser cipher is: ",encrypt(word,k))
elif action == 'decrypt':
    print("Encoded word in Caeser cipher is: ",decrypt(word,k)) 
