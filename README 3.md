#TASK 3
To implement a simple contact management system in Python, we'll create a program that allows users to add, view, edit, and delete contacts. We'll use dictionaries to represent each contact, and a list to store all contacts. We'll also use file handling to save and load contacts from a text file for persistent storage.

Here's a step-by-step implementation:

### Step-by-Step Implementation:

1. **Define Functions for Contact Management**:
   - **Add Contact**: Add a new contact by entering name, phone number, and email address.
   - **View Contacts**: Display all contacts in the list.
   - **Edit Contact**: Modify details (phone number and email) of an existing contact.
   - **Delete Contact**: Remove a contact from the list.

2. **Implement File Handling Functions**:
   - **Save Contacts**: Write the current list of contacts to a text file.
   - **Load Contacts**: Read contacts from the text file into the list.

3. **Main Program Loop**:
   - Use a loop to continuously prompt the user for actions (add, view, edit, delete, exit).

Here's the Python code for the contact management system:

```python
import os

# Global variable to store contacts
contacts = []

# File name for storing contacts
file_name = "contacts.txt"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_contact():
    print("\nAdd a New Contact")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    contact = {
        'name': name,
        'phone': phone,
        'email': email
    }
    contacts.append(contact)
    save_contacts()
    print(f"\nContact '{name}' added successfully!\n")

def view_contacts():
    clear_screen()
    print("Contact List\n")
    if contacts:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts found.")
    print()

def edit_contact():
    clear_screen()
    print("Edit Contact\n")
    view_contacts()
    if contacts:
        try:
            index = int(input("Enter the index of the contact to edit: ")) - 1
            if 0 <= index < len(contacts):
                contact = contacts[index]
                print(f"\nEditing Contact: {contact['name']}\n")
                new_phone = input(f"Enter new phone number (current: {contact['phone']}): ").strip()
                new_email = input(f"Enter new email address (current: {contact['email']}): ").strip()
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                save_contacts()
                print(f"\nContact '{contact['name']}' updated successfully!\n")
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")
    else:
        print("No contacts found.")
    print()

def delete_contact():
    clear_screen()
    print("Delete Contact\n")
    view_contacts()
    if contacts:
        try:
            index = int(input("Enter the index of the contact to delete: ")) - 1
            if 0 <= index < len(contacts):
                contact = contacts.pop(index)
                save_contacts()
                print(f"\nContact '{contact['name']}' deleted successfully!\n")
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")
    else:
        print("No contacts found.")
    print()

def save_contacts():
    with open(file_name, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")

def load_contacts():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                name, phone, email = line.strip().split(',')
                contact = {
                    'name': name,
                    'phone': phone,
                    'email': email
                }
                contacts.append(contact)
    else:
        print("No existing contacts file found.")

def main():
    load_contacts()
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        
        clear_screen()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
```

### Explanation:

- **Functions**:
  - `clear_screen()`: Clears the terminal screen (works for both Windows and Unix-like systems).
  - `add_contact()`, `view_contacts()`, `edit_contact()`, `delete_contact()`: Functions for adding, viewing, editing, and deleting contacts respectively.
  - `save_contacts()`, `load_contacts()`: Functions to save contacts to a text file (`contacts.txt`) and load contacts from it.

- **Main Program (`main()`)**:
  - Loads contacts from the file (`load_contacts()`).
  - Displays a menu of options (add, view, edit, delete, exit).
  - Based on user input, calls the appropriate function to perform the desired action.
  - Continues until the user chooses to exit (`choice == '5'`).

- **File Handling**:
  - Contacts are stored in a text file (`contacts.txt`) in the format `name,phone,email`.
  - When the program starts (`main()`), it loads existing contacts from this file into the `contacts` list using `load_contacts()`.

### Usage:

1. **Run the Program**:
   - Save the above code in a file (e.g., `contact_management.py`).
   - Open a terminal or command prompt and navigate to the directory containing the file.
   - Run the script using `python contact_management.py`.

2. **Interact with the Program**:
   - Follow the on-screen prompts to add, view, edit, and delete contacts.
   - Contacts are saved to `contacts.txt` automatically and loaded when the program starts.

3. **Persistence**:
   - Contacts are persisted between program runs using file handling.
