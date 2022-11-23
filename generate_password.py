
import os
import random
import string
import secrets

"""
Returns a strong password that is almost cryptographically secure. 
Note - I wouldn't generate passwords in a large organisational 
environment but will be perfect for individual use
"""
def random_password():
    length = 10
    pwd = list(secrets.token_urlsafe(length))

    # loop over the pwd created above and for ~1/3 swap it with a random
    # choice from the punctuation set.
    i = 0
    while i < length:
        random.seed(os.urandom(1024))
        x = random.randint(0, 2)
        if x == 1:
            y = random.choice(string.punctuation)
            pwd[i] = y
            i += 1
        else:
            i += 1
            continue
    # convert the pwd which is a list into a string for returning
    stringify = ("".join(pwd))

    return stringify


print(random_password())