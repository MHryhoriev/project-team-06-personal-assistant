"""The contact logic module

Task: Develop a Contact class that will represent an individual contact.

‌

Fields:

id (int): Unique contact identifier.
name (string): The name of the contact.
address (string): The residential address of the contact.
phone_number (string): The phone number of the contact. The format must be validated with a regular expression.
email (string): Email address of the contact. The format must be validated with a regular expression.
birthday (datetime.date): Date of birth of the prospect.
"""

import re
from dataclasses import dataclass, field, asdict
from typing import Optional
from datetime import date, datetime

@dataclass
class Contact:
    name: str
    address: str
    phone_number: str
    email: str
    birthday: str
    birthday: Optional[str] = field(default=None)

    def __post_init__(self):
        # Validate phone number and email after initialization
        self._validate_phone_number(self.phone_number)
        self._validate_email(self.email)

        # Validate birthday if it is provided
        if self.birthday:
            self._validate_birthday(self.birthday)

    @property
    def name(self) -> str:
        """
        Gets the contact name.

        Returns:
            str: The contact name.
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """
        Sets the contact name.

        Args:
            value (str): The contact name.
        """
        self.__name = value

    @property
    def address(self) -> str:
        """
        Gets the contact address.

        Returns:
            str: The contact address.
        """
        return self.__address

    @address.setter
    def address(self, value: str) -> None:
        """
        Sets the contact address.

        Args:
            value (str): The contact address.
        """
        self.__address = value

    @property
    def phone_number(self) -> str:
        """
        Gets the contact phone number.

        Returns:
            str: The contact phone number.
        """
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str) -> None:
        """
        Sets the contact phone number with validation.

        Args:
            value (str): The contact phone number.

        Raises:
            ValueError: If the phone number is invalid.
        """
        self._validate_phone_number(value)
        self.__phone_number = value

    @property
    def email(self) -> str:
        """
        Gets the contact email.

        Returns:
            str: The contact email.
        """
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        """
        Sets the contact email with validation.

        Args:
            value (str): The contact email.

        Raises:
            ValueError: If the email is invalid.
        """
        self._validate_email(value)
        self.__email = value

    @property
    def birthday(self) -> str:
        """
        Gets the contact birthday.

        Returns:
            str: The contact birthday.
        """
        return self.__birthday

    @birthday.setter
    def birthday(self, value: str) -> None:
        """
        Sets the contact birthday.

        Args:
            value (str): The contact birthday.
        """
        self.__birthday = value

    def _validate_phone_number(self, phone_number: str) -> None:
        """
        Validates the format of a phone number.

        This method checks if the provided phone number adheres to a specific format for Ukrainian phone numbers.
        It raises a `ValueError` if the phone number does not match the expected format.

        Args:
            phone_number (str): The phone number to be validated.

        Raises:
            ValueError: If the phone number does not conform to the expected format.
        """
        pattern = r'^(?:\+380|0)[\d]{9,12}$'  # Example pattern for Ukrainian numbers
        if not re.match(pattern, phone_number):
            raise ValueError(f"Invalid phone number: {phone_number}. Expected format: +380XXXXXXXXX or 0XXXXXXXXX")

    def _validate_email(self, email: str) -> None:
        """
        Validates the format of an email address.

        This method checks if the provided email address adheres to a standard email format. 
        It raises a `ValueError` if the email is empty or does not match the expected format.

        Args:
            email (str): The email address to be validated.

        Raises:
            ValueError: If the email address is empty or does not conform to the expected email format.
        """
        if not email:
            raise ValueError("Email address cannot be empty.")
        
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Updated pattern for email validation
        if not re.match(pattern, email):
            raise ValueError(f"Invalid email address: {email}. Expected format: example@domain.com")
    
    def _validate_birthday(self, birthday: str) -> None:
        """
        Validates the birthday field.

        This method checks if the provided birthday string is in the correct format (DD.MM.YYYY),
        converts it to a `date` object, and ensures that the birthday is not in the future. If any 
        of these conditions fail, a `ValueError` is raised.

        Args:
            birthday (str): The birthday in DD.MM.YYYY format to be validated.

        Raises:
            ValueError: If the birthday is not a valid date or if it is in the future.
        """
        try:
            birthday_date = datetime.strptime(birthday, '%d.%m.%Y').date()
        except ValueError:
            raise ValueError(f"Invalid birthday format: {birthday}. Expected format: DD.MM.YYYY")
        
        if birthday_date > date.today():
            raise ValueError("Birthday cannot be in the future.")

    def to_dict(self) -> dict:
        """
        Converts the Contact object into a dictionary.

        Returns:
            dict: A dictionary representation of the Contact object.
        """
        return asdict(self)
    
    def __str__(self) -> str:
        return f"Name: {self.__name}, Address: {self.__address}, Phone: {self.__phone_number}, Email: {self.__email}, Birthday: {self.__birthday}"