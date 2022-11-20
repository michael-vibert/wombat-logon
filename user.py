# A class defining user objects and performing user actions
import persistence
import krypto
from newUser import collect_credentials

# initialise the saved users from (./user_data.json) file

runtime_user_dict = persistence.re_in_state('user_data.json')


class User:
    no_of_users = 0  # keeps track of how many users and acts as a primary key for user table/dict

    def __init__(self, email, username, mast_password):
        self.email = email
        self.username = username
        self.mast_password = mast_password
        User.no_of_users += 1
        self.user_number = User.no_of_users

    def save_user(self):
        runtime_user_dict[self.username] = self
        persistence.save_state(runtime_user_dict)

    def user_logon(self):
        pass
    # login()

    def verify_logon(self):
        pass

    def print_user_attributes(self):
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("User Number: " + str(self.user_number))

    def find_user(self):
        password = self.mast_password


# for user in runtime_user_dict:
#     print(runtime_user_dict[user])
#     user = runtime_user_dict[user]
#     User.print_user_attributes(user)
#     print(type(user['username']))


# collect_credentials()

# mike = User('mike.com', 'mikee', 'Password')
# print(mike.user_number)
# kate = User('kate.com', 'katie', 'Password')
# print(kate.user_number)
# User.save_user(mike)
# User.save_user(kate)
# print(runtime_user_dict)
# print(runtime_user_dict['katie'])
# h = runtime_user_dict['katie']
# User.print_user_attributes(h)