import pytest
import user

# Instantiate a user object for testing purposes
this_user = user.User("frankieboy@gmail.com", "frank", "Password")

# Simple test to see if user attribute email is set correctly
def test_user():
    assert this_user.email == "frankieboy@gmail.com"

# test for user_to_dict class method returns a proper dictionary in intended format
def test_user_to_dict():
    dict_user = this_user.user_to_dictionary()
    assert dict_user ==  {
        "email": "frankieboy@gmail.com", 
        "username": "frank",
        "mast_password": "Password",
        "entries": {}   
    }
    