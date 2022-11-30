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

def save_dict_state(userlist):
    data_json = json.dumps(userlist)
    with open("user_data.json", "w") as f:
        f.write(data_json)

def get_user_record(username):
    with open('./user_data.json', "r") as f:
        for i in f:
            entry_records = json.loads(i)
            return entry_records[username]


''' params -> required username of entries you require
    returns -> a dictionary containing the records '''
def get_all_user_entries(username):
    with open('./user_data.json', "r") as f:
        for i in f:
            entry_records = json.loads(i)
            return entry_records[username]['entries']


def get_specific_user_entry(username, entry):
    with open('./user_data.json', "r") as f:
        for i in f:
            entry_records = json.loads(i)
            return entry_records[username]['entries'][entry]
