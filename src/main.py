from managers import ContactManager, NoteManager
from utils import (
    parse_input,
    handle_add_contact,
    handle_search_contact,
    handle_show_all_notes,
    handle_remove_contact,
    handle_show_all_contacts,
    handle_upcoming_birthdays
)
from storage import ContactStorage, NoteStorage
from constants import CONTACT_DATA_FILE_PATH, NOTE_DATA_FILE_PATH
from prompt_toolkit import PromptSession
from utils import suggest_command, completer


def main():
    """
    Main entry point for the Contact Manager console application.
    Initializes the ContactManager and provides a command-line interface for the user.
    """

    contact_storage = ContactStorage(file_path=CONTACT_DATA_FILE_PATH)
    contact_manager = ContactManager(storage=contact_storage)

    note_storage = NoteStorage(file_path=NOTE_DATA_FILE_PATH)
    note_manager = NoteManager(storage=note_storage)

    print("Welcome to the Contact Manager!")

    session = PromptSession(completer=completer)

    while True:
        try:
            user_input = session.prompt("Enter a command (add_contact/remove_contact/search_contact/all_contacts/all_notes/check_birthdays): ")
            command, *args = parse_input(user_input)

            if command in ["exit", "close"]:
                print("Good bye!")
                break
            elif command == "add_contact":
                handle_add_contact(contact_manager)
            elif command == "remove_contact":
                handle_remove_contact(contact_manager)
            elif command == "search_contact":
                handle_search_contact(contact_manager)
            elif command == "all_contacts":
                handle_show_all_contacts(contact_manager)
            elif command == "all_notes":
                handle_show_all_notes(note_manager)
            elif command == "check_birthdays":
                handle_upcoming_birthdays(contact_manager)
            else:
                suggest_command(user_input)

        except KeyboardInterrupt:
            print("\nGood bye!")
            break

if __name__ == "__main__":
    main()
