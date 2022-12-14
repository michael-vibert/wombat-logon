import random
import string
import secrets

"""
Returns a strong pseudo-random password that is secure enough for small scale use. 
Note - I wouldn't generate passwords in a large organisational 
environment but will be perfect for individual use
"""
def random_pwd(length=10):  # I made a default here for future functionality where
                            # the user can choose the strength of the password
    i = 0
    pwd = ""
    while i in range(length):
        # grab a random number between 0 and 3 - randint uses os.urandom to generate a
        # random number based on the os time
        number_random = random.randint(0, 3)

        match number_random:
            case 0:
                pwd += secrets.choice(string.ascii_lowercase)
            case 1:
                pwd += secrets.choice(string.digits)
            case 2:
                pwd += secrets.choice(string.punctuation)
            case 3:
                pwd += secrets.choice(string.ascii_uppercase)
        i += 1

    return pwd


