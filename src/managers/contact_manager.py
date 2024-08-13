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
        self.contacts: List[Contact] = []

    def add_contact(self, contact: Contact) -> None:
        """
        Adds a new contact to the list if it doesn't already exist.
        """
        # Check if a contact with the same name already exists
        for existing_contact in self.contacts:
            if existing_contact.name == contact.name:
                print(f"Contact with the name {contact.name} already exists.")
                return
        
        # Add the new contact
        self.contacts.append(contact)
        print(f"Contact {contact.name} successfully added.")

    def remove_contact(self, name: str) -> None:
        """
        Removes a contact from the list by name.
        """
        raise NotImplementedError("The 'remove_contact' method is not implemented.")

    def edit_contact(self, name: str, updated_contact: Contact) -> None:
        """
        Changes information about a contact.
        """
        # Find the contact by name
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                # Validate the updated phone number and email
                contact._validate_phone_number(updated_contact.phone_number)
                contact._validate_email(updated_contact.email)
                
                # Update the contact information
                self.contacts[i] = updated_contact
                print(f"Contact {name} updated successfully.")
                return
        
        print(f"Contact with the name {name} not found.")

    def search_by_name(self, name: str) -> List[Contact]:
        """
        Search for contacts by name.
        """
        return [contact for contact in self.contacts if contact.name == name]

    def search_by_email(self, email: str) -> List[Contact]:
        """
        Search for contacts by email.
        """
        return [contact for contact in self.contacts if contact.email == email]

    def search_by_phone_number(self, phone_number: str) -> List[Contact]:
        """
        Search for contacts by phone number.
        """
        return [contact for contact in self.contacts if contact.phone_number == phone_number]
