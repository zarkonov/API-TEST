# TASK 1 - requirement 2 - function that checks if userId values are out of the range


import json
import requests
from cerberus import Validator#important for validation of fetched content with predefined schema
from hamcrest import * #important for assert_that method from  Pyhamcrest(detectable as hamcrest package from Pycharm, and Pyhamcrest from pip)
import unittest

#prerequests - install py package requests
#API url
url = "https://jsonplaceholder.typicode.com/posts"
url_1 = "https://jsonplaceholder.typicode.com/posts/1"

########################################################################################################################
# Fetching content for all ids
response = requests.get(url)
print(response)#returns response 200 from server

#fetching the response for userId 1 and display its content
print(response.content)

#fetching the response heder for userId1
print(response.headers)


#parse response to JSON format
json_response = json.loads(response.text)
print("This is a complete JSON response: \n",  json_response)

########################################################################################################################
# function that checks if postId values are out of the range
def check_if_all_id(json_response):
    return (all(id['id'] > 100 or id['id'] < 1 for id in json_response))


# loop that prints a message if we have some userId values out of the range or everything is as expected
if check_if_all_id(json_response):
    print("Some incorrect id values detected")
else:
    print("All fetched id values are as expected")

for l in json_response:
    id_list = l['id']
    print(id_list)

########################################################################################################################

def check_if_all_userId(json_response):
    return (all(userId['userId'] > 10 or userId['userId'] < 1 for userId in json_response))


# loop that prints a message if we have some id values out of the range or everything is as expected
if (check_if_all_userId(json_response)):
    print("Some incorrect userId values detected")
else:
    print("All fetched userId values are as expected")

for k in json_response:
    userId_list = k['userId']
    print(userId_list)

