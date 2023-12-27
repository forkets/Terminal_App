from constants import COLOR
from functions import Person, find_contact_in_list, read_contacts_from_file, remove_contact_from_list, update_contact_in_list, user_action_add_contact, COLOR
from colored import Style

# if file already exists
try:
    # open the file in read mode
    contact_file = open("contacts.csv", "r")
    contact_file.close()
    print("File found")

# if file does not already exist
except FileNotFoundError:
    # create the file
    contact_file = open("contacts.csv", "w")
    contact_file.close()

users_input = ""

contacts = read_contacts_from_file()

print(f"{COLOR}*Welcome to the address book*{Style.reset}")

while users_input != "q":
    print("1. Enter 1 to add new contact")
    print("2. Enter 2 to view contacts")
    print("3. Enter 3 to find contact")
    print("4. Enter 4 to edit a contact")
    print("5. Enter 5 to remove a contact")
    print("q. Enter q to quit")
    users_input = input(f"{COLOR}Please enter your selection:{Style.reset} ")

    if users_input == "1":
        user_action_add_contact(contacts)

    elif users_input == "2":
        for contact in contacts:
            print(contact)
        input(f"{COLOR}Here are your contacts! Press Enter to return to menu.{Style.reset}")
    
    elif users_input == "3":
        find_contact_in_list(contacts)

    elif users_input == "4":
        update_contact_in_list(contacts)

    elif users_input == "5":
        contacts = remove_contact_from_list(contacts)
        
    elif users_input.lower() == "q":
        break


print(f"{COLOR}Bye!{Style.reset}")