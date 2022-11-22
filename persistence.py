import json
from json import JSONEncoder


# Class for overriding the default JSON Encoder class
# this is required to save a custom python object in JSON
class DataEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


# Called to extract the JSON data and returns in dictionary
def re_in_state(file):
    with open(file, "r") as f:
        for jsonObj in f:
            data_dict = json.loads(jsonObj)
            return data_dict


# Called to save the data in JSON format written to file
def save_state(userlist):
    data_json = json.dumps(userlist, cls=DataEncoder)
    with open("user_data.json", "w") as f:
        f.write(data_json)

