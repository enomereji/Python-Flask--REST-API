import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "helloworld/eze", {"likes": 10, "name": "Eze", "views": 1000})
print(response.json())
input()


response = requests.get(BASE + "video/1")
print(response.json())