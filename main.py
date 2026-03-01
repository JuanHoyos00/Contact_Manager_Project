from Contact_Manager.services import ContactManager
from Contact_Manager.storage import JSONStorage
from Contact_Manager.models import Contact
from pathlib import Path
import typer
 
app: typer = typer.Typer()
storage: JSONStorage = JSONStorage(Path('data/data.json'))
service: ContactManager = ContactManager(storage)


@app.command()
def add_contact(name: str, country_code: str, number: str, country: str) -> None:
    """Add a new contact."""
    service.add_contact(name, country_code, number, country)


@app.command()
def delete_contact_by_number(number: str) -> None:
    """Delete a contact by its number."""
    service.delete_contact_by_number(number)


@app.command()
def get_contact_by_number(number: str) -> None:
    """Display a contact's details by number."""
    contact: Contact = service.get_contact_by_number(number)
    typer.echo(contact)


@app.command()
def show_contacts() -> None:
    """Display all contacts."""
    service.show_contacts()

if __name__ == '__main__':
    app()
