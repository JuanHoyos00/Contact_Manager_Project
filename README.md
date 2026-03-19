# 📇 Contact Manager Project

## 📖 Project Description

**Contact Manager** is a Python command-line interface (CLI) application designed to manage contacts in a simple and efficient way.  
It allows users to add, delete, retrieve, and display contacts stored in a JSON file.

The project is built using:

- Python 3.12+
- Typer for CLI interface
- JSONStorage for persistent storage
- Modular design:
  - models
  - services
  - storage
  - exceptions

---

## 🎯 Purpose

Provide a lightweight, easy-to-use, and cross-platform tool for managing personal or small-scale contact lists.

---

## 📌 Scope

- CLI-based contact management
- JSON-based persistence
- Easily extensible architecture for future improvements

---

## 🖥️ Available Commands

Command: add-contact  
Description: Add a new contact  
Example: uv run main.py add-contact "Juan" "1" "123456789" "USA"  

Command: delete-contact-by-number  
Description: Delete a contact by phone number  
Example: uv run main.py delete-contact-by-number "123456789"  

Command: get-contact-by-number  
Description: Retrieve a contact by number  
Example: uv run main.py get-contact-by-number "123456789"  

Command: show-contacts  
Description: Display all contacts  
Example: uv run main.py show-contacts  

---

## 💡 CLI Help

You can use the --help flag to explore available commands:

uv run main.py --help  
uv run main.py add-contact --help  

---

## ⚙️ Installation Guide

Clone the repository:

git clone https://github.com/JuanHoyos00/Contact_Manager_Project.git  
cd Contact_Manager_Project  

Install dependencies:

uv sync  

Run the application:

uv run main.py --help  

---

## 🏗️ Project Structure

Contact_Manager/  
├── models.py  
├── services.py  
├── storage.py  
└── exceptions.py  

---

## 💾 Persistence

- Contacts are stored in a JSON file  
- Each contact is serialized as a dictionary  
- Data is automatically loaded and saved using JSONStorage  

---

## 🧠 Design Principles

- Separation of concerns  
- Encapsulation of validation logic  
- Layered architecture  
- Use of type hints for clarity  
- Custom exception handling  

---

## 🚀 Future Improvements

- Add support for more countries  
- Integrate a database (PostgreSQL / SQLite)  
- Build a REST API (FastAPI)  
- Add a graphical or web interface  
- Improve test coverage  

---

## 📚 Documentation

To run documentation locally:

uv run mkdocs serve  

---

## 👨‍💻 Authors

Developed by Juan Andrés Hoyos Ocampo and Jose Jiménez
