from colorama import Fore, Style
from user import runtime_user_dict
from newUser import collect_credentials
from login import login
from create_entry import create_entry, find_entry
from generate_password import random_pwd


def main_menu(this_user):


    while True:
            selection = (input(f"{Fore.GREEN}{this_user['username']}{Style.RESET_ALL}, "
                                  f"{Fore.BLUE}Please enter the number for what you would like to do:{Style.RESET_ALL}\n"
                                  f"\t{Fore.LIGHTBLUE_EX}1:{Style.RESET_ALL}   Save new logon credentials! \n"
                                  f"\t{Fore.LIGHTBLUE_EX}2:{Style.RESET_ALL}   Create a super random password \n"
                                  f"\t{Fore.LIGHTBLUE_EX}3:{Style.RESET_ALL}   Look up saved passwords \n"
                                  f"\t{Fore.LIGHTBLUE_EX}4:{Style.RESET_ALL}   Close Wombat Logon & log out \n"
                                  f"{Fore.BLUE}>>>{Style.RESET_ALL}"))
            try:
                match int(selection):
                    case 1:
                        create_entry(this_user['username'])
                    case 2:
                        print(f"Here is your random password \n"
                            f"{Fore.LIGHTRED_EX}{random_pwd(10)}{Style.RESET_ALL}\n"
                            f"Use it wisely!\n"
                            f"<----------------------------------->\n")
                    case 3:
                        find_entry(this_user['username'])
                    case 4:
                        print(f"Thanks for using Wombat Logon, see you next time =)\n"
                            f"{Fore.YELLOW}Have a nice day!{Style.RESET_ALL}\n")
                        quit(1)
                    case _:
                        print(f"Invalid input: {selection}. Please only input numbers 1, 2 or 3!\n")
                        continue
                               
            except (TypeError, ValueError) as error:
                print(f"Invalid input, we've detected a {Fore.LIGHTYELLOW_EX}{error.__class__} for input: {selection}{Style.RESET_ALL} please only input 1, 2 or 3!\n")


def start_menu():
    while True:
        selection = (input(f"\nWelcome to {Fore.LIGHTBLUE_EX}Wombat Logon{Style.RESET_ALL}, your personal password manager! \n"
                              f"Please {Fore.LIGHTBLUE_EX}select{Style.RESET_ALL} the number for what you want to do: \n"
                              f"\t{Fore.LIGHTBLUE_EX}1:{Style.RESET_ALL}   Create a new account \n"
                              f"\t{Fore.LIGHTBLUE_EX}2:{Style.RESET_ALL}   Log in to saved Wombat account \n"
                              f"\t{Fore.LIGHTBLUE_EX}3:{Style.RESET_ALL}   Close Wombat Logon & exit the program \n"))
        try:    
            match int(selection):
                case 1:
                    main_menu(collect_credentials())
                case 2:
                    this_user = login()      # login returns a user of type dict
                    print(f"Woo Hoo! {Fore.GREEN}{this_user['username']}{Style.RESET_ALL}, Let's get Wombatting!\n"
                        f"-------------------------------------------------------------")
                    main_menu(this_user)
                    # main_menu(extract_user(this_user['username']))
                case 3:
                    print(f"Thanks for using Wombat Logon, see you next time =)\n"
                        f"{Fore.YELLOW}Have a nice day!{Style.RESET_ALL}")
                    quit(1)
                case _:
                    print(f"Invalid input: {selection}. Please only input numbers 1, 2 or 3!\n")
                    continue
        except (TypeError, ValueError) as error:
            print(f"Invalid input, we've detected a {Fore.LIGHTYELLOW_EX}{error.__class__.__name__}{Style.RESET_ALL} please only input 1, 2 or 3!\n")


# This is the method that gets called when the program is started
# We will run the whole program from here
def main():
    start_menu()

# calls the main function
if __name__ == "__main__":
    main()




