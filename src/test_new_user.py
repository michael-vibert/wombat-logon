import pytest
import mock
import builtins
from new_user import check_email, check_username

# Test that check email function returns the email only if it satisfies the requirements
# of at least 1 '@' and 1 '.' charatcters.
def test_check_email():
    with mock.patch.object(builtins, 'input', lambda _: 'mike@hotmail.com'):
        assert check_email() == 'mike@hotmail.com'

  
def test_check_username():    
    with mock.patch.object(builtins, 'input', lambda _: 'LittleManMickie'):
        assert check_username() == 'LittleManMickie'

# In this I aim to check that spaces in the username make the function call the user to try again
    with mock.patch.object(builtins, 'input', lambda _: 'Little ManMickie'):
        with mock.patch.object(builtins, 'input', lambda _: 'Little     ManMickie'):
            with mock.patch.object(builtins, 'input', lambda _: 'LittleManMickie'):
                assert check_username() == 'LittleManMickie' # seems to work :)
                
