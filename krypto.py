import base64

import bcrypt
from cryptography.fernet import Fernet


# returns the hash version of the argument
def hash_password(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password_bytes, salt)
    return hashed_pw


def check_hash(pwd_to_test, password):
    pwd_bytes = bytes(pwd_to_test, 'utf-8')
    return bcrypt.checkpw(pwd_bytes, password.encode())


"""
A function to create a random secret key that will be used to encrypt and decrypt our data.
Function also saves the key to 'secret-key.key
'"""
def gen_secret_key():
    key = Fernet.generate_key()
    with open('secret-key.key', 'wb') as keys_to_kingdom:
        keys_to_kingdom.write(key)


def load_key():
    # open secret key, read it and save to variable
    with open('secret-key.key', 'rb') as key_on_file:
        key_data = key_on_file.read()

        return key_data


"""
Encrypt a file. Params the key you want to use and the file you want to encrypt 
Returns None but saves the encrypted data to file
"""
def encrypt_data(key, file):
    # get the key ready to use as a Fernet key
    f = Fernet(key)
    # print(f)
    # open up the file and read it into byte data
    with open(file, 'rb') as unencrypted_file:
        original_data = unencrypted_file.read()

    # encrypt the original byte data
    encrypted_data = f.encrypt(original_data)

    # write the encrypted data to file
    with open(file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

"""
Function to decrypt your file. Pass the params - file you want to decrypt and the key 
you want to use, function writes decrypted data to file 
"""
def decrypt_data(key, file):
    f = Fernet(key)
    with open(file, 'rb') as encrypted_file:
        data_encrypted = encrypted_file.read()

    decrypted_data = f.decrypt(data_encrypted)

    with open('./decrypted_data.json', 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)


# gen_secret_key()
# key = load_key()
# encrypt_data(key, "./test2.json")
# decrypt_data(key, "./test2.json")
