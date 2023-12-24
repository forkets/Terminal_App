import csv


def add_contact(file_name):
    print("Add contact")
    # ask the title of the contact
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    ph_number = int(input("Phone Number: "))
    # open file - list.csv
    with open(file_name, "a") as f:

        writer = csv.writer(f)
        writer.writerow([first_name, last_name, ph_number])


def remove_contact(file_name):
    print("Remove contact")
    contact_name = input("Enter first or last name of contact that you want to remove: ")
    # copy all the contents of the csv into a new csv
    # while doing this, we constantly check for the condition
    # when we encounter the contact to be removed, we don't copy that one
    # the final new contact will be written in the csv file
    contact_lists = []
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if (contact_name != row[0]): # is not the first row
                contact_lists.append(row)
    with open(file_name, "w") as f:
        writer = csv.writer(f)
        writer.writerows(contact_lists)
    print(contact_lists)
    print(f"Contact {contact_name} Removed")

def view_contacts(file_name):
    print("View contacts")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def edit_contact(file_name):
    print("Edit contact")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
    
    # Ask user for the field to edit
    field_to_edit = input("Enter the number corresponding to the field you want to edit: \n(1: First Name, 2: Last Name, 3: Email): ")
    if field_to_edit == "1":
        new_firstname = input("Enter the new first name: ")
        add_contact.first_name = new_firstname
        print("First name updated.")
        print(new_firstname)