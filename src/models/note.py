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

from models.contact import Contact  # Assume Contact class is defined in 'contact.py'

@dataclass
class Note:
    
    id: int = 0
    title: str = ""
    contact: Contact = None
    content: str = ""
    created_at: datetime = field(default_factory=datetime.now)
    updated_at:datetime = field(default_factory=datetime.now)

    def update_content(self, new_content: str) -> None:
        """
        Update the content of the note and set the updated_at timestamp to the current time.
        """
        self.content = new_content
        self.updated_at = datetime.now()

    def __repr__(self) -> str:
        return str(asdict(self))
