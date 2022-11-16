# a class for creating new users of the program


class NewUser:
    def __init__(self):
        pass
    
    def collect_credentials():
        email = input("Enter your email: \n")
        print(check_email(email))
        # username = input("Enter your username: \n")
        # check_username(username)
        # master_password = input("Enter your master password: \n")
        # check_master_password(master_password)

def check_email(email):
    at = False
    period = False

    for ch in email:
        if ch == '@':
            print('yep')
            at = True
        if ch == '.':
            print('yep2')
            period = True

    if (at == True and period == True):
        return True
    else:
      return False