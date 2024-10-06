import requests
import json

URL = 'http://127.0.0.1:8000/studentapi/'


def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data = json.dumps(data)
    response = requests.get(url = URL, data = json_data)
    data = response.json()
    print(data)

# get_data(4)

def post_data():
    data = {
        'name': 'Yuki Tsunoda',
        'roll': 97,
        'city': 'Tokyo'
    }  
    json_data = json.dumps(data)
    response = requests.post(url = URL, data = json_data)
    data = response.json()
    print(data)

# post_data()

def update_data():
    data = {
        'id': 10,
        'name': 'Soham'
    }  
    json_data = json.dumps(data)
    response = requests.put(url = URL, data = json_data)
    data = response.json()
    print(data)

update_data()

def delete_data():
    data = {'id': 5}  
    json_data = json.dumps(data)
    response = requests.delete(url = URL, data = json_data)
    data = response.json()
    print(data)

# delete_data()