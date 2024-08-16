"""The Note Manager logic module


"""
import re
from typing import List
from models import Note
from storage import NoteStorage

class NoteManager:
    def __init__(self, storage: NoteStorage) -> None:
        """
        Initializes the NoteManager with a NoteStorage instance.

        Args:
            storage (NoteStorage): An instance of NoteStorage for managing note data.
        """
        self.storage = storage
        self.notes: List[Note] = self.storage.load_data()
          
    def validate_note(self, note: Note, min_title_length: int = 5) -> bool:
        """
        Validates the title and content of a Note object.

        This method checks whether the note's title meets the minimum length requirement and ensures that the content is not empty.

        Args:
            note (Note): The Note object to be validated.
            min_title_length (int, optional): The minimum length required for the title. Default is 5 characters.

        Returns:
            bool: True if the note is valid (title and content meet the requirements), False otherwise.
        """
        if not note.title or len(note.title) < min_title_length:
            print(f"Error: The title must not be empty and should have at least {min_title_length} characters.")
            return False
        if not note.content:
            print("Error: The content must not be empty.")
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
                print(f"Error: A note with the same '{note.title}' already exists")
                return
            
        self.notes.append(note)
        print(f"Success: Note titled '{note.title}' successfully added.")

   
    def search_notes(self, query: str) -> List[Note]:
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
                raise ValueError("Search name cannot be empty.")

            pattern = re.compile(re.escape(query), re.IGNORECASE)
            matching_notes = [note for note in self.notes if pattern.search(note.title)]
                    
            return matching_notes 
                
        except re.error as e:
                raise RuntimeError(f"An error occurred while processing the search pattern: {e}")
        except Exception as e:
                raise RuntimeError(f"An unexpected error occurred during the search: {e}")


    def edit_note(self, note_id: int, updated_note: Note) -> None:
        """
        Updates a note with the specified note_id with new data.

        This method searches through the list of notes and updates the content of the note 
        that matches the provided note_id. If the note is found, its content is updated and 
        a success message is displayed. If no note with the specified ID is found, an error 
        message is displayed.

        Args:
            note_id (int): The ID of the note to be updated.
            updated_note (Note): A Note object containing the updated content.

        Raises:
            NotImplementedError: If the note with the specified ID is not found.
        """
        for note in self.notes:
            if note.id == note_id:
                note.updated_content(updated_note.content)
                print(f"Note {note_id} updated successfully.")
                return
        
        print(f"Note with the name {note_id} not found.")

    def delete_note(self, note_id: int) -> None:
        """
        Deletes a note with the specified note_id from the list of notes.

        This method iterates through the list of notes and removes the note that matches
        the provided note_id. If the note is found, it is deleted and a success message 
        is displayed. If no note with the specified ID is found, an error message is displayed.

        Args:
            note_id (int): The ID of the note to be deleted.
        """
        for note in self.notes: # Sorting through the note in the list
            if note.id == note_id: # Compare note id
                self.notes.remove(note) # Delete the found note
                print(f"Note {note_id} successfully deleted.")
                return
        
        print(f"Note {note_id} not found.")

    def search_notes_by_tag(self, tag: str) -> List[Note]:
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
            raise ValueError("Tag cannot be empty or whitespace.")

        return [note for note in self.notes if tag in note.tags]

    def sort_notes_by_tags(self, order: str = 'asc') -> List[Note]:
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
            raise ValueError("Order must be 'asc' or 'desc'")
        
        if order == 'asc':
            sorted_notes = sorted(
                self.notes, 
                key=lambda note: (len(note.tags), sorted(note.tags))
            )
        else:
            sorted_notes = sorted(
                self.notes, 
                key=lambda note: (len(note.tags), sorted(note.tags)),
                reverse=True
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
      
    def add_tag(self, note_id: int, tag: str) -> str:
        """
        Adds a tag to the note with the specified note_id.

        This method finds the note by its ID and adds the given tag to it. If the note is found and the tag is successfully added,
        the note collection is updated and saved. If the note is not found, an error message is returned.

        Args:
            note_id (int): The ID of the note to which the tag will be added.
            tag (str): The tag to add to the note.

        Returns:
            str: A message indicating the result of the operation. If the note is found and the tag is added, a success message is returned.
                If the note is not found, an error message is returned.
        """
        note = self.get_note_by_id(note_id)
        if note:
            result = note.add_tag(tag)
            self.storage.save_data(self.notes)
            return result
        return f"Note with id {note_id} not found."
    
    def remove_tag (self, note_id: int, tag: str) -> str:
        """
        Removes a tag from the note with the specified note_id.

        This method finds the note by its ID and removes the given tag from it. If the note is found and the tag is successfully removed,
        the note collection is updated and saved. If the note is not found, an error message is returned.

        Args:
            note_id (int): The ID of the note from which the tag will be removed.
            tag (str): The tag to remove from the note.

        Returns:
            str: A message indicating the result of the operation. If the note is found and the tag is removed, a success message is returned.
                If the note is not found, an error message is returned.
        """
        note = self.get_note_by_id(note_id)
        if note:
            result = note.remove_tag(tag)
            self.storage.save_data(self.notes)
            return result
        return f"Note with id {note_id} not found."