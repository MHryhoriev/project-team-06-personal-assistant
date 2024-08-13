"""The Note Manager logic module


"""

from typing import List
from models.note import Note  # Assume Note class is defined in 'note.py'

class NoteManager:
    def __init__(self) -> None:
        self.notes: List[Note] = []

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
