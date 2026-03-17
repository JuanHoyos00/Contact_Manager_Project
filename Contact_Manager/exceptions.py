class AppError(Exception):
    """Base exception for all custom application errors."""
    pass


class ContactError(AppError):
    """Base exception for errors related to contact management."""
    pass


class InvalidCountryError(ContactError):
    """
    Raised when an invalid or unsupported country is provided.

    Attributes:
        country (str): The name of the country that caused the error.
    """
    def __init__(self, country: str):
        super().__init__(f'The country {country} is invalid.')


class InvalidCountryCodeError(ContactError):
    """
    Raised when the provided country code is invalid.

    Attributes:
        country_code (str): The country code that caused the error.
    """
    def __init__(self, country_code: str):
        super().__init__(f'The code {country_code} is invalid.')


class InvalidNumberDataError(ContactError):
    """
    Raised when the data for a phone number is invalid.

    Attributes:
        number (str): The phone number that was considered invalid.
    """
    def __init__(self, number: str):
        super().__init__(f'The number {number} is invalid.')


class NotConsistencyCodeCountryError(ContactError):
    """
    Raised when the country code and the country do not match.

    Attributes:
        country_code (str): The provided country code.
        country (str): The provided country.
    """
    def __init__(self, country_code: str, country: str):
        super().__init__(f'The code {country_code} does not match the country {country}.')


class ContactAlreadyExistError(ContactError):
    """
    Raised when attempting to create a contact that already exists.

    Attributes:
        number (str): The number of the contact that already exists.
    """
    def __init__(self, number: str):
        super().__init__(f'The number {number} already exists.')


class ContactNotFoundError(ContactError):
    """
    Raised when a searched contact is not found.

    Attributes:
        number (str): The number of the contact that was not found.
    """
    def __init__(self, number: str):
        super().__init__(f'The number {number} does not exist.')


class ContactListIsEmptyError(ContactError):
    """Raised when an operation is attempted on an empty contact list."""
    def __init__(self):
        super().__init__('There are no contacts in the contact list.')

