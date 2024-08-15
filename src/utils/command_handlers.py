from typing import List
from models import contact

def display_all_contacts(self) -> None:
        """
        Displays all contacts in readable format. Shows a message if no contacts.

        """
        if not self.contacts:
            print("No contacts available.")
        else:
            print("All Contacts:")
            for contact in self.contacts:
                print (f"ID: {contact.id}, Name: {contact.name}, Address: {contact.address},"
                       f"Phone: {contact.phone_number}, Email: {contact.email}, Birthday: {contact.birthday}")
