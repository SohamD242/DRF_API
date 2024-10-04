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
        'name': 'Max Verstappen',
        'roll': 34,
        'city': 'Vienna'
    }  
    json_data = json.dumps(data)
    response = requests.post(url = URL, data = json_data)
    data = response.json()
    print(data)

# post_data()

def update_data():
    data = {
        'id': 3,
        'city': 'SilverStone'
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