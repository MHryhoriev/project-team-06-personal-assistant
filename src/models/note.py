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
from contact import Contact  # Assume Contact class is defined in 'contact.py'
from types import Optional

class Note:
    def __init__(self, id: int, title: str, contact: Contact, content: str, created_at: Optional[datetime] = None, updated_at: Optional[datetime] = None) -> None:
        self.id: int = id
        self.title: str = title
        self.contact: Contact = contact
        self.content: str = content
        self.created_at: datetime = created_at if created_at is not None else datetime.now()
        self.updated_at: datetime = updated_at if updated_at is not None else datetime.now()

    def update_content(self, new_content: str) -> None:
        """
        Update the content of the note and set the updated_at timestamp to the current time.
        """
        self.content = new_content
        self.updated_at = datetime.now()

    def __repr__(self) -> str:
        return (f"Note(id={self.id}, title='{self.title}', contact={self.contact}, "
                f"content='{self.content}', created_at={self.created_at}, updated_at={self.updated_at})")
