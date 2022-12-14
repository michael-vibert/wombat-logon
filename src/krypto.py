import bcrypt
from cryptography.fernet import Fernet


"""
Param -> string to be salted and hashed
Returns -> Hash of the password string
"""
def hash_password(password):
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password_bytes, salt)
    return hashed_pw

"""
Simple function to check if entered password matches saved hash
Params -> Plain text string of the password to check and the hash of the 
password that has been entered earlier
"""
def check_hash(pwd_to_test, password_hash):
    pwd_bytes = bytes(pwd_to_test, 'utf-8')
    return bcrypt.checkpw(pwd_bytes, password_hash.encode())


"""
A function to create a random secret key that will be used to encrypt and decrypt our data.
Function also saves the key to 'secret-key.key
This only needs to be used once to generate the key **BE CAREFUL with THIS KEY
If you run this function again it will over-ride the old stored key in the secret-key.key file
This will mean that you lose the key forever, which is the key that decrypts all your saved passwords!
In other words - my advice is to make a copy of your secret key and keep it safe!
'"""
def gen_secret_key():
    try:
        key = Fernet.generate_key()
        with open('secret-key.key', 'wb') as keys_to_kingdom:
            keys_to_kingdom.write(key)
    except FileNotFoundError as e:
        print(f"No no with secret key found. The error came back as: {e}")


def load_key():
    # open secret key, read it and save to variable
    try:    
        with open('secret-key.key', 'rb') as key_on_file:
            key_data = key_on_file.read()

            return key_data
    except FileNotFoundError as e:
        print("File to load key from was not found, please check your settings and try again")
        print(f"Error Type encourntered: {e}")
        quit()       


def encrypt_password(data):
    f = Fernet(load_key())
    return f.encrypt(bytes(data))


def decrypt_password(data):
    f = Fernet(load_key())
    return f.decrypt(bytes(data))


"""
Encrypt a file. Params the key you want to use and the file you want to encrypt 
Returns None but saves the encrypted data to file
"""
def encrypt_data(key, file):
    # get the key ready to use as a Fernet key
    f = Fernet(key)

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

    with open('decrypted_data.json', 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
