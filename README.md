# 📘 Proyecto Integrador - Aplicación Streamlit

Este proyecto es una aplicación web desarrollada con Streamlit que facilita la visualización y realización de las actividades y evaluaciones del curso _Nuevas Tecnologías de Programación_ del programa de Desarrollo de Software.

---

## 🧩 Características

- Interfaz de usuario intuitiva y adaptable.
- Navegación estructurada por momentos y actividades del curso.
- Secciones específicas para cada actividad y evaluación.
- Organización modular del código.

---

## 📁 Estructura del Proyecto

bash
proyectointegrador/
├── .devcontainer/ # Configuraciones para entornos de desarrollo
├── .streamlit/ # Configuraciones específicas de Streamlit
├── .venv/ # Entorno virtual (opcional)
├── assets/ # Imágenes y otros recursos
├── dataset/ # Datos utilizados por la app
├── pages/ # Páginas individuales de la aplicación
├── Inicio.py # Archivo principal para ejecutar la app
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación del proyecto

## ✅ Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

---

## ⚙️ Instalación y Ejecución

Clona el repositorio:

bash
git clone https://github.com/sebastucho24/proyectointegrador.git
cd proyectointegrador

# Guía para Crear y Ejecutar la Aplicación

Sigue estos pasos para configurar y ejecutar la aplicación correctamente.

---

## Paso 1: (Opcional) Crear y activar un entorno virtual

### EN WINDOWS:

bash
python -m venv .venv
.venv\Scripts\activate

### EN MACOS/LINUX:

bash
python3 -m venv .venv
source .venv/bin/activate

---

## PASO 2: INSTALAR LAS DEPENDENCIAS

bash
pip install -r requirements.txt

---

## Paso 3: Ejecutar la aplicación

bash
streamlit run Inicio.py
