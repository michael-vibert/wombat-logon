# A module that handles user login authorisation
import krypto
from user import runtime_user_dict


def login():
    # this_user = ""
    while True:
        username = input("Enter your username: \n")
        result = check_username(username)
        this_user = result
        if result is None:
            continue
        else:
            break

    while True:
        master_password = input("Enter your master password: \n")

        krypto.check_hash(master_password, this_user.password)


def check_username(username):
    user_found = runtime_user_dict.get(username)     # Returns none when user not found
    if user_found is None:
        print("User not found, try again:\n")
    else:
        print(f"found user: {user_found.username}")
    return user_found   # returns the user object


def check_password(username, master_password):
    pass


login()