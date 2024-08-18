"""The Note Manager logic module


"""

import re
from typing import List
from models import Note
from storage import NoteStorage
from colors import format_red, format_green


class NoteManager:
    def __init__(self, storage: NoteStorage) -> None:
        """
        Initializes the NoteManager with a NoteStorage instance.

        Args:
            storage (NoteStorage): An instance of NoteStorage for managing note data.
        """
        self.storage = storage
        self.notes: List[Note] = self.storage.load_data()

    def get_note_by_id(self, note_id: int) -> Note:
        """Method returns note by it`s id

        Args:
            note_id (int): Note Id number.

        Returns:
            Note: Returns Founded Note otherwise None
        """
        results = [note for note in self.notes if note.id == note_id]
        return results[-1] if results else None

    def validate_note(self, note: Note, min_title_length: int = 5) -> bool:
        """
        Validates the title, content, and contact of a Note object.

        This method checks whether the note's title meets the minimum length requirement,
        ensures that the content and contact are not empty, and returns validation results.

        Args:
            note (Note): The Note object to be validated.
            min_title_length (int, optional): The minimum length required for the title. Default is 5 characters.

        Returns:
            bool: True if the note is valid (title, content, and contact meet the requirements), False otherwise.
        """
        errors = {
            "title": f"The title must not be empty and should have at least {min_title_length} characters.",
            "content": "The content must not be empty.",
            "contact": "The contact must not be empty.",
        }

        if len(note.title or "") < min_title_length:
            print(format_red(f"Error: {errors['title']}"))
            return False
        if not note.content:
            print(format_red(f"Error: {errors['content']}"))
            return False
        if not note.contact:
            print(format_red(f"Error: {errors['contact']}"))
            return False

        return True

    def add_note(self, note: Note) -> None:
        """
        Adds a new note to the list of notes if the title is unique.

        This method checks if a note with the same title (case-insensitive) already exists in the list.
        If a note with the same title exists, an error message is printed and the note is not added.
        Otherwise, the note is added to the list, and a success message is printed.

        Args:
            note (Note): The Note object to be added.
        """
        for existing_note in self.notes:
            if existing_note.title.lower() == note.title.lower():
                print(format_red(f"Error: A note with the same '{note.title}' already exists"))
                return

        self.notes.append(note)
        self.storage.save_data(self.notes)
        print(format_green(f"Success: Note titled '{note.title}' successfully added."))

    def search_by_title(self, query: str) -> List[Note]:
        """
        Searches for notes by title or content and returns a list of matching notes.

        This method searches through the list of notes and checks if the search query
        is present in the title of any note (case-insensitive). It returns a list of
        notes that match the search query.

        Args:
            query (str): The search query string used to find matching notes.

        Returns:
            List[Note]: A list of Note objects that match the search query. If no matches
            are found, an empty list is returned.

        Raises:
            ValueError: If the search query is empty or consists only of whitespace.
            RuntimeError: If there is an issue with the search pattern or an unexpected error occurs.
        """
        try:
            if not query.strip():
                raise ValueError(format_red("Search name cannot be empty."))

            pattern = re.compile(re.escape(query), re.IGNORECASE)
            matching_notes = [note for note in self.notes if pattern.search(note.title)]

            return matching_notes

        except re.error as e:
            raise RuntimeError(
                format_red(f"An error occurred while processing the search pattern: {e}")
            )
        except Exception as e:
            raise RuntimeError(
                format_red(f"An unexpected error occurred during the search: {e}")
            )

    def edit_note(self, note_id: int, updated_note: Note) -> None:
        """
        Updates a note with the specified note_id with new data.

        This method searches for the note with the given note_id and updates its content and tags
        using the data provided in the `updated_note` object. After updating, the method saves the
        changes to storage and displays a success message. If no note with the specified ID is found,
        an error message is displayed.

        Args:
            note_id (int): The ID of the note to be updated.
            updated_note (Note): A Note object containing the updated content and tags.

        Returns:
            None: Prints a message indicating the result of the operation.
        """
        note = self.get_note_by_id(note_id)
        if note:
            note.update_content_and_tag(updated_note.content, updated_note.tags)
            self.storage.save_data(self.notes)
            print(format_green(f"Note '{note.title}' updated successfully."))
        else:
            print(format_red(f"Note with id {note_id} not found."))

    def remove_note(self, title: str) -> None:
        """
        Deletes a note with the specified title from the list of notes.

        This method searches for a note in the list that matches the provided title. If the note is found,
        it is removed from the list, and the updated list of notes is saved using the storage system.
        A success message is displayed upon successful deletion. If no note with the specified title is found,
        an error message is displayed.

        Args:
            title (str): The title of the note to be deleted.

        Raises:
            ValueError: If no note with the specified title is found, an error message is printed.
        """
        note_to_remove = next(
            (note for note in self.notes if note.title == title), None
        )
        if note_to_remove:
            self.notes.remove(note_to_remove)
            self.storage.save_data(self.notes)
            print(format_green(f"Note '{title}' successfully deleted."))
        else:
            print(format_red(f"Note '{title}' not found."))

    def search_by_tag(self, tag: str) -> List[Note]:
        """
        Searches for notes that contain the specified tag.

        This method iterates through the list of notes and returns a list of notes
        that have the specified tag in their tags.

        Args:
            tag (str): The tag to search for in the notes.

        Returns:
            List[Note]: A list of notes that contain the specified tag. If no notes contain
                        the tag, an empty list is returned.
        """

        if not tag.strip():
            raise ValueError(format_red("Tag cannot be empty or whitespace."))

        return [note for note in self.notes if tag in note.tags]

    def sort_by_tags(self, order: str = "asc") -> List[Note]:
        """
        Sort the notes by the number of tags and then alphabetically by tags.

        The primary sorting is by the number of tags. If there are multiple notes
        with the same number of tags, they are then sorted alphabetically based
        on the tags. The sorting order is determined by the `order` parameter.

        Args:
            order (str): The order of sorting. Must be either 'asc' for ascending
            or 'desc' for descending. Default is 'asc'.

        Returns:
            List[Note]: A list of notes sorted by the specified criteria.

        Raises:
            ValueError: If `order` is not 'asc' or 'desc'.
        """
        if order not in ('asc', 'desc'):
            raise ValueError(format_red("Order must be 'asc' or 'desc'"))
        
        if order == 'asc':
            sorted_notes = sorted(
                self.notes, key=lambda note: (len(note.tags), sorted(note.tags))
            )
        else:
            sorted_notes = sorted(
                self.notes,
                key=lambda note: (len(note.tags), sorted(note.tags)),
                reverse=True,
            )

        return sorted_notes

    def get_all_notes(self) -> List[Note]:
        """
        Retrieves all notes from the notes collection.

        This method returns a list of all notes currently stored in the notes collection.

        Returns:
            List[Note]: A list of all Note objects. If no notes are stored, an empty list is returned.
        """
        return self.notes

    def add_tag(self, note_id: int, tag: str) -> None:
        """
        Adds a tag to the note with the specified note_id.

        This method finds the note by its ID and adds the given tag to its tags list. The note collection is updated
        and saved after adding the tag. If the note is not found, an error message is returned.

        Args:
            note_id (int): The ID of the note to which the tag will be added.
            tag (str): The tag to add to the note.

        Returns:
            None: Prints a message indicating the result of the operation.
        """
        # Find the note by its ID
        note = self.get_note_by_id(note_id)
        if not note:
            print(format_red(f"Note with id {note_id} not found."))
            
        # Add the tag to the note's tags list if it's not already present
        if tag and tag not in note.tags:
            note.tags.append(tag)
            self.storage.save_data(self.notes)

            # Verify if the tag has been successfully added to the storage
            if self.is_note_tag_in_storage(note_id, tag):
                print(format_green(f"Tag '{tag}' has been added to the Note with id {note.title}."))
            else:
                print(
                    format_red(f"Tag '{tag}' has not been added to the Note with id {note.title} in the storage.")
                )
        elif tag in note.tags:
            print(format_red(f"Tag '{tag}' already exists for the Note with id {note.title}."))
        else:
            print(format_red("Invalid tag. Please provide a valid tag string."))
    
    def remove_tag(self, note_id: int, tag: str) -> None:
        """
        Removes a tag from the note with the specified note_id.

        This method finds the note by its ID and removes the given tag from its tags list. The note collection is updated
        and saved after removing the tag. If the note is not found, an error message is returned.

        Args:
            note_id (int): The ID of the note from which the tag will be removed.
            tag (str): The tag to remove from the note.

        Returns:
            None: Prints a message indicating the result of the operation.
        """
        note = self.get_note_by_id(note_id)
        if not note:
            print(format_red(f"Note with id {note_id} not found."))
        
        # Remove the tag if it exists
        if tag in note.tags:
            note.tags.remove(tag)
            self.storage.save_data(self.notes)

            # Verify if the tag has been successfully removed from the storage
            if not self.is_note_tag_in_storage(note_id, tag):
                print(
                    format_green(f"Tag '{tag}' has been removed from the Note with id {note.title}.")
                )
            else:
                print(
                    format_red(f"Tag '{tag}' has not been removed from the Note with id {note.title} in the storage.")
                )
        else:
            print(
                format_red(f"Tag '{tag}' not found for the Note with id {note.title}.")
            )
    
    def is_note_tag_in_storage(self, note_id: int, tag:str) -> bool:
        """Method check is tag in the data storage
        Args:
            note_id (int): The ID of the note from which the tag will be checked.
            tag (str): The tag to check.
        Returns:
            bool: True if tag is in the storage in checked Note otherwise False.
        """
        note = [note for note in self.storage.load_data() if note.id == note_id]
        if note:
            return tag in note[-1].tags
        return False
