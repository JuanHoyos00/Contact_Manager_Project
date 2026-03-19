from dataclasses import dataclass
from Contact_Manager.exceptions import (
    InvalidCountryCodeError,
    InvalidCountryError,
    InvalidNumberDataError,
    NotConsistencyCodeCountryError
)

@dataclass
class Contact:
    """
    Represents a phone contact with a name and validated phone number details.

    The contact's data (country, country code, and number) is validated
    upon instantiation to ensure its integrity.

    Attributes:
        _name (str): The name of the contact.
        _country_code (str): The international country code for the phone number.
        _number (str): The main part of the phone number.
        _country (str): The country associated with the phone number.
    """

    _name: str
    _country_code: str
    _number: str
    _country: str

    def __post_init__(self) -> None:
        """
        Performs validation after the dataclass is initialized.
        """
        self._validate_country(self._country)
        self._validate_country_code(self._country_code)
        self._validate_number(self._number)
        self._check_consistency_between_code_and_country(
            self._country_code, self._country
        )

    def __repr__(self) -> str:
        """
        Provides a human-readable string representation of the contact.

        Returns:
            str: A string displaying the contact's name and full phone number.
        """
        number: str = f'+{self.country_code} {self.number}'
        return f'Name: {self.name} \nNumber: {number}'

    @property
    def name(self) -> str:
        """Gets the contact's name."""
        return self._name

    @property
    def country_code(self) -> str:
        """Gets the contact's country code."""
        return self._country_code

    @property
    def number(self) -> str:
        """Gets the contact's phone number."""
        return self._number

    @property
    def country(self) -> str:
        """Gets the contact's country."""
        return self._country

    def to_dict(self) -> dict:
        """
        Serializes the contact object into a dictionary.

        Returns:
            dict: A dictionary containing the contact's details.
        """
        return {
            "name": self.name,
            "country_code": self.country_code,
            "number": self.number,
            "country": self.country
        }

    def _validate_country(self, country: str) -> bool:
        """
        Validates that the country is in the list of supported countries.

        Args:
            country (str): The country abbreviation to validate.

        Returns:
            True if the country is valid.

        Raises:
            InvalidCountryError: If the country is not in ['COL', 'USA'].
        """
        if country not in ['COL', 'USA']:
            raise InvalidCountryError(country)
        return True

    def _validate_country_code(self, country_code: str) -> bool:
        """
        Validates that the country code is in the list of supported codes.

        Args:
            country_code (str): The country code to validate.

        Returns:
            True if the country code is valid.

        Raises:
            InvalidCountryCodeError: If the country code is not in ['57', '1'].
        """
        if country_code not in ['57', '1']:
            raise InvalidCountryCodeError(country_code)
        return True

    def _validate_number(self, number: str) -> bool:
        """
        Validates that the phone number string contains only digits.

        Args:
            number (str): The phone number string to validate.

        Returns:
            True if the number contains only digits.

        Raises:
            InvalidNumberDataError: If any character in the number is not a digit.
        """
        if not number.isdigit():
            raise InvalidNumberDataError(number)
        return True

    def _check_consistency_between_code_and_country(self, country_code: str, country: str) -> bool:
        """
        Validates that the country code and country abbreviation are a valid pair.

        Args:
            country_code (str): The country code.
            country (str): The country abbreviation.

        Returns:
            True if the pair is consistent.

        Raises:
            NotConsistencyCodeCountryError: If the code and country do not match
                                            (e.g., 'USA' with '57').
        """
        if (country == 'USA' and country_code == '1') or \
           (country == 'COL' and country_code == '57'):
            return True
        raise NotConsistencyCodeCountryError(country_code, country)
