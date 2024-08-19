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
            logger.error("ValidationError in function '%s': %s", func.__name__, message)
            print(ex)
        except ValueError:
            message = "A ValueError occurred. Please provide the required input."
            logger.error("ValueError in function '%s': %s", func.__name__, message)
            print(format_red(message))
        except IndexError:
            message = "An IndexError occurred. The input seems to be incorrect or too many entries were provided."
            logger.error("IndexError in function '%s': %s", func.__name__, message)
            print(format_red(message))
        except KeyError:
            message = "A KeyError occurred. The specified key is missing or incorrect."
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