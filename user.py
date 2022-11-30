# A class defining user objects and performing user actions

import persistence


''' initialise the saved users from (./user_data.json) file,
    be sure to put a pair of empty curly braces in the json file if
    the file is initially empty '''
runtime_user_dict = persistence.re_in_state('user_data.json')

""" Class for new users of the application.
    When called and passed the correct arguments the class will 
    initialise a object of user and save the user details to file. """
class User:
    def __init__(self, email, username, mast_password):
        self.email = email
        self.username = username
        self.mast_password = mast_password
        self.entries = {}
        self.save_user()

    def save_user(self):
        print(f'User Saved! Details:')
        self.print_user_attributes()
        runtime_user_dict[self.username] = self
        persistence.save_state(runtime_user_dict)

    def print_user_attributes(self):
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("entries: " + str(self.entries))



# mikee = User('mike.com', 'mikeeMan', 'AcroMan32')
# entry1 = Entry('blackfriday.com', 'mike@hot.com', 'AcroMan32!', None, runtime_user_dict['mikee'])




