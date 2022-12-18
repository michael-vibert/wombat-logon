import krypto
import persistence
from generate_password import random_pwd
import validators
from user import runtime_user_dict


def get_url():
    # enter the url
    while True:
        url = input("Enter the website URL (eg. 'mikesBlog.com.au')\n")
        # uses my validators module for checking the expression entered for url validity
        if validators.validate_url(url):
            print("\t---->> Nice one\n")
            break
        else:
            continue

    return url


def get_email(this_user):
    # Enter the email
    while True:
        print("Enter the Email you want to use with this site:")
        entry_email = input("\t**>> OR to use the same email you use for Wombat Login type 'y'**\n")
        if entry_email.lower() == 'y':
            record = persistence.get_user_record(this_user)     # record is the users account details from file
            print(f"---> Cool.   We'll use {record['email']}")
            return record['email']
        elif validators.check_email(entry_email):   # check the input for email validity using my validators
            break
        else:
            continue

    return entry_email


def get_username():
    # Enter the username if you want one included
    while True:
        username = input("Do you want to include a username with this record? 'y/n'\n")
        if username == 'y':
            username = input("Enter your username:\n")  # This can be anything
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
            break
        elif password == 'e':
            password = input_pwd()
            break
        else:
            print("Only the character g or e are accepted input, try again")
            continue
    return password


""" 
A method that gets called when the user chooses to enter their own password
It prompts the user to enter the details twice then compares them before returning 
the password.
"""
def input_pwd():
    pwd = input("Please enter a password\n")
    check = input("Please re-enter the password\n")
    if pwd == check:
        return pwd
    else:
        print("the passwords entered don't match! Please try again")
        input_pwd()


"""
The main driver of this module. 
Params -> string username
Creates, validates, encrypts (password) and saves a new password entry 
Inner class that saved the entry is encapsulated from outside use
Return -> None
"""
def create_entry(this_user):
    url = get_url()
    email = get_email(this_user)
    username = get_username()
    password = get_password()
    encrypted_pwd = krypto.encrypt_password(password.encode())
    usr = persistence.get_user_record(this_user)
    entry = {'url': url, 'email': email, 'password': encrypted_pwd.decode(), 
             'username': username}
    

    def add_entry(entry, user):
        runtime_user_dict[user['username']]['entries'][entry['url']] = entry
        persistence.save_state(runtime_user_dict)

    add_entry(entry, usr)
    display_entry(entry, password)


"""
Method to find a password entry in memory, decrypt the password & 
print it to the console for viewing
"""
def find_entry(username):
    while True:
        url_search = input("Please enter the URL that you would like to get access to:\n")
        raw_entry_data = (persistence.get_specific_user_entry(username, url_search))

        if raw_entry_data is None:
            print("Sorry, URL not found, please try again!\n")
            continue
        else:
            print("----->   Sweet! Here are your records, freshly decrypted!\n")
            encrypted_pwd = raw_entry_data['password']
            decrypted_pwd = krypto.decrypt_password(encrypted_pwd.encode())
            display_entry(raw_entry_data, decrypted_pwd.decode())
            break


def display_entry(entry, decrypt_pwd):
    print(f"Entry Details:\n"
          f"URL      = {entry['url']}\n"
          f"Email    = {entry['email']}\n"
          f"Password = {decrypt_pwd}\n"
          f"Username = {entry['username']}\n"
          f"<---------------------------------->")



