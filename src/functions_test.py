from functions import Person, add_to_contact_list, read_contacts_from_file
from unittest.mock import patch

def test_contact_gets_added_to_list():
    mock_contacts = list()
    mock_contact = Person("John", "Doe", "0400111111")

    new_contacts = add_to_contact_list(mock_contact, mock_contacts)

    assert len(new_contacts) == 1
    assert new_contacts[0].first == "John"

@patch("functions.FILE_NAME", "mock_contacts.csv")
def test_read_file():
    contacts = read_contacts_from_file()
    assert len(contacts) == 1

