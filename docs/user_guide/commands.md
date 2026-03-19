# 🖥️ CLI Commands

This section explains how to use the Contact Manager command-line interface (CLI).

---

## ▶️ Run the application

To see the available commands:

uv run main.py --help

---

## ➕ Add a contact

Command:

uv run main.py add-contact --name "Juan" --country-code 57 --number 123456789 --country COL

Parameters:

--name → Contact name  
--country-code → Country code (e.g., 57, 1)  
--number → Phone number (digits only)  
--country → Country (COL, USA)  

Example output:

Success! Contact 'Juan' added successfully!

---

## 🔍 Get a contact

Command:

uv run main.py get-contact-by-number --number 123456789

Parameters:

--number → Contact number to search  

Example output:

Name: Juan  
Number: +57 123456789  

---

## ❌ Delete a contact

Command:

uv run main.py delete-contact-by-number --number 123456789

Parameters:

--number → Contact number to delete  

Example output:

Success! Contact with number '123456789' has been deleted.

---

## 📋 Show all contacts

Command:

uv run main.py show-contacts

Example output:

MY CONTACTS

Name     Number           Country  
Juan     +57 123456789    COL  

---

## ⚠️ Error handling

Some common errors:

Duplicate number:

The number 123456789 already exists.

Contact not found:

The number 123456789 does not exist.

Invalid country:

The country XYZ is invalid.

---

## 📌 Notes

- All commands are executed using `uv run`
- Data is stored in a JSON file
- Phone numbers must contain only digits
- Supported countries are: COL, USA