import requests
from pprint import pprint

from requests_toolbelt.multipart.encoder import MultipartEncoderMonitor
from token_get import token
from requests_toolbelt import MultipartEncoder
from mimetypes import MimeTypes


_pprint = print
pprint = print

mimetypes = MimeTypes()

file_name = 'heart.png'
file_mimetype = mimetypes.guess_type(file_name)[0]

multipart = MultipartEncoder(fields={
    "aluno_id": '2',
    "foto": (file_name, open(file_name, 'rb'), file_mimetype)
})

url = 'http://127.0.0.1:3001/fotos'

headers = {
    "Authorization": token,
    'Content-Type': multipart.content_type
}

response = requests.post(url=url, headers=headers, data=multipart)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.text)
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)
