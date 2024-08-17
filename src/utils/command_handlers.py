from managers import ContactManager, NoteManager
from models import Contact, Note
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
    name = _prompt_for_non_empty_input("name", "Enter contact name: ")
    if not name:
        return

    if manager.search_by_name(name):
        print(f"Contact with the name '{name}' already exists.")
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
def handle_edit_contact(manager: ContactManager) -> None:
    """
    Handles the editing of an existing contact in the contact manager.

    Prompts the user to enter the name of the contact to be edited and the new details for the contact.
    It then attempts to update the contact in the manager. If the contact is successfully updated,
    a success message is printed. If the contact is not found or an error occurs, an error message is displayed.

    Args:
        manager (ContactManager): An instance of ContactManager to manage contacts.
    """
    try:
        name = _prompt_for_non_empty_input("name", "Enter the name of the contact to edit: ")
        if not name:
            return

        address = input("Enter new address (or press Enter to keep current): ").strip()
        phone_number = input("Enter new phone number (or press Enter to keep current): ").strip()
        email = input("Enter new email (or press Enter to keep current): ").strip()
        birthday = input("Enter new birthday (DD.MM.YYYY) (or press Enter to keep current): ").strip()

        updated_contact_data = manager.search_by_name(name)
        if updated_contact_data is None:
            print(f"Contact with the name {name} not found.")
            return

        if address:
            updated_contact_data['address'] = address
        if phone_number:
            updated_contact_data['phone_number'] = phone_number
        if email:
            updated_contact_data['email'] = email
        if birthday:
            updated_contact_data['birthday'] = birthday

        # Update the contact
        manager.edit_contact(name, updated_contact_data)
    except Exception as ex:
        print(f"An error occurred while editing the contact: {ex}")

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
def handle_show_all_notes(note_manager: NoteManager) -> None:
    """
    Handles the display of all notes from a Note object.

    Args:
        note (Note): An instance of the Note class containing the data.

    Returns:
        None: Prints A formatted string displaying all notes or a message if no notes are available.
    """
    
    all_notes = note_manager.get_all_notes()
    if not all_notes:
        print("No notes available.")
        return
        
    note_list = "\n".join(str(note) for note in all_notes)
    print(f"Notes:\n{note_list}")

@error_handler
def handle_add_tag(manager: NoteManager) -> None:
    """
    Handles the logic for adding a tag to notes matching a specified title.

    Args:
        manager (NoteManager): The manager responsible for note operations.

    Returns:
        None: Prints messages indicating the result of the operation.
    """
    title = input("Please, enter the Note title: ").strip().lower()
    tag = input("Please, enter the tag name: ").strip()

    # Validate tag input
    if not tag or not isinstance(tag, str):
        print("Invalid tag. Please provide a valid tag string.")
        return

    if not title:
        print("Note title cannot be empty.")
        return

    # Search for notes by title
    note_list = manager.search_by_title(title)
    if not note_list:
        print("No notes found with the given title.")
        return

    for note in note_list:
        manager.add_tag(note.id, tag)

@error_handler
def handle_remove_tag(manager: NoteManager) -> None:
    """
    Handles the logic for removing a tag from notes matching a specified title.

    Args:
        manager (NoteManager): The manager responsible for note operations.

    Returns:
        None: Prints messages indicating the result of the operation.
    """
    note_name = input("Please, enter the Note title for removing: ").strip().lower()
    tag = input("Please, enter the tag name for removing: ").strip()

    # Validate inputs
    if not tag or not isinstance(tag, str):
        print("Invalid tag. Please provide a valid tag string.")
        return

    if not note_name:
        print("Note title cannot be empty.")
        return

    # Search for notes by title
    note_list = manager.search_by_title(note_name)
    if not note_list:
        print("No notes found with the given title.")
        return

    for note in note_list:
        manager.remove_tag(note.id, tag)


@error_handler
def handle_show_all_contacts(manager: ContactManager) -> None:
    """
    Retrieves and formats all contacts from the ContactManager into a readable string.

    Args:
        manager (ContactManager): An instance of ContactManager that contains the contacts.

    Returns:
        None: Prints A formatted string of all contacts or a message indicating no contacts are available.
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
def handler_search_notes_by_tag(manager: NoteManager, tag: str) -> None:
    """
    Handles the display of all notes from a NoteManager object filtered by tags.

    Args:
        tag (str): An instance of the Note class containing the data.

    Returns:
        None: Prints A formatted string displaying filtered notes or a message if no notes are available.
    """
    all_notes = manager.search_notes_by_tag(tag)
    if not all_notes:
        print("No notes available.")
        return
        
    note_list = "\n".join(str(note) for note in all_notes)
    print(f"Notes:\n{note_list}")

@error_handler
def handle_add_note(manager: NoteManager) -> None:
    """
    Handles the addition of a new note to the note manager.

    Prompts the user to enter details for the new note, such as title and content.
    It performs validation to ensure that the title is unique, meets length requirements, 
    and that the content is not empty. If validation passes, the note is added to the manager.

    Parameters:
        manager (NoteManager): An instance of NoteManager to manage notes.
    """
    
    title = input("Enter note title: ").strip()
    contact = input("Enter contact name: ").strip()
    content = input("Enter note content: ").strip()

    # Create a temporary note for validation
    temp_note = Note(
        id=len(manager.get_all_notes()) + 1,
        title=title,
        contact=contact,
        content=content
    )

    # Validate the note before adding it
    if not manager.validate_note(temp_note):
        print("Validation failed. Note was not added.")
        return
    
    # Check for name uniqueness
    if any(note.title.lower() == title.lower() for note in manager.get_all_notes()):
        print(f"Error: A note with the title '{title}' already exists.")
        return

    manager.add_note(temp_note)

@error_handler
def _prompt_for_non_empty_input(field_name: str, prompt: str) -> Optional[str]:
    """
    Prompts the user to enter a name and checks if it is non-empty.

    Args:
        prompt (str): The prompt message to display to the user.

    Returns:
        Optional[str]: The entered name if it is non-empty, otherwise None.
    """
    value = input(prompt).strip()
    if not value:
        print(f"Error: {field_name.capitalize()} cannot be empty.")
        return None
    return value

@error_handler
def handle_search_notes(manager: NoteManager) -> None:
    """
    Handles the search for notes based on the specified search type.

    Prompts the user to select a search type ('title' or 'tag') and enter the search query.
    It then performs the search using the appropriate method from the NoteManager and displays the results.
    If an error occurs during the search, it prints an appropriate error message.

    Parameters:
        manager (NoteManager): An instance of NoteManager to manage notes.
    """

    search_type = input("Search by (title/tag): " ).strip().lower()
    query = input("Enter the search query: ").strip()

    search_map = {
        "title": manager.search_by_title,
        "tag": manager.search_by_tag
    }

    search_method = search_map.get(search_type, "")

    if search_method:
        try:
            results = search_method(query)
            if results:
                print(f"Found {len(results)} note(s):")
                for note in results:
                    print(note)
            else:
                print("No notes found.")
        except Exception as ex: 
            print(f"An error occured during the search: {ex}")
    else:
        print("Invalid search type. Please choose 'title' or 'tag'.")

@error_handler
def handle_edit_note(manager: NoteManager) -> None:
    """
    Handles the editing of an existing note in the note manager.

    Prompts the user to enter the title of the note to be edited and the new details for the note.
    It then attempts to update the note in the manager. Before updating, it validates the note.
    If the note is successfully updated, a success message is printed. If the note is not found,
    validation fails, or an error occurs, an error message is displayed.

    Args:
        manager (note_manager): An instance of Note Manager to manage notes.
         
    """
    try:
        # Promprt for the note title and esures it is not empty
        title = input("Enter the title of the note to edit: ").strip()
        if not title:
           print("Title cannot be empty.")
           return
        
        # Fetch the list of notes matching the title
        notes_list = manager.search_by_title(title)
        if not notes_list:
            print(f"No notes found with the title '{title}'.")
            return

        # Assume that we want to edit the first matching note
        note_to_edit = notes_list[0]
        if not isinstance(note_to_edit, Note):
            print("The retrieved object is not a Note instance.")
            return
        
        new_content = input("Enter new content (or press Enter to keep current): ").strip()
        new_tags_input = input("Enter new tags, separated by commas (or press Enter to keep current): ").strip()
        new_tags = [tag.strip() for tag in new_tags_input.split(',') if tag.strip()]
        
        note_to_edit.update_content_and_tag(new_content, new_tags)

        #validate note before editing
        if not manager.validate_note(note_to_edit):
            print("Note validation failed. Please check details and try again.")
            return
        
        #update note
        manager.edit_note(note_to_edit.id, note_to_edit)

    except Exception as ex:
        print(f"An error occurred while editing the note: {ex}")

@error_handler
def handle_remove_note(manager: NoteManager) -> None:
    """
    Handles the removal of a note for the manager.

    Prompts user to enter title of the note to be deleted.
    It then attempts to remove the note from the manager. If note is successfully deleted,
    a success message is printed. If note is note found, an error message to be displayed. 
    
    """
    title = input("Enter the title of the note to remove: ").strip()
    if not title:
        print ("Title cannot be empty.")
        return
    
    result = manager.remove_note(title)
    print(result)

@error_handler
def handle_sort_notes_by_tags(manager: NoteManager) -> None:
    print("How would you like to sort the notes by tags?")
    sort_order = input("Enter 'asc' for ascending or 'desc' for descending: ").strip().lower()

    if sort_order not in ['asc', 'desc']:
        print("Invalid sort order. Please enter 'asc' or 'desc'.")
        return

    sorted_notes = manager.sort_notes_by_tags(order=sort_order)

    print("\nSorted notes by tags:")
    for note in sorted_notes:
        print(f"Title: {note.title}, Tags: {', '.join(note.tags)}")
