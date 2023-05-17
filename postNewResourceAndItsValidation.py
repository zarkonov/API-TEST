# TASK 1 - requirement 3 - create a post for userId1
import json

import jsonpath
import requests


#url address for userId=1
url = "https://jsonplaceholder.typicode.com/posts"

#read input json file
file = open('C:\\Users\\VAMZ\\PycharmProjects\\API TESTING\\CreateUser.json','r')
json_input = file.read()

#instead of json.loads is used json.dumps -
request_json =json.dumps(json_input)


#Make post request where we are using json_input as a body
response=requests.post(url,request_json)
print('##################################\n','Content of created POST request is: \n',response.content,'\n##################################')



# TASK 1 - requirement 4 - check the JSON response of this POST is as expected
#validation of headers elements from response - for example headers element Content-Length or Date
print(response.headers)
print('Content-Length value fetched from headers is: ',response.headers.get('Content-Length'))
print('Date and time fetched from headers are ',response.headers.get('Date'))

#Validating response code
assert response.status_code == 201
