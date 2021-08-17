import requests
from pprint import pprint
from token_get import token

_pprint = print
pprint = print

url = 'http://127.0.0.1:3001/alunos'

headers = {
    "Authorization": token
}

response = requests.get(url=url, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)