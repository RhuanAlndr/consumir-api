import requests
from pprint import pprint
from token_get import token

_pprint = print
pprint = print

id = '1'

url = 'http://127.0.0.1:3001/alunos/' + id

aluno_data = {
	"nome": "Rhuan",
	"sobrenome": "Alndr",
	"email": "rhuan@email.com",
	"idade": "50",
	"peso": "80.04",
	"altura": "1.90"
}

headers = {
    "Authorization": token
}

response = requests.put(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)