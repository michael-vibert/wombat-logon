import pytest
import krypto


example_password = "PassWord"

# test that the encryption changes the string
def test_encryption():    
    encrypted_pwd = krypto.encrypt_password(example_password.encode())
    assert example_password != encrypted_pwd
    
# Tests that decryption restores the origional string
def test_decryption():
    encrypted_pwd = krypto.encrypt_password(example_password.encode())
    decrypted_pwd = krypto.decrypt_password(encrypted_pwd)
    assert decrypted_pwd.decode() == example_password
    
    
# def 
    
