"""The Note Manager logic module


"""

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

    def add_note(self, note: Note) -> None:
        """
        Adds a new note to the list of notes.
        """
        raise NotImplementedError("The 'add_note' method is not implemented.")

    def search_notes(self, query: str) -> List[Note]:
        """
        Searches for notes by title or content and returns a list of matching notes.
        """
        raise NotImplementedError("The 'search_notes' method is not implemented.")

    def edit_note(self, note_id: int, updated_note: Note) -> None:
        """
        Updates a note with the specified note_id with new data.
        """
        raise NotImplementedError("The 'edit_note' method is not implemented.")

    def delete_note(self, note_id: int) -> None:
        """
        Deletes a note with the specified note_id.
        """
        raise NotImplementedError("The 'delete_note' method is not implemented.")

    def search_by_tag(self, tag: str) -> List[Note]:
        """
        Search the Note by it`s tags.

        Args:
            tag (str): A tag name to search Notes.
            
        Returns:
            List[Note]: A list of notes that contain the specified tag.

        """
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
