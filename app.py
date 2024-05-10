import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# poner un encabezado
st.header('Aplicación de Visualización de Datos de Venta de Vehículos')

# crear casillas de verificación para histograma y gráfico de dispersión
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# si la casilla de verificación para el histograma está seleccionada
if build_histogram:
    # escribir un mensaje
    st.write('Construir un histograma para la columna odómetro')
    # crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# si la casilla de verificación para el gráfico de dispersión está seleccionada
if build_scatter:
    # escribir un mensaje
    st.write('Construir un gráfico de dispersión para las columnas odómetro y precio')
    # crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)
