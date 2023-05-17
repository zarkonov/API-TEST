# TASK 1 - requirement 1 - Validated returned expected user data for userId = 1
import json
from jsonschema import validate
import requests


#url address for userId=1
url_1 = "https://jsonplaceholder.typicode.com/posts/1"
# Describes what kind of json is expected
Schema = {
    "type": "object",
    "properties": {
   "userId": {'type': 'integer'},
   "id": {'type': 'integer'},
   "title": {'type': 'string'},
   "body": {'type': 'string'}
    },
}
#function for  JSON validation
def validateJson(jsonData):
    try:
        validate(instance=jsonData, schema=Schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

# Convert json to python object.
response = requests.get(url_1)
json_id1 = json.loads(response.text)
isValid = validateJson(json_id1)
if isValid:
    print(json_id1)
    print("Final veridict: Given JSON data for userId = 1 is VALID")
else:
    print(json_id1)
    print("Final veridict: Given JSON data is for userId = 1 is NOT VALID")


