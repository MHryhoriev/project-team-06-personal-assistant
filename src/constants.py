"""
This module contains constants used throughout the application.
"""

from pathlib import Path

# Individual command constants
class COMMAND:
    ADD_CONTACT = "add_contact"
    ADD_NOTE = "add_note"
    ADD_TAG = "add_tag"
    EDIT_CONTACT = "edit_contact"
    EDIT_NOTE = "edit_note"
    SEARCH_CONTACT = "search_contact"
    SEARCH_NOTE = "search_note"
    REMOVE_CONTACT = "remove_contact"
    REMOVE_NOTE = "remove_note"
    REMOVE_TAG = "remove_tag"
    ALL_NOTES = "all_notes"
    ALL_CONTACTS = "all_contacts"
    CHECK_BIRTHDAYS = "check_birthdays"
    SORT_NOTES = "sort_notes"
    EXIT = "exit"
    HELP = "help"


# List of all commands
COMMANDS = [
    COMMAND.ADD_CONTACT,
    COMMAND.ADD_NOTE,
    COMMAND.ADD_TAG,
    COMMAND.EDIT_CONTACT,
    COMMAND.EDIT_NOTE,
    COMMAND.SEARCH_CONTACT,
    COMMAND.SEARCH_NOTE,
    COMMAND.REMOVE_CONTACT,
    COMMAND.REMOVE_NOTE,
    COMMAND.REMOVE_TAG,
    COMMAND.ALL_NOTES,
    COMMAND.ALL_CONTACTS,
    COMMAND.CHECK_BIRTHDAYS,
    COMMAND.SORT_NOTES,
    COMMAND.EXIT,
    COMMAND.HELP
]

# Command descriptions
COMMAND_DESCRIPTIONS = {
    COMMAND.ADD_CONTACT: "Add a new contact",
    COMMAND.ADD_NOTE: "Add a new note",
    COMMAND.ADD_TAG: "Add a tag for exisiting note",
    COMMAND.EDIT_CONTACT: "Edit an existing contact",
    COMMAND.EDIT_NOTE: "Edit an existing note",
    COMMAND.SEARCH_CONTACT: "Search for a contact",
    COMMAND.SEARCH_NOTE: "Search for a note",
    COMMAND.REMOVE_CONTACT: "Remove a contact",
    COMMAND.REMOVE_NOTE: "Remove a note",
    COMMAND.REMOVE_TAG: "Remove a tag from specific note",
    COMMAND.ALL_NOTES: "Show all notes",
    COMMAND.ALL_CONTACTS: "Show all contacts",
    COMMAND.CHECK_BIRTHDAYS: "Check upcoming birthdays",
    COMMAND.SORT_NOTES: "Sorting notes",
    COMMAND.EXIT: "Exit the application",
    COMMAND.HELP: "Show available commands"
}

# File paths
BASE_DIR = Path(__file__).resolve().parent.parent
CONTACT_DATA_FILE_PATH = BASE_DIR.joinpath('data', 'contacts_data.json')
NOTE_DATA_FILE_PATH = BASE_DIR.joinpath('data', 'note_data.json')
