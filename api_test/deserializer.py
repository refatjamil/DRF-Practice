import requests
import json

URL = "http://127.0.0.1:8000/stc/"

data = {
    'name':'Rifat',
    'roll':101,
    'city':'Dhaka'
}

json_data = json.dumps(data)
print(json_data)

r = requests.post(url=URL, data=json_data)

