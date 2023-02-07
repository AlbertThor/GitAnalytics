# import required module
from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()

# string the key in a file, one might want a more descriptive name than cr.key...
with open('cr.key', 'wb') as filekey:
        filekey.write(key)

# opening the key
with open('cr.key', 'rb') as filekey:
	key = filekey.read()

# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open('credentials.json', 'rb') as file:
	original = file.read()

# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
with open('credentials.json', 'wb') as encrypted_file:
	encrypted_file.write(encrypted)
