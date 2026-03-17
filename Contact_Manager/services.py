from typing import List
from rich.console import Console
from rich.table import Table

from Contact_Manager.exceptions import (
    ContactAlreadyExistError,
    ContactNotFoundError,
    ContactListIsEmptyError
)
from Contact_Manager.storage import Storage
from Contact_Manager.models import Contact

console: Console = Console()


class ContactManager:
    """
    Manages contact operations like adding, deleting, retrieving, and displaying.

    This class acts as an interface for contact-related actions, coordinating
    with a storage backend to persist contact data.

    Attributes:
        storage (Storage): The storage backend used for loading and saving contacts.
    """

    def __init__(self, storage: Storage):
        """
        Initializes the ContactManager with a specific storage backend.

        Args:
            storage (Storage): An object that conforms to the Storage interface,
                               used for persisting contact data.
        """
        self.storage: Storage = storage

    def add_contact(self, name: str, country_code: str, number: str, country: str) -> None:
        """
        Creates a new contact, validates it, and adds it to the storage.

        Loads the current contact list, ensures the new contact is unique by its
        number, appends the new contact, and saves the updated list.

        Args:
            name (str): The name of the contact.
            country_code (str): The international country code.
            number (str): The main phone number (digits only).
            country (str): The country abbreviation (e.g., 'COL', 'USA').

        Raises:
            ContactAlreadyExistError: If a contact with the same number already exists.
            (and other exceptions from Contact.__init__)
        """
        contact_list: List[Contact] = self.storage.load()
        self.validate_contact_is_unique(contact_list, number)
        contact_list.append(Contact(name, country_code, number, country))
        self.storage.save(contact_list)
        console.print(f"[bold green]\nSuccess![/bold green] Contact '{name}' added successfully!\n")

    def delete_contact_by_number(self, number: str) -> None:
        """
        Deletes a contact from storage identified by its phone number.

        Args:
            number (str): The phone number of the contact to delete.

        Raises:
            ContactNotFoundError: If no contact with the given number is found.
        """
        contact_list: List[Contact] = self.storage.load()
        self.validate_contact_exists(contact_list, number)
        # Create a new list excluding the contact to be deleted
        updated_list = [contact for contact in contact_list if contact.number != number]
        self.storage.save(updated_list)
        console.print(f"[bold green]\nSuccess![/bold green] Contact with number '{number}' has been deleted.\n")

    def get_contact_by_number(self, number: str) -> Contact:
        """
        Retrieves a single contact from storage by its phone number.

        Args:
            number (str): The phone number of the contact to retrieve.

        Returns:
            Contact: The found contact object.

        Raises:
            ContactNotFoundError: If no contact with the given number is found.
        """
        contact_list: List[Contact] = self.storage.load()
        self.validate_contact_exists(contact_list, number)
        for contact in contact_list:
            if contact.number == number:
                return contact
        # This line is technically unreachable due to the validation above,
        # but it satisfies static analysis.
        raise ContactNotFoundError(number)


    def show_contacts(self) -> None:
        """
        Displays all saved contacts in a formatted table in the console.

        Raises:
            ContactListIsEmptyError: If there are no contacts to display.
        """
        contact_list: List[Contact] = self.storage.load()
        if not contact_list:
            raise ContactListIsEmptyError()

        table: Table = Table(title='\nMY CONTACTS')
        table.add_column('Name', style='magenta')
        table.add_column('Number', style='cyan')
        table.add_column('Country', style='green')

        for contact in contact_list:
            full_number: str = f'+{contact.country_code} {contact.number}'
            table.add_row(contact.name, full_number, contact.country)

        console.print(table)

    def validate_contact_is_unique(self, contact_list: List[Contact], number: str) -> None:
        """
        Checks if a contact with the given number already exists in the list.

        Args:
            contact_list (List[Contact]): The list of contacts to check against.
            number (str): The phone number to check for uniqueness.

        Raises:
            ContactAlreadyExistError: If a contact with the same number is found.
        """
        for contact in contact_list:
            if contact.number == number:
                raise ContactAlreadyExistError(number)

    def validate_contact_exists(self, contact_list: List[Contact], number: str) -> None:
        """
        Checks if a contact with the given number exists in the list.

        Args:
            contact_list (List[Contact]): The list of contacts to search within.
            number (str): The phone number to search for.

        Raises:
            ContactNotFoundError: If no contact with the given number is found.
        """
        if not any(contact.number == number for contact in contact_list):
            raise ContactNotFoundError(number)

