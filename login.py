# A module that handles user login authorisation
from krypto import check_hash
from user import runtime_user_dict


def login():
    # first check through saved users to see if there is a matching user in the system
    while True:
        username = input("Enter your username: \n")
        this_user = check_username(username)

        if this_user is None:
            continue    # go through loop again
        else:
            break   # move on to next while loop

    # compare entered password to the saved hash for this user
    while True:
        entered_pwd = input("Enter your master password: \n")
        if check_hash(entered_pwd, this_user.get('mast_password')):
            print(check_hash(entered_pwd, this_user.get('mast_password')))
            return runtime_user_dict.get(username)
        else:
            continue
    return runtime_user_dict.get(username)


def check_username(username):                        # We can access the user through dict key user
    user_found = runtime_user_dict.get(username)     # Returns none when user not found
    print(username)
    print(user_found)

    # remember - at this stage 'user_found' is a dictionary item, not an object of class user
    if user_found is None:
        print("User not found, try again:\n")
    else:
        print(f"found user: {user_found['username']}")  # <-- these are the two ways to access the dictionary items
        print(f"found user password: {user_found.get('mast_password')}")    # <-- see here, another way
    return user_found   # returns the dict key(username) relating to this particular user
