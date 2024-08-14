import os
import json
from dataclasses import dataclass, field
from typing import List, Optional
from models import Contact

@dataclass
class Storage:
    """
    The Storage class is responsible for managing the persistent storage of contact data in a JSON file.
    It provides methods to load and save contact data, while also caching the data in memory to avoid
    redundant file operations.
    """

    file_path: str
    __data_cache: Optional[List[Contact]] = field(default=None, init=False)
    

    def __load_from_file(self) -> List[Contact]:
        """
        Loads contact data from the JSON file.

        Returns:
            List[Contact]: A list of Contact objects retrieved from the file. If the file does not
                           exist or there is an error, an empty list is returned.

        Side effects:
            Prints error messages to the console in case of file access or JSON decoding issues.
        """
        if not os.path.exists(self.file_path):
            print(f"File '{self.file_path}' does not exist.")
            return []
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    if not isinstance(data, list):
                        raise ValueError("Data in the file is not a valid list.")
                    contacts = [Contact(**contact) for contact in data if self.__is_valid_contact_data(contact)]
                    return contacts
                except json.JSONDecodeError:
                    print("Error decoding JSON data.")
                    return []
        except (OSError, IOError) as ex:
            print(f"Error reading file '{self.file_path}': {ex}")
            return []
        
        
    def load_data(self) -> List[Contact]:
        """
        Loads contact data from the cache or, if not cached, from the file.

        Returns:
            List[Contact]: A list of Contact objects. If the data is cached, it is returned from memory;
                           otherwise, the data is read from the file and cached.
        """
        if self.__data_cache is None:
            self.__data_cache = self.__load_from_file()
        return self.__data_cache
    

    def save_data(self, contacts: List[Contact]) -> None:
        """
        Saves the given list of contacts to the JSON file and updates the cache.

        Args:
            contacts (List[Contact]): A list of Contact objects to be saved.

        Side effects:
            Writes the contact data to the file in JSON format, printing error messages to the console
            in case of file access or JSON serialization issues.
        """
        self._data_cache = contacts
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                try:
                    json.dump([contact.to_dict() for contact in contacts], file, ensure_ascii=False, indent=4)
                except (TypeError, ValueError) as ex:
                    print(f"Error serializing contacts data to JSON: {ex}")
        except (OSError, IOError) as ex:
            print(f"Error writing to file '{self.file_path}': {ex}")


    def __is_valid_contact_data(self, data: dict) -> bool:
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