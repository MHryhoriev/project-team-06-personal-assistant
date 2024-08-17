from managers import ContactManager, NoteManager
from storage import ContactStorage, NoteStorage
from constants import CONTACT_DATA_FILE_PATH, NOTE_DATA_FILE_PATH, COMMAND, COMMAND_DESCRIPTIONS
from utils import suggest_command
from utils import (
    handle_add_contact,
    handle_search_contact,
    handle_show_all_notes,
    handle_remove_contact,
    handle_show_all_contacts,
    handle_upcoming_birthdays,
    handle_edit_contact,
    handle_add_note,
    handle_search_notes,
    handle_remove_note,
    handle_edit_note,
    handle_add_tag,
    handle_remove_tag,
    handle_sort_notes_by_tags
)

def initialize_managers() -> tuple[ContactManager, NoteManager]:
    """
    Initializes the contact and note managers with storage.
    
    Returns:
        tuple[ContactManager, NoteManager]: Initialized managers for contacts and notes.
    """
    contact_storage = ContactStorage(file_path=CONTACT_DATA_FILE_PATH)
    note_storage = NoteStorage(file_path=NOTE_DATA_FILE_PATH)

    contact_manager = ContactManager(storage=contact_storage)
    note_manager = NoteManager(storage=note_storage)
    
    return contact_manager, note_manager

def handle_command(command: str, contact_manager: ContactManager, note_manager: NoteManager) -> None:
    """
    Handles the execution of a command.

    Args:
        command (str): The command entered by the user.
        args (list): The arguments for the command.
        contact_manager (ContactManager): The manager for contacts.
        note_manager (NoteManager): The manager for notes.
        available_commands (dict): A dictionary of available commands and descriptions.
    """
    command_map = {
        COMMAND.ADD_CONTACT: lambda: handle_add_contact(contact_manager),
        COMMAND.ADD_NOTE: lambda: handle_add_note(note_manager),
        COMMAND.ADD_TAG: lambda: handle_add_tag(note_manager),
        COMMAND.EDIT_CONTACT: lambda: handle_edit_contact(contact_manager),
        COMMAND.EDIT_NOTE: lambda: handle_edit_note(note_manager), # not finished
        COMMAND.REMOVE_CONTACT: lambda: handle_remove_contact(contact_manager),
        COMMAND.REMOVE_NOTE: lambda: handle_remove_note(note_manager),
        COMMAND.REMOVE_TAG: lambda: handle_remove_tag(note_manager),
        COMMAND.SEARCH_CONTACT: lambda: handle_search_contact(contact_manager),
        COMMAND.SEARCH_NOTE: lambda: handle_search_notes(note_manager),
        COMMAND.ALL_CONTACTS: lambda: handle_show_all_contacts(contact_manager),
        COMMAND.ALL_NOTES: lambda: handle_show_all_notes(note_manager),
        COMMAND.CHECK_BIRTHDAYS: lambda: handle_upcoming_birthdays(contact_manager),
        COMMAND.SORT_NOTES: lambda: handle_sort_notes_by_tags(note_manager),
        COMMAND.HELP: lambda: show_help(COMMAND_DESCRIPTIONS),
        COMMAND.EXIT: lambda: exit_program()
    }

    handler = command_map.get(command)
    if handler:
        handler()
    else:
        suggest_command(command)

def show_help(available_commands: dict) -> None:
    """
    Prints the list of available commands and their descriptions.

    Args:
        available_commands (dict): A dictionary of available commands and descriptions.
    """
    print("\nAvailable commands:")
    max_length = max(len(cmd) for cmd in available_commands.keys())
    for cmd, description in available_commands.items():
        print(f"  {cmd.ljust(max_length)} : {description}")
    print()

def exit_program() -> None:
    """Handles program exit."""
    print("Good bye!")
    import sys
    sys.exit()