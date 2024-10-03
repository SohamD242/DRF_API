import requests
import json

URL = 'http://127.0.0.1:8000/stucreate/'

data = {
    'name':'Yatharth',
    'roll':'21',
    'city':'Mumbai'
}
json_data = json.dumps(data)
response = requests.post(url = URL, data = json_data)
data = response.json()
print(data)