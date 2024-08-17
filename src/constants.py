"""
This module contains constants used throughout the application.
"""

from pathlib import Path

# Individual command constants
class COMMAND:
    ADD_CONTACT = "add_contact"
    ADD_NOTE = "add_note"
    EDIT_CONTACT = "edit_contact"
    SEARCH_CONTACT = "search_contact"
    REMOVE_CONTACT = "remove_contact"
    ALL_NOTES = "all_notes"
    ALL_CONTACTS = "all_contacts"
    CHECK_BIRTHDAYS = "check_birthdays"
    EXIT = "exit"
    HELP = "help"


# List of all commands
COMMANDS = [
    COMMAND.ADD_CONTACT,
    COMMAND.EDIT_CONTACT,
    COMMAND.ADD_NOTE,
    COMMAND.SEARCH_CONTACT,
    COMMAND.REMOVE_CONTACT,
    COMMAND.ALL_NOTES,
    COMMAND.ALL_CONTACTS,
    COMMAND.CHECK_BIRTHDAYS,
    COMMAND.EXIT,
    COMMAND.HELP
]

# Command descriptions
COMMAND_DESCRIPTIONS = {
    COMMAND.ADD_CONTACT: "Add a new contact",
    COMMAND.ADD_NOTE: "Add a new note",
    COMMAND.EDIT_CONTACT: "Edit an existing contact",
    COMMAND.SEARCH_CONTACT: "Search for a contact",
    COMMAND.REMOVE_CONTACT: "Remove a contact",
    COMMAND.ALL_NOTES: "Show all notes",
    COMMAND.ALL_CONTACTS: "Show all contacts",
    COMMAND.CHECK_BIRTHDAYS: "Check upcoming birthdays",
    COMMAND.EXIT: "Exit the application",
    COMMAND.HELP: "Show available commands"
}

# File paths
BASE_DIR = Path(__file__).resolve().parent.parent
CONTACT_DATA_FILE_PATH = BASE_DIR.joinpath('data', 'contacts_data.json')
NOTE_DATA_FILE_PATH = BASE_DIR.joinpath('data', 'note_data.json')
