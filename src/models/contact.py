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

class Contact:
    def __init__(self, id: int = 0, name: str = '', address: str = '',
                 phone_number: str = '', email: str = '', birthday: str = '') -> None:
        self.__id: int = id
        self.__name: str = name
        self.__address: str = address
        self.__phone_number: str = phone_number
        self.__email: str = email
        self.__birthday: str = birthday
        
        # Validate phone number and email
        self._validate_phone_number(phone_number)
        self._validate_email(email)

    @property
    def id(self) -> int:
        """
        Gets the contact ID.

        Returns:
            int: The contact ID.
        """
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        """
        Sets the contact ID.

        Args:
            value (int): The contact ID.
        """
        self.__id = value

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


    def to_dict(self) -> dict:
        """
        Converts the Contact object into a dictionary.

        Returns:
            dict: A dictionary representation of the Contact object where keys are
                the contact attributes (e.g., 'name', 'address', 'phone_number', 'email', 'birthday')
                and values are their respective values.
        """
        return {
            "name": self.name,
            "address": self.address,
            "phone_number": self.phone_number,
            "email": self.email,
            "birthday": self.birthday
        }
    
    def __str__(self) -> str:
        return f"Name: {self.__name}, Address: {self.__address}, Phone: {self.__phone_number}, Email: {self.__email}, Birthday: {self.__birthday}"