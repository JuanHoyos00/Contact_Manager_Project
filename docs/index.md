# 📇 Contact Manager

## 🚀 Project Overview

**Contact Manager** is a Python-based application designed to manage phone contacts with validated international number formats.  
It provides a clean and modular architecture that ensures data integrity, separation of concerns, and extensibility.

The system allows users to create, retrieve, delete, and display contacts while enforcing strict validation rules for country codes and phone numbers.

---

## 🎯 Purpose of the Project

The main goal of this project is to:

- Provide a reliable way to manage contacts with validated data
- Enforce consistency between country codes and country identifiers
- Demonstrate clean architecture principles in Python
- Serve as a learning example of:
  - Data validation
  - Layered architecture
  - Use of `dataclasses`
  - Protocol-based design

---

## ✨ Main Features

- ✅ Add new contacts with validation
- ✅ Delete contacts by phone number
- ✅ Retrieve a contact by number
- ✅ Display contacts in a formatted table
- ✅ Automatic validation of:
  - Country (`COL`, `USA`)
  - Country codes (`57`, `1`)
  - Numeric phone numbers
- ✅ Error handling with custom exceptions
- ✅ JSON-based persistent storage

---

## 🏗️ General Architecture

The project follows a **layered architecture** with clear separation of responsibilities:

### 📦 Models Layer
- Defines the core data structure: `Contact`
- Uses `@dataclass` for simplicity and readability
- Performs validation in `__post_init__`

---

### ⚙️ Services Layer
- Contains business logic (`ContactManager`)
- Handles operations such as:
  - Adding contacts
  - Deleting contacts
  - Searching contacts
- Ensures rules like uniqueness and existence

---

### 💾 Storage Layer
- Abstracts data persistence using a `Storage` protocol
- Implements `JSONStorage` for file-based storage
- Handles serialization and deserialization of contacts

---

### ⚠️ Exceptions Layer
- Defines custom domain-specific exceptions
- Improves error clarity and debugging
- Examples:
  - `InvalidCountryError`
  - `ContactAlreadyExistError`
  - `ContactNotFoundError`

---

## 🔄 Data Flow

1. A user action triggers a method in `ContactManager`
2. The manager validates business rules
3. A `Contact` object is created and validated
4. Data is loaded/saved through the storage layer
5. Results are returned or displayed

---

## 🧠 Design Principles

- Separation of concerns
- Encapsulation of validation logic
- Use of protocols for flexibility
- Clear error handling strategy
- Readable and maintainable code structure

---

## 📌 Future Improvements

- Support for more countries and codes
- Database integration (PostgreSQL, SQLite)
- REST API layer (FastAPI)
- CLI or web interface
- Unit and integration test expansion

---

## 📖 Documentation

This documentation provides a detailed explanation of the system's components, architecture, and usage.

Use the navigation menu to explore each section in depth.
