# 💾 Persistence Layer

This section explains how the persistence layer works in the Contact Manager application.

---

## 📄 JSON File Storage

The application uses a JSON file to store all contacts persistently.

- Data is saved locally in a file
- If the file does not exist, it is created automatically
- If the file is empty or corrupted, the system safely returns an empty list

This approach makes the application simple and easy to use without requiring a database.

---

## 🗂️ Data Structure

Contacts are stored as a list of dictionaries in the JSON file.

Example:

[
  {
    "name": "Juan",
    "country_code": "57",
    "number": "123456789",
    "country": "COL"
  },
  {
    "name": "Alice",
    "country_code": "1",
    "number": "987654321",
    "country": "USA"
  }
]

Each object represents a contact with its corresponding attributes.

---

## 🔄 Model Serialization

The application uses a `Contact` model to represent each contact.

### Serialization (object → JSON)

Before saving data, each `Contact` object is converted into a dictionary using:

contact.to_dict()

This produces a structure compatible with JSON:

{
  "name": "Juan",
  "country_code": "57",
  "number": "123456789",
  "country": "COL"
}

Then, all contacts are written to the file using JSON formatting.

---

### Deserialization (JSON → object)

When loading data:

- The JSON file is read
- Each dictionary is converted back into a `Contact` object

This is done using:

Contact(**item)

This reconstructs the object while automatically validating the data through the model logic.

---

## ⚙️ Storage Abstraction

The system uses a `Storage` protocol to define how data should be handled.

This allows different storage implementations (e.g., JSON, database) without changing the business logic.

Current implementation:

- JSONStorage → handles reading and writing JSON files

---

## 📌 Summary

- Data is stored in a JSON file
- Contacts are saved as dictionaries
- Models are serialized with `to_dict()`
- Data is reconstructed using `Contact(**data)`
- The storage layer is abstracted using a protocol