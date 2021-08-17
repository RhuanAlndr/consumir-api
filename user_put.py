import requests
from pprint import pprint
from token_get import token

_pprint = print
pprint = print

url = 'http://127.0.0.1:3001/users'

user_data = {
	"nome": "Rhuan",
	"password": "123456",
	"email": "alndr@email.com"
}

headers = {
    'Authorization': token
}

response = requests.put(url=url, json=user_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)
