from generate_password import random_pwd
import pytest


def test_length_pwd():
    password = random_pwd(10)
    assert len(password) == 10
    
# test_length_pwd()