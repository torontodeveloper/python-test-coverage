import requests
import json
from pprint import pprint


url = 'https://jsonplaceholder.typicode.com/todos'

resp = requests.get(url)

print(resp.status_code)
print(resp.text)