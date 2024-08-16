from managers import ContactManager
from models import Contact
from utils.custom_decorators import error_handler
from managers import note_manager
from typing import List

@error_handler
def handle_add_contact(manager: ContactManager) -> None:
    """
    Handles the addition of a new contact to the contact manager.

    Prompts the user to enter details for the new contact, such as name, address, phone number, email, and birthday.
    It performs basic validation to ensure that the name is not empty and attempts to add the contact to the manager.
    If an error occurs during the process, it prints an appropriate error message.

    Parameters:
        manager (ContactManager): An instance of ContactManager to manage contacts.
    """
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
    """
    Handles the search for contacts based on the specified search type.

    Prompts the user to select a search type ('name', 'email', or 'phone') and enter the search query.
    It then performs the search using the appropriate method from the ContactManager and displays the results.
    If an error occurs during the search, it prints an appropriate error message.

    Parameters:
        manager (ContactManager): An instance of ContactManager to manage contacts.
    """
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

def handle_add_tag(manager: note_manager, note_id: int, tag: str) -> str:
    """
    Handles the logic for adding a tag to a note.

    Args:
        note_manager (NoteManager): The manager responsible for note operations.
        note_id (int): The ID of the note to which the tag will be added.
        tag (str): The tag to be added to the note.

    Returns:
        str: A message indicating the result of the operation.
    """
    if not isinstance(note_id, int) or note_id <= 0:
        return "Invalid note ID."
    
    if not tag or not isinstance(tag, str):
        return "Invalid tag. Please provide a valid tag string."
    
    result = note_manager.add_tag(note_id, tag)
    return result

def handle_remove_tag(manager: note_manager, note_id: int, tag:str) -> str:
    """
    Handles the logic for removing a tag from a note.

    Args:
        note_manager (NoteManager): The manager responsible for note operations.
        note_id (int): The ID of the note from which the tag will be removed.
        tag (str): The tag to be removed from the note.

    Returns:
        str: A message indicating the result of the operation.
    """

    if not isinstance (note_id, int) or note_id <= 0:
      return "Invalid note ID."
    
    if not tag or not isinstance(tag, str):
      return "Invalid tag. Please provide a valid tag string."
    
    result = note_manager.remove_tag(note_id, tag)
    return result

def display_all_contacts(manager: ContactManager) -> str:
    """
    Displays all contacts in a readable format. Shows a message if there are no contacts.
    """
    contacts = manager.get_all_contacts()
    
    if not contacts:
        print("No contacts available.")
    else:
        contact_list = "\n".join(str(contact) for contact in contacts)
        print(f"Contacts:\n{contact_list}")
