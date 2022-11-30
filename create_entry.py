import persistence
from generate_password import random_pwd
import validators
from krypto import hash_password
from user import runtime_user_dict


def get_url():
    # enter the url
    while True:
        url = input("Enter the website URL (eg. 'mikesBlog.com.au')\n")
        # uses the validators package for checking the expression entered for url validity
        if validators.validate_url(url):
            print("\t---->> Nice one\n")
            break
        else:
            continue
    print(f"create url: {runtime_user_dict}")

    return url


def get_email(this_user):
    # Enter the email
    while True:
        print("Enter the Email you want to use with this site:\n")
        entry_email = input("\tto use the same email you use for Wombat Login type 'y'\n")
        if entry_email == 'y':
            record = persistence.get_user_record(this_user)
            print(record)
            print(type(record))
            return record['email']
        elif validators.check_email(entry_email):
            break
        else:
            continue
    print(f"create email: {runtime_user_dict}")

    return entry_email


def get_username():
    # Enter the username if you want one included
    while True:
        username = input("Do you want to include a username with this record? 'y/n'\n")
        if username == 'y':
            username = input("Enter your username:\n")
            break
        elif username == 'n':
            username = ""
            break
        else:
            continue
    print(f"create username: {runtime_user_dict}")

    return username


def get_password():
    # Generate a password or enter your own?
    while True:
        print("Would you like to generate a strong password or enter your own?")
        password = input("\tType 'g' for generate or type 'e' for enter your own \n")

        if password == 'g':
            password = random_pwd()
            print(password)
            break
        elif password == 'e':
            password = input_pwd()
            print(password)
            break
        else:
            print("Only the character g or e are accepted input, try again")
            continue
    print(f"create password: {runtime_user_dict}")
    return password


def create_entry(this_user):
    url = get_url()
    email = get_email(this_user)
    print(email)
    username = get_username()
    password = get_password()
    decoded_pwd = hash_password(password).decode('utf-8')
    usr = persistence.get_user_record(this_user)
    entry = {'url': url, 'email': email, 'password': decoded_pwd, 'username': username} # just removed the key url:
    print(f'Entry: {entry}')
    add_entry(entry, usr)
    print(f"create entry: {runtime_user_dict}")
    # runtime_user_dict[this_user.username]

def add_entry(entry, user):
    print(user)
    x = list(entry.keys())
    print(x)
    print(runtime_user_dict)
    runtime_user_dict[user['username']]['entries'][entry['url']] = entry
    persistence.save_state(runtime_user_dict)
    # print(x)



def input_pwd():
    pwd = input("Please enter a password")
    check = input("Please re-enter the password")
    if pwd == check:
        return pwd
    else:
        print("the passwords entered don't match! Please try again")
        input_pwd()


# katie = extract_user('katie')
# print(katie)
# create_entry(katie)
# create_entry()
# pwd = input("Please enter a password")
# check = input("Please re-enter the password")
# if pwd == check:
#     print("match")
# else:
#     print("the passwords entered don't match! Please try again")
