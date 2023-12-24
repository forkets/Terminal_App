from functions import add_contact, view_contacts, remove_contact, edit_contact
from colored import Fore, Back, Style

file_name = "list.csv"

try:
    # open the file in read mode
    contact_file = open(file_name, "r")
    contact_file.close()
    print("File Found")
    # if it throws error, it means the file doesn't exist, goes to except block
    # if no error, it means the file exists
except FileNotFoundError:
    # now, we know the file doesn't exist
    # create the file
    contact_file = open(file_name, "w")
    # we can also insert the first line into the file
    contact_file.write("First, Last, Number\n")
    contact_file.close()
    print("File Created")

print(f"{Fore.black}{Back.dark_gray}***Welcome!***{Style.reset}")
print(f"{Fore.black}{Back.light_gray}Contacts Book {Style.reset}")

# change these to relevant address book options
def create_menu():
    print("1. Enter 1 to add new contact")
    print("2. Enter 2 to remove contact")
    print("3. Enter 3 to view your contacts")
    print("4. Enter 4 to edit a contact")
    print("5. Enter 5 to exit")
    choice = input("Enter your selection: ")
    return choice

users_choice = ""

while users_choice != "5":
    users_choice = create_menu()
    if (users_choice == "1"):
        add_contact(file_name)
    elif (users_choice == "2"):
        remove_contact(file_name)
    elif (users_choice == "3"):
        view_contacts(file_name)
        input("Here are your contacts! Press Enter to return to menu.")
    elif (users_choice == "4"):
        edit_contact(file_name)
    elif (users_choice == "5"):
        print("Goodbye")
        continue
    else:
        print("Invalid Input")
    # print(users_choice)
    


# create file for functions for each option, import functions