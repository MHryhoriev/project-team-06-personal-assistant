from managers import ContactManager, NoteManager
from utils import parse_input, handle_add_contact, handle_search_contact, handle_edit_contact
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
            user_input = session.prompt("Enter a command (add/search/edit/remove/exit): ")
            command, *args = parse_input(user_input)
            
            print(f"Command entered: {command}")  # Debugging line

            if command in ["exit", "close"]:
                print("Good bye!")
                break
            elif command == "add":
                handle_add_contact(contact_manager)
            elif command == "edit":
                handle_edit_contact(contact_manager)
            elif command == "remove":
                # Implement remove functionality here if needed
                pass
            elif command == "search":
                handle_search_contact(contact_manager)
            elif command == "all":
                # Implement all functionality here if needed
                pass
            else:
                suggest_command(user_input)

        except KeyboardInterrupt:
            print("\nGood bye!")
            break

if __name__ == "__main__":
    main()