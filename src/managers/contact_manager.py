"""The Contact Manager logic implementation

Task: Develop a ContactManager class that will be responsible for managing all contacts.

‌

Fields:

contacts (List[Contact]): A list of Contact objects.
‌

Methods (without implementation):

add_contact(contact: Contact): Adds a new contact to the list.
remove_contact(name: str): Removes a contact from the list by name.
edit_contact(name: str, updated_contact: Contact): Changes information about a contact.
search_by_name(name: str): Search for contacts by name.
search_by_email(email: str): Search for prospects by email.
search_by_phone_number(phone_number: str): Search for contacts by phone number.
"""

from typing import List
from models import Contact  # Assume Contact class is defined in 'contact.py'

class ContactManager:
    def __init__(self) -> None:
        # Initialize an empty list of contacts
        self.contacts: List[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        """
        Adds a new contact to the list.
        """
        # Check if contact with the same name already exists
        for existing_contact in self.contacts:
            if existing_contact.name == contact.name:
                print(f"Contact with the name '{contact.name}' already exists.")
                return
        
        # Add the new contact to the list
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' successfully added.")

    def remove_contact(self, name: str) -> None:
        """
        Removes a contact from the list by name.
        """
        for existing_contact in self.contacts:
            if existing_contact.name == name:
                self.contacts.remove(name)
            else:
                print("The 'remove_contact' method is not implemented.")
 

    def edit_contact(self, name: str, updated_contact: Contact) -> None:
        """
        Changes information about a contact.
        """
        raise NotImplementedError("The 'edit_contact' method is not implemented.")

    def search_by_name(self, name: str) -> List[Contact]:
        """
        Search for contacts by name.
        """
        raise NotImplementedError("The 'search_by_name' method is not implemented.")

    def search_by_email(self, email: str) -> List[Contact]:
        """
        Search for contacts by email.
        """
        raise NotImplementedError("The 'search_by_email' method is not implemented.")

    def search_by_phone_number(self, phone_number: str) -> List[Contact]:
        """
        Search for contacts by phone number.
        """
        raise NotImplementedError("The 'search_by_phone_number' method is not implemented.")
