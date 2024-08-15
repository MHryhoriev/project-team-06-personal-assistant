"""The Note Manager logic module


"""
import re
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
        try:
            if not query.strip(): # Checking the quest
                raise ValueError("Search name cannot be empty.")
              # Searches for notes by title or content and returns a list      
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
        """
        for note in self.notes: # Sorting through the note in the list
            if note.id == note_id: # Compare note id
                note.updated_content(updated_note.content)  #Replace the found note with a new note           
                print(f"Note {note_id} updated successfully.")
                return
        
        print(f"Note with the name {note_id} not found.")
    
        raise NotImplementedError("The 'edit_note' method is not implemented.")

    def delete_note(self, note_id: int) -> None:
        """
        Deletes a note with the specified note_id.
        """
        for note in self.notes: # Sorting through the note in the list
            if note.id == note_id: # Compare note id
                self.notes.remove(note) # Delete the found note
                return
            
