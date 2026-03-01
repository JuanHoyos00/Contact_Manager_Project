from Contact_Manager.exceptions import ContactAlreadyExistError, ContactNotFoundError, ContactListIsEmptyError
from Contact_Manager.storage import Storage
from Contact_Manager.models import Contact
from rich.console import Console
from rich.table import Table
from typing import List

console: Console = Console()


class ContactManager:

    ''' Manages contacts with add, delete, get and display operations.
    '''

    def __init__(self, storage: Storage):
        self.storage: Storage = storage
    
    def add_contact(self, name: str, country_code: str, number: str, country: str) -> None:

        ''' Add a contact to the contact manager.
        '''

        contact_list: List[Contact] = self.storage.load()            
        self.validate_contact_is_unique(contact_list, number)
        contact_list.append(Contact(name, country_code, number, country))
        self.storage.save(contact_list)
        console.print(f"[bold green]\nSuccess![/bold green] contact {name} added successfully!\n")
    
    def delete_contact_by_number(self, number: str) -> None:

        ''' Delete a contact from the contact manager.
        '''
        
        contact_list: List[Contact] = self.storage.load()
        self.validate_contact_exists(contact_list, number)
        contact_list = [contact for contact in contact_list if contact.number != number]
        self.storage.save(contact_list)
        console.print(f"[bold green]\nSuccess![/bold green] Contact whit number: {number} has been deleted successfully!\n")
    
    def get_contact_by_number(self, number: str) -> Contact:

        ''' Get a contact by its numuber.
        '''
        
        contact_list: List[Contact] = self.storage.load()
        self.validate_contact_exists(contact_list, number)
        for contact in contact_list:
            if contact.number == number:
                console.print(f"[bold green]\n{contact}[/bold green]\n")
        return contact
    
    def show_contacts(self) -> None:

        ''' Show the whole contacts on a board.
        '''
        
        table: Table = Table(title = '\nMY CONTACTS')

        table.add_column('Name', style = 'magenta')
        table.add_column('Number', style = 'cyan')
        table.add_column('Country', style = 'green')

        contact_list: List[Contact] = self.storage.load()
        if len(contact_list) == 0:
            raise ContactListIsEmptyError()
        for contact in contact_list:
            number: str = f'+{contact.country_code} {contact.number}'
            table.add_row(contact.name, number, contact.country)
        
        console.print(table)
    
    def validate_contact_is_unique(self, contact_list: List[Contact], number: str) -> None:

        ''' Validate that a contact is unique.
        '''
        
        for contact in contact_list:
                if contact.number == number:
                    raise ContactAlreadyExistError(number)
    
    def validate_contact_exists(self, contact_list: List[Contact], number: str) -> None:

        ''' Validate that a contact exists in storage.
        '''
        
        if not any(contact.number == number for contact in contact_list):
            raise ContactNotFoundError(number)