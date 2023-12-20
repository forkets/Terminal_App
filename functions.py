import csv

def add_contact(file_name):
    print("Add contact")
    # ask the title of the contact
    contact_name = input("Enter a name: ")
    contact_number = int(input("Enter a phone number: "))
    # open file - list.csv
    with open(file_name, "a") as f:
        # insert values - title = user entered
                    # - completed = False
        writer = csv.writer(f)
        writer.writerow([contact_name, contact_number])
        # writer.writerow([contact_number, "False"])

def remove_contact(file_name):
    print("Remove contact")
    contact_name = input("Enter contact name that you want to remove: ")
    # contact_number = int(input("Enter contact number you want to remove: "))
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

def view_contacts(file_name):
    print("View contacts")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)