from models import Note
from storage import Storage
from colors import format_red

class NoteStorage(Storage[Note]):
    """
    The NoteStorage class is responsible for managing the persistent storage of note data
    in a JSON file. It extends the base Storage class with specific methods for handling note data.
    """

    def is_valid_data(self, data: dict) -> bool:
        """
        Validates whether the provided note data contains all required fields.

        Args:
            data (dict): The note data to be validated.

        Returns:
            bool: True if the data contains all required fields, False otherwise.

        Side effects:
            Prints an error message to the console if any required fields are missing.
        """
        required_fields = {"id", "title", "contact", "content", "created_at", "updated_at", "tags"}
        missing_fields = required_fields - data.keys()
        if missing_fields:
            print(format_red(f"Missing fields in note data: {missing_fields}"))
            return False
        return True


    def create_instance(self, data: dict) -> Note:
        """
        Creates a Note instance from the provided data.

        Args:
            data (dict): The data to be used for creating a Note instance.

        Returns:
            Note: A Note instance created from the provided data.
        """
        return Note(**data)
