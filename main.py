import persistence
import user
from user import User
from newUser import collect_credentials
from login import login
from create_login import create_entry

def main_menu(this_user):
    while True:
        selection = int(input(f"{this_user['username']}, Please enter the number for what you would like to do: \n"
                              "\t1:   Save new logon credentials! \n"
                              "\t2:   Create a super random password \n"
                              "\t3:   Close Wombat Logon & log out \n"))

        match selection:
            case 1:
                pass
            case 2:
                print("you selected two")
                # pass
            case 3:
                print("you selected three")


def start_menu():
    while True:
        selection = int(input("Hello and welcome to Wombat Logon, your personal password manager! \n"
                              "Please select the number for what you want to do: \n"
                              "\t1:   Create a new account \n"
                              "\t2:   Log in to saved Wombat account \n"
                              "\t3:   Close Wombat Logon & exit the program \n"
                              ">>> "))

        match selection:
            case 1:
                collect_credentials()

            case 2:
                this_user = login()      # login returns a user of type dict
                print(f"Woo Hoo! {this_user['username']}, Let's get Wombatting!\n"
                      f"-------------------------------------------------------------")
                return this_user
            case 3:
                print("you selected three")


# This is the method that gets called when the program is started
# We will run the whole program from here
def main():
    # this_user = start_menu()
    # main_menu(this_user)
    this_user = user.runtime_user_dict['katie']
    print(type(this_user))
    create_entry(this_user)
# calls the main function
if __name__ == "__main__":
    main()




