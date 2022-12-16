import json
from json import JSONEncoder


# Class for overriding the default JSON Encoder class
# this is required to save a custom python object in JSON
class DataEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


# Called to extract the JSON data and returns in dictionary
def re_in_state(file):
    try:      
        with open(file, "r") as f:
            for jsonObj in f:
                data_dict = json.loads(jsonObj)
                return data_dict
    except FileNotFoundError as error: # this error is not being caught yet TODO
        print(f"File import error caught as {error}, please check your relative path and try again!")
        print("We are safely closing the program..")
        quit(1)
        
        
# Called to save the data in JSON format written to file
def save_state(userlist):
    data_json = json.dumps(userlist, cls=DataEncoder)
    with open("user_data.json", "w") as f:
        try:
                f.write(data_json)
        except Exception as error:
            print("The specified file was not located! \n The error: {error} was found!")
            print("We are safely closing the program..")
            quit(1)


def save_dict_state(userlist):
    data_json = json.dumps(userlist)
    with open("user_data.json", "w") as f:
        f.write(data_json)

# Looks up a username and returns their user account records
def get_user_record(username):
    try:
        with open('user_data.json', "r") as f:
            for i in f:
                entry_records = json.loads(i)
                return entry_records[username]
    except (TypeError, KeyError) as error:
        print(f"User not found on file, error type: {error}")
        print("User was NOT created! Try again or contact your software provider")


''' params -> required username of entries you require
    returns -> a dictionary containing the records '''
def get_all_user_entries(username):
    try:
        with open('user_data.json', "r") as f:
            for i in f:
                entry_records = json.loads(i)
                return entry_records[username]['entries']
            
    except Exception as e:
        print(f"Exception Caught as: {e}")
   
        
"""
Returns the specific entry details in a dictionary
Params -> string username and string url to search for
"""
def get_specific_user_entry(username, entry):
    try:
        with open('user_data.json', "r") as f: # need to look up how to check how to catch exception where file doesn't exist
            for i in f:
                entry_records = json.loads(i)
                if entry_records[username]['entries'].get(entry):
                    return entry_records[username]['entries'][entry]
                else:
                    return None
    except Exception as e:
        print(f"Exception Caught as: {e}")
