import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# poner un encabezado
st.header('Aplicación de Visualización de Datos de Venta de Vehículos')

hist_button = st.button('Construir histograma')  # construir un boton

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

 # crear un histograma
fig = px.histogram(car_data, x="odometer")
fig.show()  # mostrar el gráfico

# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)

disp_button = st.button(
    'Construir gráfico de dispersión')  # construir un boton

if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

 # crear un gráfico de dispersión
fig = px.scatter(car_data, x="odometer", y="price")
fig.show()  # mostrar el gráfico
