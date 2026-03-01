import json
from typing import List, Protocol
from pathlib import Path
from Contact_Manager.models import Contact


class Storage(Protocol):

    ''' Protocol for storage classes handling contacts.
    '''

    def load(self, filepath: Path) -> List[Contact]:

        ''' Load contacts from a given filepath.
        '''
        ...

    def save(self, contact_list: List[Contact]) -> None:

        ''' Save contacts to the storage.
        '''
        ...


class JSONStorage:

    ''' Handles storing contacts in a JSON file.
    '''

    def __init__(self, filepath: Path):

        ''' Initializes JSON storage with the given file path.
        '''
        self.filepath = filepath

    def load(self) -> List[Contact]:

        ''' Loads contacts from the JSON file.
        '''
        if not self.filepath.exists():
            return []

        with open(self.filepath, "r") as f:
            data = json.load(f)

        return [Contact(**item) for item in data]

    def save(self, contact_list: List[Contact]) -> None:

        ''' Saves contacts to the JSON file.
        '''
        with open(self.filepath, "w") as f:
            json.dump([contact.to_dict() for contact in contact_list], f, indent=2)