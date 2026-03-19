# 🏗️ Architecture

This section describes the main design decisions behind the Contact Manager project.

---

## 📁 Project Structure

The project follows a **package-based structure**, where all the application code is organized inside a main module.

Example structure:

Contact_Manager/
├── models.py
├── services.py
├── storage.py
└── exceptions.py

### Why this structure?

- Keeps all core logic grouped in a single module
- Simplifies imports and project navigation
- Suitable for small to medium-sized applications
- Easy to understand and maintain

---

## 🧩 Layered Architecture

The application is divided into clearly defined layers, each with a specific responsibility.

---

### 📦 Models Layer

- Defines the core data structure (`Contact`)
- Handles data validation
- Uses `@dataclass` for simplicity and readability

---

### ⚙️ Services Layer

- Contains the business logic (`ContactManager`)
- Coordinates operations such as:
  - Adding contacts
  - Deleting contacts
  - Retrieving contacts
- Ensures rules like uniqueness and existence

---

### 💾 Storage Layer

- Responsible for data persistence
- Uses a `Storage` protocol to abstract implementation
- Current implementation: `JSONStorage`

---

### ⚠️ Exceptions Layer

- Defines custom exceptions for the domain
- Improves error clarity and handling
- Examples:
  - InvalidCountryError
  - ContactNotFoundError

---

## 🧠 Clean Code Principles

Several clean code principles are applied throughout the project:

---

### 🔹 Separation of Concerns

Each module has a single responsibility:

- Models → data and validation  
- Services → business logic  
- Storage → persistence  

---

### 🔹 Encapsulation

- Internal data is protected using private attributes
- Access is controlled through properties
- Validation logic is encapsulated within the model

---

### 🔹 Readability

- Clear and descriptive method names
- Consistent naming conventions
- Use of type hints for better understanding

---

### 🔹 Error Handling

- Custom exceptions are used instead of generic errors
- Errors are meaningful and domain-specific

---

### 🔹 Abstraction

- The `Storage` protocol allows changing persistence without modifying business logic
- Promotes flexibility and extensibility

---

## 📌 Summary

- The project uses a package-based structure (`Contact_Manager`)
- It follows a layered architecture
- Clean code principles improve readability, maintainability, and scalability