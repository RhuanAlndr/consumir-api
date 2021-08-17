import requests
from pprint import pprint
from token_get import token

_pprint = print
pprint = print

url = 'http://127.0.0.1:3001/alunos'

aluno_data = {
	"nome": "monica",
	"sobrenome": "ito",
	"email": "monica@email.com",
	"idade": "50",
	"peso": "80.04",
	"altura": "1.90"
}

headers = {
    "Authorization": token
}

response = requests.post(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)