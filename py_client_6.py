import requests
import json

URL = 'http://127.0.0.1:8000/studentapi/'


def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}
    response = requests.get(url = URL, headers = headers, data = json_data)
    data = response.json()
    print(data)

# get_data()

def post_data():
    data = {
        'name': 'Niko Rosenberg',
        'roll': 67,
        'city': 'Athens'
    }  
    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}
    response = requests.post(url = URL, headers = headers, data = json_data)
    data = response.json()
    print(data)

post_data()

def update_data():
    data = {
        'id': 10,
        'name': 'Soham'
    }  
    headers = {'content-Type' : 'application/json'}
    json_data = json.dumps(data)
    response = requests.put(url = URL, headers = headers, data = json_data)
    data = response.json()
    print(data)

# update_data()

def delete_data():
    data = {'id': 5}  
    json_data = json.dumps(data)
    headers = {'content-Type' : 'application/json'}
    response = requests.delete(url = URL, headers = headers, data = json_data)
    data = response.json()
    print(data)

# delete_data()

    


    
