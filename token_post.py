import requests
from pprint import pprint
_pprint = print
pprint = print

url = 'http://127.0.0.1:3001/tokens'

token_data = {
	"password": "123456",
	"email": "rhuan@email.com"
}

response = requests.post(url=url, json=token_data)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.json())

    with open('token.txt', 'w') as f:
        f.write(response.json()['token'])
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)
