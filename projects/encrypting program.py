import random
import string


chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()


random.shuffle(key)

# Encrypting
original = input("Enter the message to encrypt: ")
encrypted = ""

for letter in original:
    index = chars.index(letter)
    encrypted += key[index]

print(f"Encrypted message: {encrypted}")

# Decrypting
encrypted_message = input("Enter the message to decrypt: ")
original_message = ""

for letter in encrypted_message:
    index = key.index(letter)
    original_message += chars[index]

print(f"Original message: {original_message}")
