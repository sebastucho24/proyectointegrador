import streamlit as st
import pandas as pd
# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")

import pandas as pd
import streamlit as st

df = pd.read_csv('dataset/estudiantes_colombia.csv')

st.dataframe(df)

st.header("Primeras 5 filas del dataframe")
st.write(df.head())

st.header("Últimas 5 filas del dataframe")
st.write(df.tail())

st.header("Resumen del dataframe")
st.write("Información del dataframe:")
st.write(df.info())

st.write("Descripción estadística del dataframe:")
st.write(df.describe())

st.header("Seleccionar columnas específicas")
columnas = st.multiselect("Selecciona las columnas que quieres ver", df.columns)
if columnas:
    st.write(df[columnas])

st.header("Filtrar estudiantes por promedio")
promedio_minimo = st.slider("Selecciona el promedio mínimo", 0.0, 5.0, 3.0)
estudiantes_filtrados = df[df['promedio'] > promedio_minimo]
st.write(estudiantes_filtrados)
