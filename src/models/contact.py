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


class Contact:
    def __init__(self, id: int = 0, name: str = '', address: str = '',
        phone_number: str = '', email: str = '', birthday: str = '') -> None:
        self.__id: int = id
        self.__name: str = name
        self.__address: str = address
        self.__phone_number: str = phone_number
        self.__email: str = email
        self.__birthday: str = birthday
    
    # Getter and setter for id
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        self.__id = value

    # Getter and setter for name
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    # Getter and setter for address
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str) -> None:
        self.__address = value

    # Getter and setter for phone_number
    @property
    def phone_number(self) -> str:
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value: str) -> None:
        self.__phone_number = value

    # Getter and setter for email
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        self.__email = value

    # Getter and setter for birthday
    @property
    def birthday(self) -> str:
        return self.__birthday

    @birthday.setter
    def birthday(self, value: str) -> None:
        self.__birthday = value
