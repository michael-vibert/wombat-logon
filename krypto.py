import bcrypt


# returns the hash version of the argument
def hash_password(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password_bytes, salt)
    return hashed_pw


def check_hash(pwd_to_test, password):
    pwd_bytes = bytes(pwd_to_test, 'utf-8')
    return bcrypt.checkpw(pwd_bytes, password.encode())
