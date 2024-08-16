"""The module for custom decorators"""

from typing import Callable, Any

def error_handler(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to handle errors in handlers.
    Catches specific and unforeseen exceptions and logs an error message.

    Args:
        func (Callable[..., Any]): The function to be decorated.

    Returns:
        Callable[..., Any]: The decorated function.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Please enter the name.")
        except IndexError:
            print("To many names, try the command 'all' to investigate.")
        except KeyError:
            print("Enter the correct name please, try the command 'all' to investigate.")
        except NotImplementedError as nie:
            print(f"NotImplementedError in {func.__name__}: {nie}")
        except Exception as un_err:
            print(f"Unexpected error in {func.__name__}: {un_err}")
        
    return inner
