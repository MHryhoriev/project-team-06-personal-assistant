from managers import ContactManager
from models import Contact
from utils.custom_decorators import error_handler

@error_handler
def handle_add_contact(manager: ContactManager) -> None:
    try:
        name = input("Enter name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        address = input("Enter address: ").strip()
        phone_number = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        birthday = input("Enter birthday (DD-MM-YYYY): ").strip()

        new_contact = Contact(name=name, address=address, phone_number=phone_number, email=email, birthday=birthday)
        manager.add_contact(new_contact)
    except Exception as ex:
        print(f"An error occurred while adding the contact: {ex}")

@error_handler
def handle_search_contact(manager: ContactManager) -> None:
    search_type = input("Search by (name/email/phone): ").strip().lower()
    query = input("Enter the search query: ").strip()

    search_map = {
        "name": manager.search_by_name,
        "email": manager.search_by_email,
        "phone": manager.search_by_phone_number
    }

    search_method = search_map.get(search_type, "")

    if search_method:
        try:
            results = search_method(query)
            if results:
                print(f"Found {len(results)} contact(s):")
                for contact in results:
                    print(contact)
            else:
                print("No contacts found.")
        except Exception as ex:
            print(f"An error occurred during the search: {ex}")
    else:
        print("Invalid search type. Please choose 'name', 'email', or 'phone'.")

@error_handler
def handle_edit_contact(manager: ContactManager) -> None:
    """
    Handles the editing of an existing contact in the contact manager.

    Prompts the user to enter the name of the contact to edit, and then allows the user to update
    the contact's address, phone number, email, and birthday. It performs basic validation to ensure
    that the name is not empty and attempts to update the contact in the manager.
    If an error occurs during the process, it prints an appropriate error message.

    Parameters:
        manager (ContactManager): An instance of ContactManager to manage contacts.
    """
    try:
        name = input("Enter the name of the contact to edit: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        address = input("Enter new address (leave blank to keep current): ").strip()
        phone_number = input("Enter new phone number (leave blank to keep current): ").strip()
        email = input("Enter new email (leave blank to keep current): ").strip()
        birthday = input("Enter new birthday (leave blank to keep current): ").strip()

        updated_contact_data = {}
        if address:
            updated_contact_data['address'] = address
        if phone_number:
            updated_contact_data['phone_number'] = phone_number
        if email:
            updated_contact_data['email'] = email
        if birthday:
            updated_contact_data['birthday'] = birthday

        success = manager.edit_contact(name, updated_contact_data)
        if success:
            print(f"Contact {name} updated successfully!")
        else:
            print(f"Contact {name} not found.")
    except Exception as ex:
        print(f"An error occurred while editing the contact: {ex}")
