import logging
from typing import Callable, Any
from colors import format_red
from utils.exceptions import ValidationError

# Logging settings
logging.basicConfig(
    level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def error_handler(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to handle and log errors in handlers.
    Catches specific and unforeseen exceptions and logs an error message.

    Args:
        func (Callable[..., Any]): The function to be decorated.

    Returns:
        Callable[..., Any]: The decorated function with error handling.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as ex:
            message = f"A ValidationError occurred: {ex}"
            logger.error("ValidationError in function '%s': %s", func.__name__, message)
            print(format_red(message))
        except ValueError as ex:
            message = f"A ValueError occurred: {ex}"
            logger.error("ValueError in function '%s': %s", func.__name__, message)
            print(format_red(message))
        except IndexError as ex:
            message = f"An IndexError occurred: {ex}"
            logger.error("IndexError in function '%s': %s", func.__name__, message)
            print(format_red(message))
        except KeyError as ex:
            message = f"A KeyError occurred: {ex}"
            logger.error("KeyError in function '%s': %s", func.__name__, message)
            print(format_red(message))
        except NotImplementedError as nie:
            message = f"A NotImplementedError occurred: {nie}"
            logger.error(
                "NotImplementedError in function '%s': %s", func.__name__, message
            )
            print(format_red(message))
        except Exception as un_err:
            message = f"An unexpected error occurred: {un_err}"
            logger.error(
                "Unexpected error in function '%s': %s", func.__name__, message
            )
            print(format_red(message))

    return wrapper