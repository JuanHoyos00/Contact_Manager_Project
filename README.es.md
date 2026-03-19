# 📇 Proyecto Contact Manager

## 📖 Descripción del Proyecto

**Contact Manager** es una aplicación de línea de comandos (CLI) en Python diseñada para gestionar contactos de manera simple y eficiente.  
Permite agregar, eliminar, consultar y mostrar contactos almacenados en un archivo JSON.

El proyecto está construido con:

- Python 3.12+
- Typer para la interfaz de línea de comandos
- JSONStorage para almacenamiento persistente
- Diseño modular:
  - models
  - services
  - storage
  - exceptions

---

## 🎯 Propósito

Brindar una herramienta ligera, fácil de usar y multiplataforma para la gestión de contactos personales o de pequeños equipos.

---

## 📌 Alcance

- Gestión de contactos mediante CLI
- Persistencia basada en JSON
- Arquitectura fácilmente extensible para futuras mejoras

---

## 🖥️ Comandos Disponibles

Comando: add-contact  
Descripción: Agrega un nuevo contacto  
Ejemplo: uv run main.py add-contact "Juan" "1" "123456789" "USA"  

Comando: delete-contact-by-number  
Descripción: Elimina un contacto por número de teléfono  
Ejemplo: uv run main.py delete-contact-by-number "123456789"  

Comando: get-contact-by-number  
Descripción: Consulta un contacto por número  
Ejemplo: uv run main.py get-contact-by-number "123456789"  

Comando: show-contacts  
Descripción: Muestra todos los contactos  
Ejemplo: uv run main.py show-contacts  

---

## 💡 Ayuda de la CLI

Puedes usar la opción --help para ver más detalles:

uv run main.py --help  
uv run main.py add-contact --help  

---

## ⚙️ Guía de Instalación

Clonar el repositorio:

git clone https://github.com/JuanHoyos00/Contact_Manager_Project.git  
cd Contact_Manager_Project  

Instalar dependencias:

uv sync  

Ejecutar la aplicación:

uv run main.py --help  

---

## 🏗️ Estructura del Proyecto

Contact_Manager/  
├── models.py  
├── services.py  
├── storage.py  
└── exceptions.py  

---

## 💾 Persistencia

- Los contactos se almacenan en un archivo JSON  
- Cada contacto se serializa como un diccionario  
- Los datos se cargan y guardan automáticamente mediante JSONStorage  

---

## 🧠 Principios de Diseño

- Separación de responsabilidades  
- Encapsulación de la lógica de validación  
- Arquitectura por capas  
- Uso de type hints para mayor claridad  
- Manejo de errores mediante excepciones personalizadas  

---

## 🚀 Mejoras Futuras

- Soporte para más países  
- Integración con base de datos (PostgreSQL / SQLite)  
- Creación de una API REST (FastAPI)  
- Interfaz gráfica o web  
- Mejora de cobertura de pruebas  

---

## 📚 Documentación

Para ejecutar la documentación localmente:

uv run mkdocs serve  

---

## 👨‍💻 Autores

Desarrollado por Juan Andrés Hoyos Ocampo y Jose Jiménez