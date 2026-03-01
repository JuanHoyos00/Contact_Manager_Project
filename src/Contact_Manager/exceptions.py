class AppError(Exception):

    ''' Base exception for the application.
    '''
    pass


class ContactError(AppError):

    ''' Base exception for contact-related errors.
    '''
    pass


class InvalidCountryError(ContactError):

    ''' Raised when the country is invalid.
    '''
    def __init__(self, country: str):
        super().__init__(f'The country {country} is invalid.')


class InvalidCountryCodeError(ContactError):

    ''' Raised when the country code is invalid.
    '''
    def __init__(self, country_code: str):
        super().__init__(f'The code {country_code} is invalid.')


class InvalidNumberDataError(ContactError):

    ''' Raised when the phone number is invalid.
    '''
    def __init__(self, number: str):
        super().__init__(f'The number {number} is invalid.')


class NotConsistencyCodeCountryError(ContactError):

    ''' Raised when country and code do not match.
    '''
    def __init__(self, country_code: str, country):
        super().__init__(f'The code {country_code} does not match with the country {country}.')


class ContactAlreadyExistError(ContactError):

    ''' Raised when the contact already exists.
    '''
    def __init__(self, number):
        super().__init__(f'The number {number} already exists.')


class ContactNotFoundError(ContactError):

    ''' Raised when the contact is not found.
    '''
    def __init__(self, number):
        super().__init__(f'The number {number} does not exist.')


class ContactListIsEmptyError(ContactError):

    ''' Raised when the contact list is empty.
    '''
    def __init__(self):
        super().__init__('There are no contacts in the contact list.')