import streamlit as st
import pandas as pd
import numpy as np
from faker import Faker
import random

st.set_page_config(
    page_title="Actividad M2",
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.

Además, implementaremos una aplicación interactiva con Streamlit, donde simularemos la generación de datos demográficos utilizando la librería Faker, y aplicaremos filtros dinámicos sobre un conjunto de datos que representa una población ficticia.
Se trabajará con bibliotecas como NumPy y Pandas para el manejo y análisis de datos, incluyendo aspectos como valores nulos, conversión de tipos, y operaciones estadísticas simples.
""")

st.header("Objetivos de aprendizaje")
st.markdown("""
-Dominar las estructuras de datos fundamentales como listas, tuplas, diccionarios y conjuntos

-Familiarizarse con el uso de bibliotecas como NumPy, Pandas, y Faker

-Identificar y manejar valores nulos dentro de un conjunto de datos

-Aplicar filtros sobre datos utilizando condiciones lógicas 
""")

def generar_datos():
    fake = Faker('es_CO')
    np.random.seed(123)
    random.seed(123)
    fake.seed_instance(123)

    n = 50
    data = {
        'id': range(1, n + 1),
        'nombre_completo': [fake.name() for _ in range(n)],
        'edad': np.random.randint(15, 76, n),
        'region': random.choices(
            ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
            weights=[0.3, 0.4, 0.15, 0.1, 0.05],
            k=n
        ),
        'municipio': random.choices(
            [
                'Barranquilla', 'Santa Marta', 'Cartagena',  # Caribe
                'Bogotá', 'Medellín', 'Tunja', 'Manizales',  # Andina
                'Cali', 'Quibdó', 'Buenaventura',           # Pacífica
                'Villavicencio', 'Yopal',                    # Orinoquía
                'Leticia', 'Puerto Inírida'                  # Amazonía
            ],
            k=n
        ),
        'ingreso_mensual': np.random.randint(800000, 12000001, n),
        'ocupacion': random.choices(
            [
                'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
                'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
                'Emprendedor', 'Obrero'
            ],
            k=n
        ),
        'tipo_vivienda': random.choices(['Propia', 'Arrendada', 'Familiar'], k=n),
        'fecha_nacimiento': [fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)],
        'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
    }

    df = pd.DataFrame(data)
    df.loc[3:5, 'ingreso_mensual'] = np.nan
    df.loc[15:17, 'ocupacion'] = np.nan
    df['fecha_nacimiento'] = pd.to_datetime(df['fecha_nacimiento'])
    return df

df = generar_datos()

st.subheader("🔹 Ejercicio 1: Visualización de los datos generados")
st.write(df.head())

st.subheader("🔹 Ejercicio 2: Filtro por Edad")
edad_min, edad_max = st.slider("Selecciona el rango de edad", 15, 75, (20, 40))
df_edad = df[df['edad'].between(edad_min, edad_max)]
st.write(df_edad)

st.subheader("🔹 Ejercicio 3: Filtro por Municipio")
municipios = st.multiselect("Selecciona municipios", sorted(df['municipio'].unique()))
df_municipio = df[df['municipio'].isin(municipios)] if municipios else df
st.write(df_municipio)

st.subheader("🔹 Ejercicio 4: Filtro por Ingreso Mensual")
ingreso_min = st.slider("Filtrar por ingreso mensual mínimo", 800000, 12000000, 2000000)
df_ingreso = df[df['ingreso_mensual'] > ingreso_min]
st.write(df_ingreso)

st.subheader("🔹 Ejercicio 5: Filtros Combinados y Resumen Final")

df_filtrado = df[
    df['edad'].between(edad_min, edad_max) &
    (df['ingreso_mensual'] > ingreso_min)
]

if municipios:
    df_filtrado = df_filtrado[df_filtrado['municipio'].isin(municipios)]

st.write(df_filtrado)

st.markdown(f"**Total de registros después de aplicar los filtros:** {df_filtrado.shape[0]}")
