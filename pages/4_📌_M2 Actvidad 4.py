import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

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


# Crear dos DataFrames con datos de estudiantes
df1 = pd.DataFrame({
    'Nombre': ['Ana', 'Luis'],
    'Edad': [20, 22],
    'Ciudad': ['Madrid', 'Barcelona']
})

df2 = pd.DataFrame({
    'Nombre': ['Marta', 'Pedro'],
    'Edad': [19, 21],
    'Ciudad': ['Valencia', 'Sevilla']
})

# Agregar filas usando pd.concat (eje 0 para filas)
df_combinado = pd.concat([df1, df2], ignore_index=True)
# ignore_index=True reinicia los índices para evitar duplicados

print("DataFrame combinado (filas agregadas):")
print(df_combinado)

# Agregar una nueva columna
df_combinado['Nota'] = [8.5, 7.0, 9.0, 6.5]  # Nueva columna con notas
print("\nDataFrame con nueva columna:")
print(df_combinado)



# Crear un DataFrame con datos de ventas
df_ventas = pd.DataFrame({
    'Producto': ['Manzana', 'Naranja', 'Manzana', 'Naranja', 'Manzana'],
    'Ciudad': ['Madrid', 'Madrid', 'Barcelona', 'Barcelona', 'Madrid'],
    'Ventas': [100, 150, 200, 120, 80]
})

# Agrupar por 'Producto' y calcular el promedio de ventas
ventas_por_producto = df_ventas.groupby('Producto')['Ventas'].mean()

print("Promedio de ventas por producto:")
print(ventas_por_producto)

# Agrupar por 'Ciudad' y contar el número de registros
conteo_por_ciudad = df_ventas.groupby('Ciudad').count()

print("\nConteo de registros por ciudad:")
print(conteo_por_ciudad)



# Crear dos DataFrames
df_estudiantes = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Nombre': ['Ana', 'Luis', 'Marta', 'Pedro'],
    'Curso': ['Matemáticas', 'Historia', 'Física', 'Química']
})

df_notas = pd.DataFrame({
    'ID': [1, 2, 5],
    'Nota': [8.5, 7.0, 9.0]
})

# Fusión tipo 'inner'
inner_merge = pd.merge(df_estudiantes, df_notas, on='ID', how='inner')
# 'on' especifica la columna clave; 'how' define el tipo de fusión

print("Fusión tipo inner:")
print(inner_merge)

# Fusión tipo 'left'
left_merge = pd.merge(df_estudiantes, df_notas, on='ID', how='left')

print("\nFusión tipo left:")
print(left_merge)