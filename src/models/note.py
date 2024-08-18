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
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __repr__(self) -> str:
        return str(asdict(self))

        # Temporary solution

    def __str__(self) -> str:
        return f"ID: {self.id}, Title: {self.title}, Contact: {self.contact}, Content: {self.content}, Created_at: {self.created_at}, Updated_at: {self.updated_at}, Tags: {self.tags}"

    def update_content_and_tag(self, new_content: str, new_tags: List[str]) -> None:
        """
        Updates the content and tags of the note and sets the updated_at timestamp to the current time.

        This method modifies the note's content and tags based on the provided values. If `new_content`
        is provided, it updates the note's content with the new content. If `new_tags` is provided, it
        updates the note's tags with the new tags. After updating the content and tags, the method updates
        the `updated_at` timestamp to the current date and time to reflect the modification.

        Args:
            new_content (str): The new content to update in the note. If an empty string is provided, the content will not be changed.
            new_tags (List[str]): A list of new tags to set for the note. If an empty list is provided, the tags will not be changed.

        Returns:
            None: This method does not return any value. It modifies the note object in place.
        """
        if new_content:
            self.content = new_content
        if new_tags:
            self.tags = new_tags
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        """
        Converts the Note object into a dictionary.

        This method serializes the Note object into a dictionary format, converting datetime fields into ISO format strings and including all fields such as 'id', 'title', 'contact', 'content', 'created_at', 'updated_at', and 'tags'.

        Returns:
            dict: A dictionary representation of the Note object, where keys are:
                - 'id': The unique identifier of the note (int).
                - 'title': The title of the note (str).
                - 'contact': The contact associated with the note (str).
                - 'content': The content of the note (str).
                - 'created_at': The creation timestamp of the note, serialized to ISO format if it's a datetime object (str or datetime).
                - 'updated_at': The last update timestamp of the note, serialized to ISO format if it's a datetime object (str or datetime).
                - 'tags': A list of tags associated with the note (List[str]).
        """
        note_dict = asdict(self)

        note_dict["created_at"] = (
            self.created_at.isoformat()
            if isinstance(self.created_at, datetime)
            else self.created_at
        )
        note_dict["updated_at"] = (
            self.updated_at.isoformat()
            if isinstance(self.updated_at, datetime)
            else self.updated_at
        )

        return note_dict
