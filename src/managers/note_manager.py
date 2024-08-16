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
          
    def validate_note(self, note: Note, min_title_length: int = 5) -> bool:
        """
        Validates the note's title and content
        """
        if not note.title or len(note.title) < min_title_length: #Number 5 is for example. Could be any number
            print(f"Error: The title must not be empty and should have at least {min_title_length} characters.")
            return False
        if not note.content:
            print("Error: The content must not be empty.")
            return False
        return True
    
    def add_note(self, note: Note) -> None:
        """
        Adds a new note to the list of notes.
        """
        #Check if the note with the same name already exists
        for existing_note in self.notes:
            if existing_note.title.lower() == note.title.lower():
                print(f"Error: A note with the same '{note.title}' already exists")
                return
            
        #Add the new note to the list
        self.notes.append(note)
        print(f"Success: Note titled '{note.title}' successfully added.")

   
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
