"""The Note logic implementation

Task: Develop a Note class that will represent a single note.

‌

Fields:

id (int): The unique identifier of the note.
title (string): The title of the note.
contact (Contact): An object of the Contact class with which the note is associated.
content (string): The textual content of the note.
created_at (Date): The date and time the note was created.
updated_at (Date): Date and time the note was last updated.
"""


from datetime import datetime
from dataclasses import dataclass, asdict, field
from typing import List
from models.contact import Contact  # Assume Contact class is defined in 'contact.py'

@dataclass
class Note:
    
    id: int = 0
    title: str = ""
    contact: Contact = None
    content: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    updated_at:datetime = field(default_factory=datetime.now)
    tags: List [str] = field(default_factory=list) #new field for tags

    def update_content(self, new_content: str) -> None:
        """
        Update the content of the note and set the updated_at timestamp to the current time.
        """
        self.content = new_content
        self.updated_at = datetime.now()

    def add_tag(self, tag: str) -> str:
        """
        Add a tag to a note if it does not exist yet.
        """
        if tag in self.tags:
            return f"Tag '{tag}' already exists."
        self.tags.append(tag)
        self.updated_at = datetime.now()
        return f"Tag '{tag}' added."
    
    def remove_tag(self, tag: str) ->str:
        """
        Remove a tag from the note if exists.
        """
        if tag not in self.tags:
            return f"Tag '{tag}' not found."
        self.tags.remove(tag)
        self.updated_at = datetime.now()
        return f"Tag '{tag}' removed."

    def __repr__(self) -> str:
        return str(asdict(self))
    
    def to_dict(self) -> dict:
        """
        Converts the Note object into a dictionary.

        Returns:
            dict: A dictionary representation of the Note object where keys are
                the contact attributes (e.g., 'id', 'title', 'contact', 'content', 'created_at', 'updated_at')
                and values are their respective values.
        """
        return {
            "id": self.id,
            "title": self.title,
            "contact": self.contact,
            "content": self.content,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "tags": self.tags #Include tags in dict.
        }
