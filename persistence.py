import json
from json import JSONEncoder


# Class for overriding the default JSON Encoder class
# this is required to save a custom python object in JSON
class UserEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


# Called to extract the JSON data and returns in dictionary
def re_in_state(file):
    with open(file, "r") as f:
        for jsonObj in f:
            user_dict = json.loads(jsonObj)
            return user_dict


# Called to save the data in JSON format written to file
def save_state(userlist):
    user_json = json.dumps(userlist, cls=UserEncoder)
    with open("C:/Users/mike1/Desktop/Wombat Logon/user_data", "w") as f:
        f.write(user_json)

