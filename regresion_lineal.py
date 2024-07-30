import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos
data = pd.read_csv('/mnt/data/inteligente.csv')

# Título de la aplicación
st.title('Gráficos de Barras por Columna')

# Iterar sobre cada columna y crear un gráfico de barras
for column in data.columns:
    st.write(f'Gráfico de barras para {column}')
    fig, ax = plt.subplots()
    data[column].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)