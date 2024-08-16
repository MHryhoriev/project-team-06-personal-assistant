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
                print(f"Note {note_id} successfully deleted.")
                return
        
        print(f"Note {note_id} not found.")

    def search_notes_by_tag(self, tag: str) -> List[Note]:
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
