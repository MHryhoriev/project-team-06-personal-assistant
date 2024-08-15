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

    def add_tag(self, note_id: int, tag: str) -> str:
        """
        Adds tag to the note with the specified note_id.
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
        """

        note = self.get_note_by_id(note_id)
        if note:
            result = note.remove_tag(tag)
            self.storage.save_data(self.notes)
            return result
        return f"Note with id {note_id} not found."