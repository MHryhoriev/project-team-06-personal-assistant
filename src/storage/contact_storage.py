from models import Contact
from storage import Storage


class ContactStorage(Storage[Contact]):
    """
    The ContactStorage class is responsible for managing the persistent storage of contact data
    in a JSON file. It extends the base Storage class with specific methods for handling contact data.
    """

    def is_valid_data(self, data: dict) -> bool:
        """
        Validates whether the provided contact data contains all required fields.

        Args:
            data (dict): The contact data to be validated.

        Returns:
            bool: True if the data contains all required fields, False otherwise.

        Side effects:
            Prints an error message to the console if any required fields are missing.
        """
        required_fields = {"name", "address", "phone_number", "email", "birthday"}
        missing_fields = required_fields - data.keys()
        if missing_fields:
            print(f"Missing fields in contact data: {missing_fields}")
            return False
        return True

    def create_instance(self, data: dict) -> Contact:
        """
        Creates a Contact instance from the provided data.

        Args:
            data (dict): The data to be used for creating a Contact instance.

        Returns:
            Contact: A Contact instance created from the provided data.
        """
        return Contact(**data)
