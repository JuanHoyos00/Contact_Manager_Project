# 🚀 Getting Started

Esta guía explica cómo configurar el proyecto localmente y ejecutar el primer comando desde la línea de comandos (CLI).

---

## 📦 Instalación usando uv

Este proyecto utiliza `uv` para la gestión de dependencias y ejecución.

Si no tienes `uv` instalado, puedes hacerlo con:

```bash
pip install uv
```

## 📁 Clonar el repositorio

Clona el proyecto y accede a la carpeta:

```bash
git clone "https://github.com/JuanHoyos00/Contact_Manager_Project.git"
cd <CONTACTMANAGERPROJECT>
```

## 🔄 Sincronización de dependencias

Para instalar todas las dependencias del proyecto, ejecuta:

```bash
uv sync
```

Este comando:
* Crea un entorno virtual automáticamente
* Instala todas las dependencias definidas en pyproject.toml

## ▶️ Primer comando de la CLI

Una vez instaladas las dependencias, puedes ejecutar el programa con:

```bash
uv run main.py --help
```

Este comando:
* Ejecuta el programa dentro del entorno virtual
* Muestra las opciones disponibles de la aplicación



## 📌 Resumen rápido

```bash
uv sync
uv run main.py --help
```

## 📖 Siguientes pasos

* Revisar la documentación de la API
* Explorar la arquitectura del proyecto
* Ejecutar y probar funcionalidades del gestor de contactos