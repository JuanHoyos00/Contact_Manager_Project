from Contact_Manager.exceptions import InvalidCountryCodeError, InvalidCountryError, InvalidNumberDataError, NotConsistencyCodeCountryError


class Contact:

    ''' Represents a contact with validated phone data.
    '''

    def __init__(self, name: str, country_code: str, number: str, country: str):

        ''' Initializes a contact after validating its data.
        '''

        self.validate_country(country)
        self.validate_country_code(country_code)
        self.validate_number(number)
        self.check_consistency_between_code_and_country(country_code, country)

        self._name: str = name
        self._country_code: str = country_code
        self._number: str = number
        self._country: str = country

    def __repr__(self) -> str:

        ''' Returns a readable string representation of the contact.
        '''

        number: str = f'+{self.country_code} {self.number}'
        return f'Name: {self.name} \nNumber: {number}'

    @property
    def country_code(self) -> str:

        ''' Returns the country code.
        '''

        return self._country_code

    @property
    def name(self) -> str:

        ''' Returns the contact name.
        '''

        return self._name

    @property
    def number(self) -> str:

        ''' Returns the phone number.
        '''

        return self._number

    @property
    def country(self) -> str:

        ''' Returns the country.
        '''

        return self._country

    def to_dict(self) -> dict:

        ''' Converts the contact into a dictionary.
        '''

        return {
            "name": self.name,
            "country_code": self.country_code,
            "number": self.number,
            "country": self.country
        }

    def validate_country(self, country: str) -> bool:

        ''' Validates that the country is supported.
        '''

        if country not in ['COL', 'USA']:
            raise InvalidCountryError(country)
        return True

    def validate_country_code(self, country_code: str) -> bool:

        ''' Validates that the country code is supported.
        '''

        if country_code not in ['57', '1']:
            raise InvalidCountryCodeError(country_code)
        return True

    def validate_number(self, number: str) -> bool:

        ''' Validates that the number contains only digits.
        '''

        for digit in number:
            if not digit.isdigit():
                raise InvalidNumberDataError(number)
        return True

    def check_consistency_between_code_and_country(self, country_code: str, country: str) -> bool:

        ''' Validates that country and code match correctly.
        '''

        if (country == 'USA' and country_code == '1') or (country == 'COL' and country_code == '57'):
            return True
        raise NotConsistencyCodeCountryError(country_code, country)