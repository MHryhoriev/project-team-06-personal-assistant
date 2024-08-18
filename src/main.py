from launcher import initialize_managers, handle_command
from utils import parse_input, completer, format_yellow, format_green
from prompt_toolkit import PromptSession

def main():
    """
    Main entry point for the Contact Manager console application.
    Initializes the ContactManager and provides a command-line interface for the user.
    """
    contact_manager, note_manager = initialize_managers()

    print(format_green("Welcome to the Contact Manager!"))
    session = PromptSession(completer=completer)

    while True:
        try:
            user_input = session.prompt("Enter a command: ")
            command, *args = parse_input(user_input)
            handle_command(command, contact_manager, note_manager)
        except KeyboardInterrupt:
            print(format_yellow("Good bye!"))
            break

if __name__ == "__main__":
    main()
