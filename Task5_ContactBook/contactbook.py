contacts = {}

def separator():
    print("\n" + "-" * 40 + "\n")


def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10


def add_contact():
    separator()
    phone = input("Enter Phone Number: ")

    if not is_valid_phone(phone):
        print("Invalid phone number! Please enter a 10-digit number.")
        return

    if phone in contacts:
        print("Contact already exists!")
        return

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[phone] = {
        "name": name,
        "email": email,
        "address": address
    }

    print("\nContact added successfully!")


def view_contacts():
    separator()
    if not contacts:
        print("No contacts available.")
        return

    print("Contact List:")
    print("-" * 40)
    for phone, details in contacts.items():
        print(f"Name: {details['name']} | Phone: {phone}")


def search_contact():
    separator()
    search = input("Enter name or phone number to search: ")

    found = False
    for phone, details in contacts.items():
        if search == phone or search.lower() in details["name"].lower():
            print("\nContact Found:")
            print("-" * 40)
            print(f"Name   : {details['name']}")
            print(f"Phone  : {phone}")
            print(f"Email  : {details['email']}")
            print(f"Address: {details['address']}")
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    separator()
    old_phone = input("Enter phone number to update: ")

    if old_phone not in contacts:
        print("Contact not found.")
        return

    print("Leave blank to keep existing value.")

    new_name = input("Enter New Name: ")
    new_phone = input("Enter New Phone Number: ")
    new_email = input("Enter New Email: ")
    new_address = input("Enter New Address: ")

    contact = contacts[old_phone]

    if new_name:
        contact["name"] = new_name
    if new_email:
        contact["email"] = new_email
    if new_address:
        contact["address"] = new_address

    if new_phone:
        if not is_valid_phone(new_phone):
            print("Invalid phone number! Must be 10 digits.")
            return
        if new_phone in contacts:
            print("Another contact already exists with this phone number.")
            return

        contacts[new_phone] = contact
        del contacts[old_phone]
        phone_to_show = new_phone
    else:
        phone_to_show = old_phone

    print("\nContact updated successfully!")
    print("-" * 40)
    print(f"Name   : {contacts[phone_to_show]['name']}")
    print(f"Phone  : {phone_to_show}")
    print(f"Email  : {contacts[phone_to_show]['email']}")
    print(f"Address: {contacts[phone_to_show]['address']}")


def delete_contact():
    separator()
    phone = input("Enter phone number to delete: ")

    if phone not in contacts:
        print("Contact not found.")
        return

    confirm = input("Are you sure you want to delete this contact? (y/n): ").lower()

    if confirm == "y":
        del contacts[phone]
        print("\nContact deleted successfully!")
    else:
        print("\nDelete operation cancelled.")


def menu():
    while True:
        separator()
        print("--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            separator()
            print("Thanks for using the Contact Book..!! 😊")
            break
        else:
            print("Invalid choice. Please try again.")


menu()
