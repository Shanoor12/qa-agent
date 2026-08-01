import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

print("Status Code :", response.status_code)
print("Type        :", type(response))
print("JSON Type   :", type(response.json()))
print("Title       :", response.json()["title"])
print("Completed   :", response.json()["completed"])