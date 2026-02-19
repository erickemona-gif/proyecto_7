import streamlit as st
import pandas as pd 
import plotly.express as px

#Encabezado 
st.header("Vehiculos")

car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir histograma') #Crear un botón

#Crear histograma
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión') #Crea un botón

#Crear gráfico de dispersión de precio VS kilometraje
if scatter_button:
    st.write('Creación de un gráfico de dispersión: Precio VS Kilometraje')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)