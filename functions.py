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

def view_contacts(file_name):
    print("View contacts")
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)