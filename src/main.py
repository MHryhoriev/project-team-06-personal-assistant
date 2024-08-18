from launcher import initialize_managers, handle_command
from utils import parse_input, completer
from prompt_toolkit import PromptSession
from colors import format_yellow, format_green, format_red

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
            if user_input:
                command, *args = parse_input(user_input)
                handle_command(command, contact_manager, note_manager)
            else:
                print(format_red("No command entered. Please try again."))
        except KeyboardInterrupt:
            print(format_yellow("Good bye!"))
            break

if __name__ == "__main__":
    main()
