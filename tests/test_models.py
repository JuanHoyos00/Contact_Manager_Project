from Contact_Manager.exceptions import InvalidCountryCodeError, InvalidCountryError, InvalidNumberDataError, NotConsistencyCodeCountryError
from Contact_Manager.models import Contact
import pytest 

def test_contact_creation_valid() -> None:

    ''' Test that the contact is created successfully.
    '''
    
    contact: Contact = Contact('Juan', '57', '123456789', 'COL')
    assert contact.name == "Juan"
    assert contact.country_code == "57"
    assert contact.number == "123456789"
    assert contact.country == "COL"

def test_invalid_country() -> None:

    """ Raises an error when phone number contains non-numeric characters.
    """

    with pytest.raises(InvalidCountryError):
        Contact('Juan', '1', '12345', 'MED')

def test_invalid_country_code() -> None:

    ''' Raises an error when country code is invalid.
    '''

    with pytest.raises(InvalidCountryCodeError):
        Contact('Juan', '12', '12345', 'USA')

def test_inconsistency_between_code_and_country() -> None:
    
    ''' Raises an error when there is an inconsistency between the code and the country.
    '''

    with pytest.raises(NotConsistencyCodeCountryError):
        Contact('Juan', '1', '123456789', 'COL')

def test_invalid_number() -> None:
    
    ''' Raises an error when the number is invalid.
    '''

    with pytest.raises(InvalidNumberDataError):
        Contact('Juan', '1', '123e56789', 'USA')