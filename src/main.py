from managers import ContactManager
from utils import parse_input, handle_add_contact, handle_search_contact


def main():
    """
    Main entry point for the Contact Manager console application.
    Initializes the ContactManager and provides a command-line interface for the user.
    """
    manager = ContactManager()
    print("Welcome to the Contact Manager!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break
        elif command == "add":
            handle_add_contact(manager)
        elif command == "remove":
            pass
        elif command == "search":
            handle_search_contact(manager)
        elif command == "all":
            pass
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
