import csv
from colored import Style

from constants import COLOR, FILE_NAME

class Person:
    def __init__(self, first, last, ph_number):
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
    to_view = input(f"{COLOR}Enter contact name to view:\n{Style.reset}")
    for contact in contacts:
            if to_view in contact.full_name():
                print(contact)

def save_contacts(contacts: list[Person]):
    with open(FILE_NAME, "w") as f:
        writer = csv.writer(f)

        for c in contacts:
            writer.writerow([c.first, c.last, c.ph_number])

# read all contacts from a file into in-memory list
def read_contacts_from_file():
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

def display_contact_list(contacts):
    with open(FILE_NAME, "r") as f:
        reader = csv.reader(f)
    return contacts