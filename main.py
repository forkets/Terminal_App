file_name = "list.csv"

try:
    # open the file in read mode
    todo_file = open(file_name, "r")
    todo_file.close()
    print("In try block")
    # if it throws error, it means the file doesn't exist, goes to except block
    # if no error, it means the file exists
except FileNotFoundError:
    # now, we know the file doesn't exist
    # create the file
    todo_file = open(file_name, "w")
    # we can also insert the first line into the file
    todo_file.write("Name,Number\n")
    todo_file.close()
    print("In except block")

print("***Welcome!***")
print(" Address Book")

# change these to relevant address book options
def create_menu():
    print("1. Enter 1 to add new contact")
    print("2. Enter 2 to remove contact")
    print("3. Enter 3 to edit a contact")
    print("4. Enter 4 to view your contacts")
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
        edit_contact(file_name)
    elif (users_choice == "4"):
        view_contacts(file_name)
    elif (users_choice == "5"):
        print("Goodbye")
        continue
    else:
        print("Invalid Input")
    print(users_choice)
    
print("Thank you for choosing Address Book for all your contact needs!")

# create file for functions for each option, import functions