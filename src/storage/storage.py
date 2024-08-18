import os
import json
from typing import List, Optional, TypeVar, Generic
from abc import ABC, abstractmethod
from colors import format_red

# Define a TypeVar for the generic type
T = TypeVar("T")


class Storage(Generic[T], ABC):
    """
    The Storage class is responsible for managing the persistent storage of data in a JSON file.
    It provides methods to load and save data, while also caching the data in memory to avoid
    redundant file operations.
    """

    def __init__(self, file_path: str) -> None:
        """
        Initializes the Storage object with the specified file path.

        Args:
            file_path (str): The path to the file where data is stored in JSON format.

        Attributes:
            file_path (str): The path to the file where data will be read from or written to.
            __data_cache (Optional[List[T]]): A cache for storing data loaded from the file.
                                            Initialized as None to indicate that data has not yet been loaded.
        """
        self.file_path = file_path
        self.__data_cache: Optional[List[T]] = None

    def __load_from_file(self) -> List[T]:
        """
        Loads data from the JSON file.

        Returns:
            List[T]: A list of objects of type T retrieved from the file. If the file does not
                     exist or there is an error, an empty list is returned.

        Side effects:
            Prints error messages to the console in case of file access or JSON decoding issues.
        """
        if not os.path.exists(self.file_path):
            print(format_red(f"File '{self.file_path}' does not exist."))
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    if not isinstance(data, list):
                        raise ValueError(
                            format_red("Data in the file is not a valid list.")
                        )
                    return [
                        self.create_instance(item) 
                        for item in data 
                        if self.is_valid_data(item)
                    ]
                except json.JSONDecodeError:
                    print(format_red("Error decoding JSON data."))
                    return []
        except (OSError, IOError) as ex:
            print(format_red(f"Error reading file '{self.file_path}': {ex}"))
            return []

    def load_data(self) -> List[T]:
        """
        Loads data from the cache or, if not cached, from the file.

        Returns:
            List[T]: A list of objects of type T. If the data is cached, it is returned from memory;
                     otherwise, the data is read from the file and cached.
        """
        if self.__data_cache is None:
            self.__data_cache = self.__load_from_file()
        return self.__data_cache

    def save_data(self, data: List[T]) -> None:
        """
        Saves the given list of data to the JSON file and updates the cache.

        Args:
            data (List[T]): A list of objects of type T to be saved.

        Side effects:
            Writes the data to the file in JSON format, printing error messages to the console
            in case of file access or JSON serialization issues.
        """
        self.__data_cache = data
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                try:
                    json.dump(
                        [item.to_dict() for item in data],
                        file,
                        ensure_ascii=False,
                        indent=4,
                    )
                except (TypeError, ValueError) as ex:
                    print(format_red(f"Error serializing data to JSON: {ex}"))
        except (OSError, IOError) as ex:
            print(format_red(f"Error writing to file '{self.file_path}': {ex}"))

    @abstractmethod
    def is_valid_data(self, data: dict) -> bool:
        """
        Validates whether the provided data contains all required fields.
        """
        pass

    @abstractmethod
    def create_instance(self, data: dict) -> T:
        """
        Creates an instance of type T from the provided data.
        """
        pass
