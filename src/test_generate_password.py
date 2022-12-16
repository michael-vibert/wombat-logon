from generate_password import random_pwd
import pytest

# Test to check that random password function returns the specified length password
def test_length_pwd():
    password = random_pwd(10)
    assert len(password) == 10
    