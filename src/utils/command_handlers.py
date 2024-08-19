from managers import ContactManager, NoteManager
from models import Contact, Note
from utils.custom_decorators import error_handler
from prettytable import PrettyTable
from typing import List, Dict, Any, Optional
from colors import format_yellow, format_green, format_red


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
    name = _prompt_for_non_empty_input("name", "Enter contact name (required): ")
    if not name:
        return

    if manager.search_by_name(name):
        print(format_red(f"Contact with the name '{name}' already exists."))
        return

    address = input("Enter address (or press Enter to skip): ").strip()
    phone_number = input("Enter phone number (required): ").strip()
    email = input("Enter email (required): ").strip()
    birthday = input("Enter birthday (DD.MM.YYYY) (or press Enter to skip): ").strip()

    new_contact = Contact(
        name=name,
        address=address,
        phone_number=phone_number,
        email=email,
        birthday=birthday,
    )
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
        "phone": manager.search_by_phone_number,
    }

    search_method = search_map.get(search_type, "")

    if search_method:
        try:
            results = search_method(query)
            if results:
                print(format_green(f"Found {len(results)} contact(s):"))
                _print_contacts(results)
            else:
                print(format_red("No contacts found."))
        except Exception as ex:
            print(format_red(f"An error occurred during the search: {ex}"))
    else:
        print(format_red("Invalid search type. Please choose 'name', 'email', or 'phone'."))


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
        name = _prompt_for_non_empty_input(
            "name", "Enter the name of the contact to edit: "
        )
        if not name:
            return

        address = input("Enter new address (or press Enter to keep current): ").strip()
        phone_number = input(
            "Enter new phone number (or press Enter to keep current): "
        ).strip()
        email = input("Enter new email (or press Enter to keep current): ").strip()
        birthday = input(
            "Enter new birthday (DD.MM.YYYY) (or press Enter to keep current): "
        ).strip()

        updated_contact_data = manager.search_by_name(name)
        if updated_contact_data is None:
            print(format_red(f"Contact with the name {name} not found."))
            return

        if address:
            updated_contact_data["address"] = address
        if phone_number:
            updated_contact_data["phone_number"] = phone_number
        if email:
            updated_contact_data["email"] = email
        if birthday:
            updated_contact_data["birthday"] = birthday

        # Update the contact
        manager.edit_contact(name, updated_contact_data)
    except Exception as ex:
        print(format_red(f"An error occurred while editing the contact: {ex}"))


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
        print(format_red("Name cannot be empty."))
        return
        
    manager.remove_contact(name)

    
@error_handler
def handle_show_all_notes(manager: NoteManager) -> None:
    """
    Handles the display of all notes from a Note object.

    Args:
        note (Note): An instance of the Note class containing the data.

    Returns:
        None: Prints A formatted string displaying all notes or a message if no notes are available.
    """
    all_notes = manager.get_all_notes()
    if not all_notes:
        print(format_red("No notes available."))
        return

    print(format_green(f"\nFound {len(all_notes)} note(s):"))
    _print_notes(all_notes)


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
        print(format_red("Invalid tag. Please provide a valid tag string."))
        return

    if not title:
        print(format_red("Note title cannot be empty."))
        return

    # Search for notes by title
    note_list = manager.search_by_title(title)
    if not note_list:
        print(format_red("No notes found with the given title."))
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
        print(format_red("Invalid tag. Please provide a valid tag string."))
        return

    if not note_name:
        print(format_red("Note title cannot be empty."))
        return

    # Search for notes by title
    note_list = manager.search_by_title(note_name)
    if not note_list:
        print(format_red("No notes found with the given title."))
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
        print(format_red("No contacts available."))
        return

    print(format_green(f"\nFound {len(contacts)} contact(s):"))
    _print_contacts(contacts)


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
            n_day_input = input(
                "Enter the number of days to check for upcoming birthdays: "
            ).strip()
            n_day = int(n_day_input)
            if n_day <= 0:
                print(format_red("Number of days must be positive. Please try again."))
                continue
            break
        except ValueError:
            print(
                format_red("Invalid input. Please enter a valid number.")
            )
    upcoming_birthdays = manager.get_upcoming_birthdays(n_day)

    if not upcoming_birthdays:
        print(format_red("No upcoming birthdays within the specified period."))
        return

    _print_upcoming_birthdays(upcoming_birthdays)


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

    title = input("Enter note title (required): ").strip()
    contact = input("Enter contact name: ").strip()
    content = input("Enter note content: ").strip()

    # Create a temporary note for validation
    temp_note = Note(
        id=len(manager.get_all_notes()) + 1,
        title=title,
        contact=contact,
        content=content,
    )

    # Validate the note before adding it
    if not manager.validate_note(temp_note):
        print(format_red("Validation failed. Note was not added."))
        return

    # Check for name uniqueness
    if any(note.title.lower() == title.lower() for note in manager.get_all_notes()):
        print(format_red(f"Error: A note with the title '{title}' already exists."))
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
        print(format_red(f"Error: {field_name.capitalize()} cannot be empty."))
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

    search_type = input("Search by (title/tag): ").strip().lower()
    query = input("Enter the search query: ").strip()

    search_map = {"title": manager.search_by_title, "tag": manager.search_by_tag}

    search_method = search_map.get(search_type, "")

    if search_method:
        try:
            results = search_method(query)
            if results:
                print(format_red(f"Found {len(results)} note(s):"))
                _print_notes(results)
            else:
                print(format_red("No notes found."))
        except Exception as ex: 
            print(
                format_red(f"An error occured during the search: {ex}")
            )
    else:
        print(format_red("Invalid search type. Please choose 'title' or 'tag'."))


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
           print(format_red("Title cannot be empty."))
           return
        
        # Fetch the list of notes matching the title
        notes_list = manager.search_by_title(title)
        if not notes_list:
            print(format_red(f"No notes found with the title '{title}'."))
            return

        # Assume that we want to edit the first matching note
        note_to_edit = notes_list[0]
        if not isinstance(note_to_edit, Note):
            print(format_red("The retrieved object is not a Note instance."))
            return

        new_content = input(
            "Enter new content (or press Enter to keep current): "
        ).strip()
        new_tags_input = input(
            "Enter new tags, separated by commas (or press Enter to keep current): "
        ).strip()
        new_tags = [tag.strip() for tag in new_tags_input.split(",") if tag.strip()]

        note_to_edit.update_content_and_tag(new_content, new_tags)

        # validate note before editing
        if not manager.validate_note(note_to_edit):
            print(format_red("Note validation failed. Please check details and try again."))
            return

        # update note
        manager.edit_note(note_to_edit.id, note_to_edit)

    except Exception as ex:
        print(format_red(f"An error occurred while editing the note: {ex}"))


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
        print(format_red("Title cannot be empty."))
        return

    manager.remove_note(title)


@error_handler
def handle_sort_notes_by_tags(manager: NoteManager) -> None:
    """
    Handles sorting of notes by their tags and displays them.

    Prompts the user to specify the sort order and then sorts the notes by their tags
    in the specified order. The method prints the details of each note including
    all fields such as title, content, tags, and updated timestamp.

    Args:
        manager (NoteManager): An instance of Note Manager to manage notes.
    """
    print("How would you like to sort the notes by tags?")
    sort_order = (
        input("Enter 'asc' for ascending or 'desc' for descending: ").strip().lower()
    )

    if sort_order not in ['asc', 'desc']:
        print(
            format_red("Invalid sort order. Please enter 'asc' or 'desc'.")
        )
        return

    sorted_notes = manager.sort_by_tags(order=sort_order)

    _print_sorted_notes(sorted_notes)


def _print_sorted_notes(sorted_notes: List[Any]) -> None:
    """
    Prints a table of sorted notes by tags.

    Args:
        sorted_notes (List[Any]): List of notes sorted by tags.
    """
    table_sorted_notes = PrettyTable()
    table_sorted_notes.field_names = [
        format_yellow("Title"),
        format_yellow("Content"),
        format_yellow("Tags"),
        format_yellow("Updated")
    ]


    for note in sorted_notes:
        tags_str = ", ".join(note.tags)
        table_sorted_notes.add_row(
            [note.title, note.content, tags_str, note.updated_at]
        )

    print(format_green("\nSorted notes by tags:"))
    print(table_sorted_notes)


def _print_upcoming_birthdays(upcoming_birthdays: List[Dict[str, str]]) -> None:
    """
    Prints a table of upcoming birthdays.

    Args:
        upcoming_birthdays (List[Dict[str, str]]): List of dictionaries containing birthday details.
    """
    table_birthdays = PrettyTable()
    table_birthdays.field_names = [
        format_yellow("Name"),
        format_yellow("Birthday")
    ]

    for birthday in upcoming_birthdays:
        table_birthdays.add_row([birthday["name"], birthday["congratulation_date"]])

    print(format_green("\nUpcoming birthdays:"))
    print(table_birthdays)


def _print_contacts(contacts: List[Any]) -> None:
    """
    Prints a table of contacts.

    Args:
        contacts (List[Any]): List of contact objects.
    """
    table_contacts = PrettyTable()
    table_contacts.field_names = [
        format_yellow("Name"),
        format_yellow("Address"),
        format_yellow("Phone Number"),
        format_yellow("Email"),
        format_yellow("Birthday")
    ]

    for contact in contacts:
        table_contacts.add_row(
            [
                contact.name,
                contact.address,
                contact.phone_number,
                contact.email,
                contact.birthday,
            ]
        )

    print(table_contacts)


def _print_notes(notes: List[Any]) -> None:
    """
    Prints a table of all notes.

    Args:
        all_notes (List[Any]): List of all notes.
    """
    table_notes = PrettyTable()
    table_notes.field_names = [
        format_yellow("ID"),
        format_yellow("Title"),
        format_yellow("Contact"),
        format_yellow("Content"),
        format_yellow("Tags"),
        format_yellow("Created At"),
        format_yellow("Updated At")
    ]

    for note in notes:
        tags_str = ", ".join(note.tags)
        table_notes.add_row(
            [
                note.id,
                note.title,
                note.contact,
                note.content,
                tags_str,
                note.created_at,
                note.updated_at,
            ]
        )

    print(table_notes)
