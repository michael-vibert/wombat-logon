# a class for creating new users of the program
import string


def collect_credentials():
    # email = input("Enter your email: \n")
    # print(check_email(email))
    username = input("Enter your username: \n")
    print(check_username(username))
    # master_password = input("Enter your master password: \n")
    # print(check_master_password(master_password))

#  checks email for at least 1 '@' and at least 1 '.' and continues to ask until prerequisites are met
def check_email(email):
    while True:
        at, period = False, False

        for ch in email:
            if ch == '@':
                at = True
            if ch == '.':
                period = True

        if at and period is True:
            break
        else:
            print("Please ensure your email is valid (it must contain @ and .)")
            email = input("Enter your email: \n")
    return email

# checks the username for length >= 5 and no spaces
def check_username(username):
    temp_username = ""

    while True:
        if len(username) < 5:
            print("Username must be at least 5 characters")
            temp_username = input("Enter your username: \n")
            username = temp_username
        else:
            break

    while True:
        for ch in username:
            if ch == " ":
                print("Username cannot contain spaces")
                temp_username = input("Enter your username: \n")
                username = temp_username
        else:
            break
    return username

# master password must contain at least 8 characters, 1 uppercase, 1 lowercase, 2 numbers and 1 special character
def check_master_password(master_password):
    # set the initial parameters
    special_ch = "!@#$%^&*()_,+=<>/?:;"
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    numbers = string.digits
    x, y, z, a = 0, 0, 0, 0

    # check through the different types of required characters and sum the totals of each
    for ch in master_password:
        if ch in lower_case:
            x += 1
        elif ch in upper_case:
            y += 1
        elif ch in numbers:
            z += 1
        elif ch in special_ch:
            a += 1

    # test to see if password is strong enough
    if x >= 1 and y >= 1 and z >= 2 and a >= 1:
        print("good password password")
        return True
    return False


