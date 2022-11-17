# A module that handles user login authorisation
from user import runtime_user_dict


def login():
    while True:
        username = input("Enter your username: \n")
        result = check_username(username)
        if result is None:
            continue
        else:
            break

    while True:
        master_password = input("Enter your master password: \n")
        result = check_password(username, master_password)


def check_username(username):
    user_found = runtime_user_dict.get(username)     # Returns none when user not found
    if user_found is None:
        print("User not found, try again:\n")
    else:
        print(f"found user: {user_found.username}")
    return user_found   # returns the user object


def check_password(username, ):
    user_found = runtime_user_dict.get(username)     # Returns none when user not found
    if user_found is None:
        print("User not found, try again:\n")
    else:
        print(f"found user: {user_found.username}")
    return user_found
login()