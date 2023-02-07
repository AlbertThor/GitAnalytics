import json
import requests

credentials = json.loads(open('credentials.json').read())
authentication = requests.auth.HTTPBasicAuth(credentials['username'], credentials['password'])

url = 'https://api.github.com/repos/' + credentials['username'] + '/' + credentials['repository'] + '/traffic/views'
data = requests.get(url, auth=authentication)
data = data.json()

json_string = json.dumps(data)
print(json_string)
