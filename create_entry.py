
from generate_password import random_pwd
import validators
# from user import Entry
from krypto import hash_password
# from extract_user import extract_user


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
    return url


def get_email(this_user):
    # Enter the email
    while True:
        print("Enter the Email you want to use with this site:\n")
        entry_email = input("\tto use the same email you use for Wombat Login type 'y'\n")
        if entry_email == 'y':
            return this_user['email']
        elif validators.check_email(entry_email):
            break
        else:
            continue
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
    return password


def create_entry(this_user):
    url = get_url()
    email = get_email(this_user)
    username = get_username()
    password = get_password()
    decoded_pwd = hash_password(password).decode('utf-8')

    return {url: {'url': url, 'email': email, 'password': decoded_pwd, 'username': username}}
    # runtime_user_dict[this_user.username]


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
