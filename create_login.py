import validators


def create_entry(this_user):
    # enter the url
    while True:
        url = input("Enter the website URL (eg. 'mikesBlog.com.au'\n")
        if validators.validate_url(url):
            print("\t---->> Nice one\n")
            break
        else:
            continue

    # Enter the email
    while True:
        print("Enter the Email you want to use with this site:\n")
        entry_email = input("\tto use the same email you use for Wombat Login type 'y'\n")
        if entry_email is 'y':
            entry_email = this_user
        elif validators.check_email(entry_email):
            break
        else:
            continue

    # Enter the username if you want one included
    while True:
        include_username = input("Do you want to include a username with this record? 'y/n'\n")
        if include_username is 'y':
            username = input("Enter your username:\n")
        elif include_username is 'n':
            break
        else:
            continue

    # Generate a password or enter your own?
    while True:
        print("Would you like to generate a strong password or enter your own?\n")
        generate = input("\tType 'g' for generate or type 'e' for enter your own \n")
        if generate is 'g' or 'G':
            password = input("Please enter your desired password:\n")
        elif generate is 'e' or 'E':
            pass
        else:
            print("Only the character g or e are accepted input, try again")
            continue

        new_entry = Entry(url, entry_email, password, username)


class Entry:
    def __init__(self, url, entry_email, password, username=None):
        self.url = url
        self.entry_email = entry_email
        self.password = password
        self.username = username
        print("Entry created:!")

    # create tuple of the entry deets.
    # print()

# create_entry()
