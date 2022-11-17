# A class defining user objects and performing user actions
import persistence

runtime_user_dict = {}


class User:
    no_of_users = 0     # keeps track of how many users and acts as a primary key for user table/dict

    def __init__(self, user_number, email, username, mast_password):
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

mike = User(0, 'mike.com', 'mikee', 'Password')
print(mike.user_number)
kate = User(0, 'kate.com', 'katie', 'Password')
print(kate.user_number)
User.save_user(mike)
User.save_user(kate)
print(runtime_user_dict)
print(runtime_user_dict['katie'])
h = runtime_user_dict['katie']
User.print_user_attributes(h)