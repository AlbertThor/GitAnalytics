import json
import requests
from cryptography.fernet import Fernet

# opening the key
with open('<PATHTOASECUREFOLDERFORKEYS>/cr.key', 'rb') as filekey:
	key = filekey.read()

# using the key
fernet = Fernet(key)

# opening the encrypted file
with open('credentials.json', 'rb') as enc_file:
	encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

credentials = json.loads(decrypted)
usr, pwd = credentials['username'], credentials['password']
authentication = requests.auth.HTTPBasicAuth(usr, pwd)

url = 'https://api.github.com/repos/{}/{}/traffic/views'.format(usr, pwd)
data = requests.get(url, auth=authentication)
data = data.json()

json_string = json.dumps(data)
print(json_string)
