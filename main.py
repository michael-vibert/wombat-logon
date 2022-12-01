
from user import runtime_user_dict
from newUser import collect_credentials
from login import login
from create_entry import create_entry, find_entry
from generate_password import random_pwd


def main_menu(this_user):


    while True:
            selection = int(input(f"{this_user['username']}, "
                                  f"Please enter the number for what you would like to do: \n"
                                  "\t1:   Save new logon credentials! \n"
                                  "\t2:   Create a super random password \n"
                                  "\t3:   Look up saved passwords \n"
                                  "\t4:   Close Wombat Logon & log out \n"))

            match selection:
                case 1:
                    create_entry(this_user['username'])
                case 2:
                    print(f"Here is your random password \n"
                          f"{random_pwd(10)}\n"
                          f"Use it wisely!\n"
                          f"<----------------------------------->\n")
                case 3:
                    find_entry(this_user['username'])
                case 4:
                    print("Thanks for using Wombat Logon, see you next time =)")
                    quit(1)
                case 5:
                    print(runtime_user_dict)


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
                main_menu(collect_credentials())
            case 2:
                this_user = login()      # login returns a user of type dict
                print(f"Woo Hoo! {this_user['username']}, Let's get Wombatting!\n"
                      f"-------------------------------------------------------------")
                main_menu(this_user)
                # main_menu(extract_user(this_user['username']))
            case 3:
                print("Thanks for using Wombat Logon, see you next time =)")
                quit(1)


# This is the method that gets called when the program is started
# We will run the whole program from here
def main():
    print(f"create main: {runtime_user_dict}")

    start_menu()

# calls the main function
if __name__ == "__main__":
    main()




