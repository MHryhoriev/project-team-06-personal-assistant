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
    contact: Contact.name = ""
    content: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    updated_at:datetime = field(default_factory=datetime.now)
    tags: List [str] = field(default_factory=list) #new field for tags
    
    def __repr__(self) -> str:
        return str(asdict(self))
    
        # Temporary solution
    def __str__(self) -> str:
        return f"ID: {self.id}, Title: {self.title}, Contact: {self.contact}, Content: {self.content}, Created_at: {self.created_at}, Updated_at: {self.updated_at}"
    
    def update_content(self, new_content: str) -> None:
        """
        Update the content of the note and set the updated_at timestamp to the current time.
        """
        self.content = new_content
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """
        Converts the Note object into a dictionary.

        Returns:
            dict: A dictionary representation of the Note object where keys are
                the contact attributes (e.g., 'id', 'title', 'contact', 'content', 'created_at', 'updated_at')
                and values are their respective values.
        """
        return asdict(self)

    def add_tag(self, tag: str) -> bool:
        """The method adds the tag to instance tags list

        Args:
            tag (str): The tag name.
            
        Returns:
            bool: True if self.tags has new tags otherwise False
        """
        if tag and tag not in self.tags:
            self.tags.append(tag)
            return tag in self.tags
        return False
    
    
    def delete_tag(self, tag: str) -> bool:
        """The method deletes the tag from the instance tags list

        Args:
            tag (str): The tag name.
            
        Returns:
            bool: True if self.tags has new tags otherwise False
        """
        if tag in self.tags:
            index = self.tags.index(tag)
            del self.tags[index]
            return tag in self.tags
        return False
