contacts = [
    {"name": "John Doe", "phone": "1234567890", "email": "johndoe@example.com"}
]
def display_menu():
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Save Contacts")
    print("7. Load Contacts")
    print("8. Exit")
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
def search_contact(contacts):
    search_term = input("Enter name or phone to search: ")
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            return contact
    print("No contact found.")
    return None
def edit_contact(contacts):
    contact = search_contact(contacts)
    if contact:
        contact['name'] = input(f"Enter new name (current: {contact['name']}): ") or contact['name']
        contact['phone'] = input(f"Enter new phone (current: {contact['phone']}): ") or contact['phone']
        contact['email'] = input(f"Enter new email (current: {contact['email']}): ") or contact['email']
        print("Contact updated successfully!")
def delete_contact(contacts):
    contact = search_contact(contacts)
    if contact:
        contacts.remove(contact)
        print("Contact deleted successfully!")
import json
def save_contacts(contacts, filename="contacts.json"):
    with open(filename, "w") as file:
        json.dump(contacts, file)
    print("Contacts saved successfully!")
def load_contacts(filename="contacts.json"):
    import os
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    print("No saved contacts found.")
    return []
def main():
    contacts = load_contacts()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            edit_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
        elif choice == "7":
            contacts = load_contacts()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
