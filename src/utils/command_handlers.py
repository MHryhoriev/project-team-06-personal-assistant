from managers import ContactManager, NoteManager
from models import Contact
from utils.custom_decorators import error_handler
from managers import note_manager
from typing import Optional

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
    name = _prompt_for_non_empty_name("Enter name: ")
    if not name:
        return
        
    address = input("Enter address (or press Enter to skip): ").strip()
    phone_number = input("Enter phone number (or press Enter to skip): ").strip()
    email = input("Enter email (or press Enter to skip): ").strip()
    birthday = input("Enter birthday (DD.MM.YYYY) (or press Enter to skip): ").strip()

    new_contact = Contact(name=name, address=address, phone_number=phone_number, email=email, birthday=birthday)
    manager.add_contact(new_contact)

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

@error_handler
def handle_remove_contact(manager: ContactManager) -> None:
    """
    Handles the removal of a contact from the contact manager.

    Prompts the user to enter the name of the contact to be removed.
    It then attempts to remove the contact from the manager. If the contact is successfully removed,
    a success message is printed. If the contact is not found, an error message is displayed.

    Parameters:
        manager (ContactManager): An instance of ContactManager to manage contacts.
    """
    name = input("Enter the name of the contact to remove: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
        
    result = manager.remove_contact(name)
    print(result)

@error_handler
def handle_show_all_notes(note_manager: NoteManager) -> str:
    """
    Handles the display of all notes from a Note object.

    Args:
        note (Note): An instance of the Note class containing the data.

    Returns:
        str: A formatted string displaying all notes or a message if no notes are available.
    """
    
    all_notes = note_manager.get_all_notes()
    if not all_notes:
        print("No notes available.")
        return
        
    note_list = "\n".join(str(note) for note in all_notes)
    print(f"Notes:\n{note_list}")

@error_handler
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

@error_handler
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

@error_handler
def handle_show_all_contacts(manager: ContactManager) -> str:
    """
    Retrieves and formats all contacts from the ContactManager into a readable string.

    Args:
        manager (ContactManager): An instance of ContactManager that contains the contacts.

    Returns:
        str: A formatted string of all contacts or a message indicating no contacts are available.
    """
    contacts = manager.get_all_contacts()
    
    if not contacts:
        print("No contacts available.")
    else:
        contact_list = "\n".join(str(contact) for contact in contacts)
        print(f"Contacts:\n{contact_list}")
        
@error_handler
def handle_upcoming_birthdays(manager: ContactManager) -> None:
    """
    Handles the retrieval and display of upcoming birthdays.

    Prompts the user to enter the number of days to check for upcoming birthdays.
    It then calls the get_upcoming_birthdays method and displays the results.

    Args:
        manager (ContactManager): An instance of ContactManager to manage contacts.
    """
    while True:
        try:
            n_day_input = input("Enter the number of days to check for upcoming birthdays: ").strip()
            n_day = int(n_day_input)
            if n_day <= 0:
                print("Number of days must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    upcoming_birthdays = manager.get_upcoming_birthdays(n_day)
    
    if upcoming_birthdays:
        print("Upcoming birthdays:")
        for birthday in upcoming_birthdays:
            print(birthday)
    else:
        print("No upcoming birthdays within the specified period.")

@error_handler
def _prompt_for_non_empty_name(prompt: str) -> Optional[str]:
    """
    Prompts the user to enter a name and checks if it is non-empty.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        Optional[str]: The entered name if it is non-empty, otherwise None.
    """
    name = input(prompt).strip()
    if not name:
        print("Name cannot be empty.")
        return None
    return name