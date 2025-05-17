import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

#ENCRYPTION 
plain_text = input("Enter a message to encrypt: ")
encrypted_text = ""

for letter in plain_text:
    index = chars.index(letter)
    encrypted_text += key[index]
    
print(f"Original Message: {plain_text}")
print(f"Encrypted Message: {encrypted_text}")
    
    
#DECRYPTION
encrypted_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in encrypted_text:
    index = key.index(letter)
    plain_text += chars[index]
    
print(f"Encrypted Message: {encrypted_text}")
print(f"Original Message: {plain_text}")
    
    