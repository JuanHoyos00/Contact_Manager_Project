# Proyecto Contact Manager

## 📖 Descripción del Proyecto

**Contact Manager** es una aplicación de línea de comandos (CLI) en Python para gestionar contactos de manera sencilla y eficiente.  
Permite **agregar, eliminar, consultar y mostrar contactos** almacenados en un archivo JSON.  
El proyecto está diseñado con:

- **Python 3.12+**
- **Typer** para la interfaz de línea de comandos
- **JSONStorage** para almacenamiento persistente
- Diseño modular: `services`, `models` y `storage`

**Propósito:** Brindar una herramienta ligera y multiplataforma para la gestión de contactos personales o pequeños equipos.  
**Alcance:** Operaciones básicas de CLI para manejar contactos, fácilmente extensible para proyectos más grandes.

---

## ⚙️ Guía de Instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/JuanHoyos00/Contact_Manager_Project.git
cd Contact_Manager_Project



```bash
### 🖥️ Comandos Disponibles

| Comando | Descripción | Ejemplo |
|---------|------------|---------|
| ✨ `add-contact` | Agrega un nuevo contacto | `uv run main.py add-contact "Juan" "1" "123456789" "USA"` |
| ❌ `delete-contact-by-number` | Elimina un contacto por número de teléfono | `uv run main.py delete-contact-by-number "123456789"` |
| 🔍 `get-contact-by-number` | Muestra los datos de un contacto por número | `uv run main.py get-contact-by-number "123456789"` |
| 📋 `show-contacts` | Muestra todos los contactos | `uv run main.py show-contacts` |

> 💡 Tip: Puedes usar `--help` para ver más detalles de cada comando:
uv run main.py --help
uv run main.py add-contact --help