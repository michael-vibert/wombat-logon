
class Entry:
    def __init__(self, url, entry_email, password, username):
        self.url = url
        self.entry_email = entry_email
        self.password = password
        self.username = username if username is not None else ""

        print(f"New entry created! {self.__dict__}")


# google = Entry("google.com", "mike@.com", "Password", "mikeee")
