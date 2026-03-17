import json
from typing import List, Protocol
from pathlib import Path
from Contact_Manager.models import Contact


class Storage(Protocol):
    """
    Defines a protocol for storage classes that handle contact persistence.

    This protocol ensures that any storage implementation will have a consistent
    interface for loading and saving contact data.
    """

    def load(self) -> List[Contact]:
        """
        Loads and returns a list of contacts from the storage medium.

        Returns:
            List[Contact]: A list of Contact objects. If no contacts are found,
                           an empty list should be returned.
        """
        ...

    def save(self, contact_list: List[Contact]) -> None:
        """
        Saves a list of contacts to the storage medium.

        Args:
            contact_list (List[Contact]): The list of Contact objects to be saved.
        """
        ...


class JSONStorage:
    """
    A concrete storage implementation that saves contacts to a JSON file.

    This class implements the Storage protocol, handling the serialization
    and deserialization of Contact objects to and from a specified JSON file.

    Attributes:
        filepath (Path): The path to the JSON file where contacts are stored.
    """

    def __init__(self, filepath: Path):
        """
        Initializes the JSONStorage with a specific file path.

        Args:
            filepath (Path): The path object pointing to the .json file.
        """
        self.filepath = filepath

    def load(self) -> List[Contact]:
        """
        Loads contacts from the JSON file specified during initialization.

        If the file does not exist, it returns an empty list. Otherwise, it
        reads the file, deserializes the JSON data, and reconstructs a list
        of Contact objects.

        Returns:
            List[Contact]: A list of hydrated Contact objects.
        """
        if not self.filepath.exists():
            return []

        with open(self.filepath, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                # Return empty list if file is empty or malformed
                return []

        return [Contact(**item) for item in data]

    def save(self, contact_list: List[Contact]) -> None:
        """
        Saves a list of contacts to the JSON file.

        This method serializes each Contact object in the list into a dictionary
        and writes the entire list to the JSON file with human-readable indentation.

        Args:
            contact_list (List[Contact]): The list of Contact objects to save.
        """
        with open(self.filepath, "w") as f:
            # Convert each Contact object to its dictionary representation for JSON
            serializable_list = [contact.to_dict() for contact in contact_list]
            json.dump(serializable_list, f, indent=4)

