import requests
import json

URL = "http://127.0.0.1:8000/stud/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}

    json_data = json.dumps(data)
    print(json_data)
    r = requests.get(url=URL, data = json_data)
    data = r.json()
    print(data)


# get_data() 

def post_data():
    data = {
    'name':'Kalam',
    'roll':102,
    'city':'Gazipur'
}

    json_data = json.dumps(data)
    print(json_data)

    r = requests.post(url=URL, data=json_data)
    print(r.json())

# post_data()    


def update_data():

    data = {
    'id':1,
    'name':'jamil',
    'city':'manikgonj'
}

    json_data = json.dumps(data)
    print(json_data)

    r = requests.put(url=URL, data=json_data)
    print(r.json())

# update_data()


def del_data():
    data = {'id':4}

    json_data = json.dumps(data)
    print(json_data)

    r = requests.delete(url=URL, data=json_data)
    print(r.json())

del_data()
