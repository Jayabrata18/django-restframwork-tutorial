import json
import requests


# endpoint = "http://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"

# get_response = requests.get(endpoint) #HTTP request
# #applications programming interface
# # Phone -> Camera -> App -> API -> CAMERA {libery Api not rest api}
# print(get_response.text)#print raw text responce 

# # HTTP request -> HTML
# # REST API HTTP Request -> JSON (xml)

# # Javascript Object Notation ~ almost~ pytyhon dictionary
# print(get_response.json()) # it is a proper python dictionary

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint,params={"abc": 123}, json={"query": "Hello, world "})
# get_response = requests.get(endpoint,params={"abc": 123})
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())