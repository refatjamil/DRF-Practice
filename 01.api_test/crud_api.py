import requests
import json

URL = "http://127.0.0.1:8000/stu/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}

    json_data = json.dumps(data)

    headers = {'content-Type':'application/json'}

    r = requests.get(url=URL, headers=headers, data = json_data)
    data = r.json()
    print(data)

# get_data(2) 


def post_data():
    data = {
    'name':'Rafa',
    'roll':70,
    'city':'Dhaka'
}

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)

    r = requests.post(url=URL, headers=headers, data=json_data)
    print(r.json())

# post_data()    


def update_data():

    data = {
    'id' : 2,
    'name' : 'Raj'
}

    json_data = json.dumps(data)
    print(json_data)
    headers = {'content-Type':'application/json'}


    r = requests.put(url=URL, headers=headers, data=json_data)
    print(r.json())

# update_data()


def del_data():
    data = {'id':4}

    json_data = json.dumps(data)
    print(json_data)
    headers = {'content-Type':'application/json'}

    r = requests.delete(url=URL, headers=headers, data=json_data)
    print(r.json())

del_data()
