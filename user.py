# A class defining user objects and performing user actions
import entry
import persistence
from create_entry import create_entry
# initialise the saved users from (./user_data.json) file

# global runtime_user_dict


# def initialise_runtime_data():

runtime_user_dict = persistence.re_in_state('user_data.json')
if runtime_user_dict is None:
    runtime_user_dict = {}

# except TypeError or FileNotFoundError:
#     print("We detected a No User data found error.. Initialising a new data structure.\n")
#     runtime_user_dict = {}


class User:
    no_of_users = 0  # keeps track of how many users and acts as a primary key for user table/dict

    def __init__(self, email, username, mast_password):
        self.email = email
        self.username = username
        self.mast_password = mast_password
        User.no_of_users += 1
        self.user_number = User.no_of_users
        self.entries = {}

    def save_user(self):
        print(runtime_user_dict)
        print(self.print_user_attributes())
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
        print("entries: " + str(self.entries))


def save_entry(user, entry):
    entry_to_save = {
                     'email': entry.entry_email,
                     'password': entry.password,
                     'username': entry.username
    }
    runtime_user_dict[user.username]['entries'][entry.url] = entry_to_save
    print(runtime_user_dict)
    persistence.save_state(runtime_user_dict)
    # user.save_user()

# # katie = User('katie.com', 'katie', 'passcode')
# # katie.save_user()
# mikee = User('mike.com', 'mikeeMan', 'AcroMan32')
# mikee.save_user()
#
#
# name = runtime_user_dict['katie']
# entry1 = entry.Entry('katie3.com.au', 'katie@hotty.com', 'blanker', '')
# save_entry(name, entry1)
# entry2 = entry.Entry('cooking.com.au', 'katie@hotty.com', 'Usemade', '')
# save_entry(name, entry2)




