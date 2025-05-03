import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página (debe ser la primera línea de código)
st.set_page_config(
    page_icon="📌",
    layout="wide"
)

# Título de la aplicación
st.title("Momento 2 - Actividad 4")

# Descripción de la actividad
st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

# Objetivos de aprendizaje
st.header("Objetivos de aprendizaje")
st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

# Creación del DataFrame de ejemplo
def crear_df():
    np.random.seed(42)
    data = {
        'ID': range(1, 11),
        'Nombre': ['Juan', 'Ana', 'Pedro', 'Maria', 'Luis', 'Carlos', 'Sofia', 'Marta', 'Andres', 'Lucia'],
        'Edad': np.random.randint(20, 60, 10),
        'Salario': np.random.randint(1000000, 5000000, 10),
        'Ciudad': ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena', 
                   'Bucaramanga', 'Manizales', 'Pereira', 'Santa Marta', 'Cúcuta']
    }
    df = pd.DataFrame(data)
    return df

# Crear el DataFrame
df = crear_df()

# Mostrar el DataFrame original
st.header("Datos Iniciales")
st.write(df)

# Ejercicio 1: Filtro por Edad utilizando .loc
st.subheader("🔹 Filtrar por Edad utilizando .loc")
edad_min, edad_max = st.slider("Selecciona el rango de edad", 18, 80, (20, 50))
df_edad = df.loc[df['Edad'].between(edad_min, edad_max)]
st.write(df_edad)

# Ejercicio 2: Selección de filas y columnas usando .iloc
st.subheader("🔹 Seleccionar filas y columnas con .iloc")
fila = st.slider("Selecciona el número de fila (índice)", 0, len(df) - 1, 0)
columna = st.slider("Selecciona el número de columna", 0, len(df.columns) - 1, 0)
valor_seleccionado = df.iloc[fila, columna]
st.write(f"Valor en la fila {fila} y columna {columna}: {valor_seleccionado}")

# Ejercicio 3: Modificar un valor en el DataFrame con .loc
st.subheader("🔹 Modificar un valor con .loc")
id_modificar = st.selectbox("Selecciona el ID de la persona a modificar", df['ID'])
nueva_edad = st.number_input("Ingresa la nueva edad", min_value=18, max_value=100, value=df.loc[df['ID'] == id_modificar, 'Edad'].values[0])
df.loc[df['ID'] == id_modificar, 'Edad'] = nueva_edad
st.write("Datos actualizados:")
st.write(df)

# Ejercicio 4: Filtro combinado con .loc y .iloc
st.subheader("🔹 Filtro combinado con .loc y .iloc")
filtro_ciudad = st.selectbox("Selecciona una ciudad para filtrar", df['Ciudad'].unique())
df_filtrado = df.loc[df['Ciudad'] == filtro_ciudad]

# Verifica si df_filtrado tiene más de una fila antes de crear el slider
if len(df_filtrado) > 1:
    fila_1 = st.slider("Selecciona la fila para ver con .iloc", 0, len(df_filtrado) - 1, 0)
    columna_1 = st.slider("Selecciona la columna para ver con .iloc", 0, len(df.columns) - 1, 0)
    valor_filtrado = df_filtrado.iloc[fila_1, columna_1]
    st.write(f"Valor seleccionado con .iloc en la ciudad {filtro_ciudad}: {valor_filtrado}")
else:
    st.write(f"No hay suficientes datos para mostrar en la ciudad {filtro_ciudad}.")

# Resumen Final
st.subheader("🔹 Resumen Final")
st.write(f"Total de registros: {df.shape[0]}")
st.write(f"Datos filtrados para la ciudad {filtro_ciudad}:")
st.write(df_filtrado)
