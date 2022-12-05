# A class defining user objects and performing user actions

import persistence 

''' initialise the saved users from (./user_data.json) file,
    be sure to put a pair of empty curly braces in the json file if
    the file is initially empty '''
runtime_user_dict = persistence.re_in_state('./user_data.json')

""" Class for new users of the application.
    When called and passed the correct arguments the class will 
    initialise a object of user and save the user details to file. """
class User:
    def __init__(self, email, username, mast_password):
        self.email = email
        self.username = username
        self.mast_password = mast_password
        self.entries = {}
        dt = self.user_to_dictionary()
        self.save_user(dt)

    # I changed the data type straight into a dictionary to avoid storage difficulties later
    # after you re-in-state the user data
    def user_to_dictionary(self):
        return {'email': self.email, 'username': self.username, 'mast_password': self.mast_password, 'entries': self.entries}
    # Save the new user data straight into runtime_user_dict where it will be saved into file later.
    # This helps with the problem of users being objects during this session then dictionaries on the next session
    def save_user(self, dt):
        print('User Saved! Details:')
        self.print_user_attributes()
        runtime_user_dict[self.username] = dt
        persistence.save_state(runtime_user_dict)

    def print_user_attributes(self):
        print("Username: " + self.username)
        print("Email: " + self.email)
        print("entries: " + str(self.entries))



# mikee = User('mike.com', 'mikeeMan', 'AcroMan32')
# entry1 = Entry('blackfriday.com', 'mike@hot.com', 'AcroMan32!', None, runtime_user_dict['mikee'])




