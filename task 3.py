import json

class ContactManager:
    def __init__(self):
        self.contacts = {}  # Dictionary to store contacts
        self.load_contacts()  # Load contacts from file on initialization
    
    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = {}
    
    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.contacts, file, indent=4)
    
    def add_contact(self, name, phone_number, email):
        if name in self.contacts:
            print(f"{name} is already in contacts. Update the existing contact.")
        else:
            self.contacts[name] = {
                'phone_number': phone_number,
                'email': email
            }
            self.save_contacts()
            print(f"Added {name} with phone number {phone_number} and email {email} to contacts.")
    
    def update_contact(self, name, new_phone_number, new_email):
        if name in self.contacts:
            self.contacts[name]['phone_number'] = new_phone_number
            self.contacts[name]['email'] = new_email
            self.save_contacts()
            print(f"Updated phone number and email for {name}.")
        else:
            print(f"{name} is not found in contacts. Add this contact instead.")
            self.add_contact(name, new_phone_number, new_email)
    
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Deleted {name} from contacts.")
        else:
            print(f"{name} is not found in contacts. Cannot delete.")
    
    def search_contact(self, name):
        if name in self.contacts:
            contact_info = self.contacts[name]
            print(f"Name: {name}, Phone Number: {contact_info['phone_number']}, Email: {contact_info['email']}")
        else:
            print(f"{name} is not found in contacts.")
    
    def display_contacts(self):
        if not self.contacts:
            print("No contacts to display.")
        else:
            print("List of Contacts:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone Number: {info['phone_number']}, Email: {info['email']}")
        print()  # Empty line for better readability

def main():
    contact_manager = ContactManager()
    
    while True:
        print("Welcome to the Contact Management System!")
        print("1. Add a Contact")
        print("2. Update a Contact")
        print("3. Delete a Contact")
        print("4. Search for a Contact")
        print("5. Display All Contacts")
        print("6. Exit\n")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            name = input("Enter the name of the contact: ").strip()
            phone_number = input("Enter the phone number: ").strip()
            email = input("Enter the email address: ").strip()
            contact_manager.add_contact(name, phone_number, email)
        
        elif choice == '2':
            name = input("Enter the name of the contact to update: ").strip()
            new_phone_number = input("Enter the new phone number: ").strip()
            new_email = input("Enter the new email address: ").strip()
            contact_manager.update_contact(name, new_phone_number, new_email)
        
        elif choice == '3':
            name = input("Enter the name of the contact to delete: ").strip()
            contact_manager.delete_contact(name)
        
        elif choice == '4':
            name = input("Enter the name of the contact to search: ").strip()
            contact_manager.search_contact(name)
        
        elif choice == '5':
            contact_manager.display_contacts()
        
        elif choice == '6':
            print("Saving contacts and exiting the Contact Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 6.\n")

if __name__ == "__main__":
    main()
