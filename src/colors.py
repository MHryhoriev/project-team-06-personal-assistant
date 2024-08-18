from colorama import Fore, Style, init

# Initialize colorama for color support on Windows
init(autoreset=True)

def format_yellow(message: str) -> str:
    """
    Formats a message in yellow color.
    
    Args:
        message (str): The message to be formatted.
    
    Returns:
        str: The formatted message string.
    """
    return f"{Fore.YELLOW}{message}{Style.RESET_ALL}"

def format_purple(message: str) -> str:
    """
    Formats a message in purple color.
    
    Args:
        message (str): The message to be formatted.
    
    Returns:
        str: The formatted message string.
    """
    return f"{Fore.MAGENTA}{message}{Style.RESET_ALL}"

def format_red(message: str) -> str:
    """
    Formats a message in red color.
    
    Args:
        message (str): The message to be formatted.
    
    Returns:
        str: The formatted message string.
    """
    return f"{Fore.RED}{message}{Style.RESET_ALL}"

def format_green(message: str) -> str:
    """
    Formats a message in green color.
    
    Args:
        message (str): The message to be formatted.
    
    Returns:
        str: The formatted message string.
    """
    return f"{Fore.GREEN}{message}{Style.RESET_ALL}"
