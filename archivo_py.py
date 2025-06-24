import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Análisis de anuncios de venta de vehículos en EE.UU.')

st.subheader('Vista previa del conjunto de datos')

st.dataframe(car_data)

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Construir grafico dispersion')

if scatter_button:
    st.write('Creación de un grafico de dispersion para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)



if st.checkbox("Mostrar histograma del kilometraje"):
    st.write("Histograma de kilometraje (odómetro)")
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        color_discrete_sequence=["#EAA64D"]  # Color personalizado
    )
    fig_hist.update_layout(
        xaxis_title="Kilometraje (millas)",
        yaxis_title="Cantidad de vehículos",
        title="Distribución del kilometraje"
    )
    st.plotly_chart(fig_hist, use_container_width=True)


if st.checkbox("Mostrar gráfico de dispersión entre kilometraje y precio"):
    st.write("Relación entre kilometraje y precio")
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color_discrete_sequence=["#0D5EA6"]  # Color personalizado
    )
    fig_scatter.update_layout(
        xaxis_title="Kilometraje (millas)",
        yaxis_title="Precio (USD)",
        title="Kilometraje vs. Precio"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
