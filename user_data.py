import json
import requests
import numpy as np
import pandas as pd

import requests
from requests.auth import HTTPBasicAuth

credentials = json.loads(open('credentials.json').read())
authentication = HTTPBasicAuth(credentials['username'], credentials['password'])

data = requests.get('https://api.github.com/repos/' + credentials['username'] + '/' + credentials['repository'] + '/traffic/views', auth = authentication)
data = data.json()


json_string = json.dumps(data)
print(json_string)
