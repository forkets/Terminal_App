# Contact Book Application

## Features
- Add contacts - Allows users to add a new contact quickly and easily. There is a prompt for first name, last name, and contact number.
- Remove contacts - Allows users to remove any unwanted contacts. Simply enter a name (first or last) for the desired contact to remove and it will remove the whole contact.
- View contacts - Allows users to view the entire contact list. 
- Edit contacts?? - If I can get it working, this will allow users to modify a contact in their list. This would include changing either first or last name, or the contact number.

## Implementation Plan
- Create menu
    - This will be created using a function. Include options for:<br>
        - [x] adding contacts<br>
        - [x] removing contacts<br>
        - [x] viewing contacts<br>
        - [ ] editing contacts<br>
        - [x] exit prompt
- Create file
    - [x] Define file name
    - [x] Use try/except blocks to check if the file exists yet and create one if it doesn't.
- Build Add Contacts feature
    - This will use a function called add_contacts. Include options for:
        - [x] Adding first name
        - [x] Adding last name
        - [x] Adding phone number
        - [x] Inform user that the information has been stored
- Build Remove Contacts feature
    - This will use a function called remove_contacts.
        - [x] Prompt user for a contact name to remove
        - [x] Code will find the contact and remove it
        - [x] Print amended contact list
        - [x] Inform user the contact has been removed
- Build View Contacts feature
    - This will use a function called view_contacts.
        - [x] Display entire contact list
        - [x] Prompt user to press Enter to return to menu. This avoids the menu being displayed immediately after the contact list, making it easier to read. 
- Build Edit Contacts feature
    - This will use a function called edit_contacts.
        - [ ] Prompt user for a contact to edit
        - [ ] Display contact
        - [ ] Prompt user for specific data to edit (first name, last name, or phone number)
        - [ ] Display updated contact
        - [ ] Inform user the contact has been updated

## How to use application
There are some requirements in order for this application to be used. This application can be used on any standard Windows or Mac computer<br>

Step 1: Install VS Code for your system (https://code.visualstudio.com/download)<br>
Step 2: Download code for application from github (https://github.com/forkets/Terminal_App)<br>
Step 3: Open source folder in VS Code<br>
Step 4: Check Python is installed<br>
- 4a: Open terminal and type ```python3 --version``` and hit enter. If Python is installed it will display the Python version you have. If your version is 3.10 or higher, proceed to Step 5.
- 4b: If Python is not installed or older than 3.10, follow this link for instructions how to install Python 3.12 (https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-12-on-ubuntu-20-04-and-22-04-lts/)<br>

Step 5: In the terminal, type ```./run.sh```. This will create a virtual environment and install any packages required for the application to work. It will also run the application for you.<br>
Step 6: Follow prompts given in the application
- 6a: There will be 5 options in the main menu of the application; add contact, remove contact, view contacts, edit contact, and exit.
- 6b: Enter the number that corrosponds with the option you want.
- 6c: Follow any new prompts provided.