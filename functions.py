import csv
from colored import Style

from constants import COLOR, FILE_NAME

class Person:
    def __init__(self, first: str, last: str, ph_number: int):
        self.first = first
        self.last = last
        self.ph_number = ph_number

    def full_name(self):
        return f"{self.first} {self.last}"

    def __str__(self) -> str:
        print("----------\n")
        return f"{self.first} {self.last} : {self.ph_number}\n"

def user_action_add_contact(contacts: list[Person]):
    print(f"{COLOR}Please enter contact information{Style.reset}")

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    ph_number = int(input("Phone Number: "))

    our_contact = Person(first_name, last_name, ph_number)
    contacts = add_to_contact_list(our_contact, contacts)
    save_contacts(contacts)

    print(f"{COLOR}Thanks! Information stored!{Style.reset}")

def view_contacts(contacts: list[Person]):
    to_view = input(f"{COLOR}Enter contact's full name to view:\n{Style.reset}")
    for contact in contacts:
            if to_view in contact.full_name():
                print(contact)

def save_contacts(contacts: list[Person]):
    with open(FILE_NAME, "w") as f:
        writer = csv.writer(f)

        for c in contacts:
            writer.writerow([c.first, c.last, c.ph_number])

# read all contacts from a file into in-memory list
def read_contacts_from_file() -> list[Person]:
    contacts = list()
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            contacts.append(Person(row[0], row[1], row[2]))
    return contacts

# add to in-memory list of contacts
def add_to_contact_list(contact: Person, contacts: list[Person]) -> list[Person]:
    contacts.append(contact)
    return contacts

# list the contents of in-memory list
def display_contact_list(contacts):
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
    return contacts

# search the list for a specific contact
def find_contact_in_list(contacts: list[Person], prompt: str = "Enter contact's full name to view") -> Person:
    contact_name = input(prompt + ": \n")
    matched_contact = None
    for contact in contacts:   
        if contact_name == contact.full_name():
            matched_contact = contact
            break

    if matched_contact is None:
        print("Contact not found")
    else:
        print(matched_contact)
    return matched_contact

# edit existing contact
def update_contact_in_list(contacts: list[Person]) -> Person:
    # find contact
    matched_contact = find_contact_in_list(contacts, "Enter contact's full name to update")
    # collect information from user
    print(f"{COLOR}Please enter contact information{Style.reset}")

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    ph_number = int(input("Phone Number: "))

    # replace existing info with new info
    matched_contact.first = first_name
    matched_contact.last = last_name
    matched_contact.ph_number = ph_number

    save_contacts(contacts)
    return matched_contact

def remove_contact_from_list(contacts: list[Person]) -> list[Person]:
    # find contact
    matched_contact = find_contact_in_list(contacts, "Enter contact's full name to remove")
    # start a new list
    new_contact_list = []

    # loop over existing list
    for contact in contacts:
        # check if matched_contact is this_contact
        if matched_contact == contact:
            # if so, skip
            continue
            # if not, add to new list
        else:
            new_contact_list.append(contact)

    save_contacts(new_contact_list)
    return new_contact_list