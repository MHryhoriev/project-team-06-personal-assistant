"""The Contact Manager logic implementation

Task: Develop a ContactManager class that will be responsible for managing all contacts.


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

import re
from storage import ContactStorage
from datetime import datetime, timedelta, date
from typing import List
from models import Contact


class ContactManager:
    def __init__(self, storage: ContactStorage) -> None:
        """
        Initializes the ContactManager with a ContactStorage instance.

        Args:
            storage (ContactStorage): An instance of ContactStorage for managing contact data.
        """
        self.storage = storage
        self.contacts: List[Contact] = self.storage.load_data()

    def add_contact(self, contact: Contact) -> None:
        """
        Adds a new contact to the list if it doesn't already exist and saves the updated list to the storage.

        This method performs the following steps:
        1. Checks if there is already a contact with the same name in the current list.
        2. If a contact with the same name is found, prints an error message and does not add the new contact.
        3. If no contact with the same name exists, adds the new contact to the list.
        4. Updates the stored data by saving the updated list of contacts to the storage.

        Parameters:
            contact (Contact): The contact to be added to the list. Must be an instance of the Contact class.
        
        Returns:
            None
        """

        # Check if contact with the same name already exists
        if self.contacts:
            for existing_contact in self.contacts:
                if existing_contact.name == contact.name:
                    print(f"Contact with the name '{contact.name}' already exists.")
                    return
        
        # Add the new contact to the list
        self.contacts.append(contact)
        self.storage.save_data(self.contacts)
        print(f"Contact '{contact.name}' successfully added.")
        
    def remove_contact(self, name: str) -> None:
        """
        Removes a contact from the list by name.
        """
        for contact in self.contacts: # Sorting through the contacts in the list
            if contact.name == name: # Compare contacts
                self.contacts.remove(contact) # The found contact is deleted
                print(f"Contact {name} successfully deleted.")
                return

        print(f"Contact {name} not found.")

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
                self.storage.save_data(self.contacts)
                print(f"Contact {name} updated successfully.")
                return
        
        print(f"Contact with the name {name} not found.")

    def search_by_name(self, name: str) -> List[Contact]:
        """
        Searches for contacts by name or part of the name.

        Parameters:
            name (str): The name or part of the name to search for.

        Returns:
            List[Contact]: A list of contacts that match the search query.

        Raises:
            ValueError: If the name parameter is empty.
            RuntimeError: If there is an unexpected error during the search.
        """
        try:
            if not name.strip():
                raise ValueError("Search name cannot be empty.")
            
            pattern = re.compile(re.escape(name), re.IGNORECASE)
            matching_contacts = [contact for contact in self.contacts if pattern.search(contact.name)]
            
            return matching_contacts # A list of notes s that match the search query.
        
        except re.error as e:
            raise RuntimeError(f"An error occurred while processing the search pattern: {e}")
        
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred during the search: {e}")

    def search_by_email(self, email: str) -> List[Contact]:
        """
        Search for contacts by email.
        """
        matching_contacts = []
        #search for contacts with matching email
        for contact in self.contacts:
            if email in contact.email:
                matching_contacts.append(contact)
        # retrun the list of matching contacts        
        return matching_contacts

    def search_by_phone_number(self, phone_number: str) -> List[Contact]:
        """
        Search for contacts by phone number (exact or partial match).

        Parameters:
        - contacts (list of dict): A list of contacts, where each contact is represented by a dictionary with 'name' and 'phone' keys.
        - phone_number (str): The phone number or part of the phone number to be searched.

        Returns:
        - list of dict: A list of contacts whose phone numbers match the search query.
        """
        # Initialize an empty list to hold matching contacts
        matching_contacts = []

        # Iterate over each contact in the contacts list
        if self.contacts: # Skip if list is empty
            for contact in self.contacts:
                # Check if the phone number part of the contact matches the search query
                if str(phone_number) in contact.phone_number:
                    matching_contacts.append(contact)

        return matching_contacts
    
    def get_all_contacts(self) -> List[Contact]:
        return self.contacts

    def get_upcoming_birthdays(self, n_day: int=7) -> List:
        """
        A list of birthdays for a specified period of time
        """
        res = [] # Create an empty list
        if self.contacts: 
            to_date = date.today() # Let's find out what day it is today
            for contact in self.contacts: # We go through the contacts and pike up birthdays, transferring the day to the desired format
                birthday = datetime.strptime(contact.birthday, "%d.%m.%Y").replace(year=to_date.year).date()
                if birthday < to_date: # Check if the date of birth has passed
                    birthday = birthday.replace(year=to_date.year+1) #
                if to_date <= birthday <= (to_date + timedelta(days=n_day)): # Check if the date of birth falls within a given period of days
                    res.append(f"name: {contact.name}, congratulation_date: {birthday.strftime('%d.%m.%Y')}\n") # Add the found date
        return res # Return the list of birthdays
