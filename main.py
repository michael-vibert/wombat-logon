from user import User
from newUser import NewUser

# This is the method that gets called when the program is started
# We will run the whoel program from here
def main():
  mike = User("mike@hotmail.com", "mikie", "password")
  
  print(mike.__dict__)
  NewUser.collect_credentials()

  
if __name__ == "__main__":
    main()
