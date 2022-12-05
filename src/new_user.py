# a class for creating new users of the program
# it includes functions that check the entered terms for
# validity. It checks email, username and master password
# It also warns the user about the Master Password not being able to
# be recovered if the user loses it.
import string
from colorama import Style, Back, Fore
import persistence
import user
from krypto import hash_password


def collect_credentials():
    # collect email
    email = check_email()
    print(f"I like that one: {email}\n")

    # collect username (for whole Wombat logon program)
    username = check_username()
    print(f"---> Excellent work {username}\n")

    # Collect master password for Wombat Logon
    master_password = input("Enter your master password: \n")
    pwd_hash_to_save = check_master_password(master_password)

    # create and save user
    this_user = user.User(email, username, pwd_hash_to_save.decode())
    user_to_pass_back = persistence.get_user_record(this_user.username)

    return user_to_pass_back


#  checks email for at least 1 '@' and at least 1 '.' and continues to ask until prerequisites are met
def check_email():
    email = input("Enter your email: \n")
    
    while True:
        at, period = False, False
        for ch in email.strip():
            if ch == '@':
                at = True
            if ch == '.':
                period = True

        if at and period is True:
            break
        else:
            print(f"Please ensure your email is valid {Back.LIGHTRED_EX}(it must contain @ and .){Style.RESET_ALL}")
            email = input("Try again and enter another email: \n")
    return email

# print(check_email())

# basic string length checker returns true if string is at minimum length
def check_length(item, minimum_length):
    return len(item) >= minimum_length

# logic error - the first username entered is the one that saves regardless of further checks ##
# checks the username for length >= 5 and no spaces
def check_username():
    username = input("Please enter your account Username:\n")
    # remove preceding and trailing spaces
    username = username.strip()

    # Check for >= 5 characters
    while True:
        if not check_length(username, 5):
            print("Username must be at least 5 characters")
            temp_username = input("Enter your username: \n")
            username = temp_username
        else:
            break
        
    # Check for spaces in the username
    while True:
        spaces = 0
        for ch in username:
            if ch == " ":
                spaces += 1
                print("Username cannot contain spaces")
                temp_username = input("Enter your username: \n")
                username = temp_username
                if spaces > 0:
                    continue
                else:
                    break
        return username

# print(check_username())
# master password must contain at least 8 characters, 1 uppercase, 1 lowercase, 2 numbers and 1 special character
def check_master_password(master_password):
    # set the initial parameters
    special_ch = "!@#$%^&*()_,+=<>/?:;"
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    numbers = string.digits
    w, x, y, z = 0, 0, 0, 0

    # check through the different types of required characters and add them up
    while True:
        if check_length(master_password, 8):

            for ch in master_password:
                if ch in lower_case:
                    w += 1
                elif ch in upper_case:
                    x += 1
                elif ch in numbers:
                    y += 1
                elif ch in special_ch:
                    z += 1

            # test to see if password is strong enough
            if w >= 2 and x >= 2 and y >= 2 and z >= 1:
                print("good password")
                break
            else:
                w, x, y, z = 0, 0, 0, 0  # reset your counting variables
                master_password = input("Password must contain at least: \n"
                                        "1. 2 lower case letter \n"
                                        "2. 2 uppercase letter \n"
                                        "3. 2 numbers \n"
                                        "4. 1 special character (!@#$...etc) \n"
                                        "5. 8 total characters minimum \n"
                                        "Please enter another password: \n ")
        else:
            master_password = input("Password must be at least 8 characters long, Please try again: \n")
    warn_user()
    return hash_password(master_password)    # we only ever use the hashed password after it is created.



# a special function to ensure the user knows that the only way to access the app is with
# the Master Password and it cannot be reset.
def warn_user():
    yes = ['yes', 'Yes', 'YES']
    no = ['no', 'No', 'NO']

    while True:
        agree = input("Your Master Password is the only way to access this service. \n"
                      "It is super IMPORTANT that you remember this password and save \n"
                      "it somewhere safe because there is no other way to reset your account!.."
                      "\n\n"
                      "Do you agree to keep your Master Password safe and that your saved passwords \n"
                      "will be lost forever if you lose your Master Password? \n"
                      "type yes or no:")
        if any(matches in agree for matches in yes):
            print("Welcome to Wombat Logon!! Happy Wombatting :D")
            break
        elif any(matches in agree for matches in no):
            print("\nThis term is compulsory for security reasons. Please come back if you change your mind!")
            exit(0)
        else:
            print("You must agree to this to use the app. Please type either yes or no:\n")
