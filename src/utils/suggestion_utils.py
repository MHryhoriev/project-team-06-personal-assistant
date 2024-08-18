from fuzzywuzzy import process
from prompt_toolkit.completion import WordCompleter
from constants import COMMANDS
from colors import format_purple, format_red

# Initialize a WordCompleter instance for autocompletion of commands
completer = WordCompleter(COMMANDS, ignore_case=True)

def get_closest_command(user_input: str, similarity: int) -> str:
    """
    Finds the closest matching command from the list of valid commands.

    Args:
        user_input (str): The command entered by the user.
        similarity (int): The minimum similarity score (as a percentage) required to suggest a command.

    Returns:
        str: The closest matching command or None if no match is found.
    """
    suggestion, score = process.extractOne(user_input, COMMANDS)
    if score > similarity:
        return suggestion
    return None

def suggest_command(user_input: str, similarity: int = 70) -> None:
    """
    Suggests the closest matching command based on user input using fuzzy string matching.

    This function takes the user's input command and compares it against a predefined list of valid commands.
    If the similarity score between the user's input and a valid command exceeds the threshold, 
    the function suggests the closest matching command.

    Args:
        user_input (str): The command entered by the user.
        similarity (int, optional): The minimum similarity score (as a percentage) required to suggest 
                                    a command. Default is 70%.

    Returns:
        None. This function prints a suggestion if a close match is found, or a message indicating 
        that no close match was found.

    Example:
        If the user types "addd" instead of "add", the function might output:
        "Invalid command. Did you mean: add?"
    """
    try:
        suggestion = get_closest_command(user_input, similarity)
        if suggestion:
            print(format_purple(f"Invalid command. Did you mean: {suggestion}?"))
        else:
            print(format_red("Invalid command."))
    except Exception as ex:
        print(format_red(f"An error occurred while suggesting a command: {ex}"))