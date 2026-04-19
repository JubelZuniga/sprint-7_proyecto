import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Vehiculos en Venta - US",
    layout="wide"
)

# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv('vehicles_us.csv')
    return df

df = load_data()

# Encabezado de la página
st.header("Análisis de Vehículos en Venta (USA)")
st.write("Explora el conjunto de datos de anuncios de coches usados.")


# visualización de gráficos, casilla de verificación
st.subheader("Visualizaciones Interactivas")

#Histograma del Odómetro, casilla de verificación 1
build_histogram = st.checkbox('Construir Histograma (Odómetro)')

if build_histogram:
    st.write('Distribución de millas recorridas por los vehículos anunciados.')
    fig_hist = px.histogram(df, x='odometer', nbins=50, title='Distribución del Odómetro')
    fig_hist.update_layout(xaxis_title='Millas', yaxis_title='Cantidad de Vehículos')
    st.plotly_chart(fig_hist, use_container_width=True)

#Gráfico de Dispersión, casilla de verificación 2
build_scatter = st.checkbox('Construir Gráfico de Dispersión (Odómetro vs Precio)')

if build_scatter:
    st.write('Relación entre el kilometraje y el precio de venta.')
    fig_scatter = px.scatter(df, x='odometer', y='price', 
                             title='Relación Odómetro vs Precio',
                             opacity=0.6)
    fig_scatter.update_layout(xaxis_title='Millas', yaxis_title='Precio (USD)')
    st.plotly_chart(fig_scatter, use_container_width=True)

#Histograma de Precios, casilla de verificación 3
build_price_hist = st.checkbox('Construir Histograma (Precios)')

if build_price_hist:
    st.write('Distribución de precios de los vehículos.')
    fig_price = px.histogram(df, x='price', nbins=50, title='Distribución de Precios')
    fig_price.update_layout(xaxis_title='Precio (USD)', yaxis_title='Cantidad de Vehículos')
    st.plotly_chart(fig_price, use_container_width=True)
