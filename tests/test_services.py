from Contact_Manager.exceptions import ContactAlreadyExistError, ContactNotFoundError, ContactListIsEmptyError
from Contact_Manager.services import ContactManager
from Contact_Manager.models import Contact
from unittest.mock import MagicMock
import pytest

def test_add_contact_successfully() -> None:

    ''' Test whether a contact can be added successfully.
    '''
    
    mock_storage: MagicMock = MagicMock()
    mock_storage.load.return_value = []
    service: ContactManager = ContactManager(mock_storage)
    service.add_contact('Juan', '57', '123456789', 'COL')
    mock_storage.save.assert_called_once()

def test_contact_alredy_exist_error() -> None:
    
    ''' Raises an error when trying to add a contact that already exists.
    '''

    mock_storage: MagicMock = MagicMock()
    mock_storage.load.return_value = [Contact('Juan', '57', '123456789', 'COL')]
    service: ContactManager = ContactManager(mock_storage)
    with pytest.raises(ContactAlreadyExistError):
        service.add_contact('Juan', '57', '123456789', 'COL')

def test_delete_contact_successfully() -> None:
    
    ''' Test whether a contact can be deleted successfully.
    '''

    mock_storage: MagicMock = MagicMock()
    mock_storage.load.return_value = [Contact('Juan', '57', '123456789', 'COL')]
    service: ContactManager = ContactManager(mock_storage)
    service.delete_contact_by_number('123456789')
    mock_storage.save.assert_called_once()

def test_get_contact_by_number() -> None:

    '''Tests successful retrieval of a contact by number.
    '''

    mock_storage: MagicMock = MagicMock()
    contact: Contact = Contact('Juan', '57', '123456789', 'COL')
    mock_storage.load.return_value = [contact]
    service: ContactManager = ContactManager(mock_storage)
    assert service.get_contact_by_number('123456789') == contact
    
def test_contact_not_found_error() -> None:

    ''' Raises an error if the contact does not exist.
    '''

    mock_storage: MagicMock = MagicMock()
    mock_storage.load.return_value = []
    service: ContactManager = ContactManager(mock_storage)
    with pytest.raises(ContactNotFoundError):
        service.delete_contact_by_number('123456789')

def test_show_contatc_list_successfully() -> None:

    """
    Test that show_contacts runs successfully.
    """
    
    mock_storage: MagicMock = MagicMock()
    mock_storage.load.return_value = [Contact('Juan', '57', '123456789', 'COL')]
    service: ContactManager = ContactManager(mock_storage)
    service.show_contacts()

def test_contact_list_empty() -> None:

    ''' Raises an error if the contact list is empty.
    '''

    mock_storage: MagicMock = MagicMock()
    mock_storage.load.return_value = []
    service: ContactManager = ContactManager(mock_storage)
    with pytest.raises(ContactListIsEmptyError):
        service.show_contacts()