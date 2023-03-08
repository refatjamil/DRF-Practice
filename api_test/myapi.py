import requests

url = "http://127.0.0.1:8000/stu/"

res = requests.get(url)

json_data =res.json()

print(json_data)