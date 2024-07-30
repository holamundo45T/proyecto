import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de Streamlit
st.title('CIENTIFICOS INTELIGENTES')

# Cargar el archivo CSV usando el cargador de archivos de Streamlit
archivo_csv = st.file_uploader("Sube tu archivo CSV", type="csv")

if archivo_csv:
    try:
        # Cargar los datos
        data = pd.read_csv(archivo_csv)

        # Limpiar nombres de columnas
        data.columns = data.columns.str.strip()

        # Verificar las columnas
        st.write("Columnas disponibles:", data.columns)

        # Mostrar las primeras filas del dataset
        st.write(data.head())

        # Función para graficar y mostrar gráficos en Streamlit
        def plot_and_show(data, x, y=None, title='', xlabel='', ylabel='', plot_type='bar', color='blue'):
            plt.figure(figsize=(10, 6))
            if plot_type == 'bar':
                sns.barplot(x=x, y=y, data=data, color=color)
            elif plot_type == 'line':
                sns.lineplot(x=x, y=y, data=data, color=color)
            elif plot_type == 'hist':
                sns.histplot(data[x], kde=True, color=color)
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.grid(True)
            st.pyplot(plt.gcf())
            plt.close()

        # Gráfico de IQ de los científicos (Histograma)
        if 'IQ' in data.columns:
            plot_and_show(data, x='IQ', title='IQ Distribution', xlabel='IQ', ylabel='Frequency', plot_type='hist', color='teal')
        else:
            st.error("La columna 'IQ' no se encuentra en el archivo.")

        # Gráfico de Birth Year de los científicos (Histograma)
        if 'Birth Year' in data.columns:
            plot_and_show(data, x='Birth Year', title='Birth Year Distribution', xlabel='Birth Year', ylabel='Frequency', plot_type='hist', color='coral')
        else:
            st.error("La columna 'Birth Year' no se encuentra en el archivo.")

        # Gráfico de Género de los científicos (Barras)
        if 'Gender' in data.columns:
            plot_and_show(data, x='Gender', title='Gender Distribution', xlabel='Gender', ylabel='Count', plot_type='bar', color='green')
        else:
            st.error("La columna 'Gender' no se encuentra en el archivo.")

        # Gráfico de Países de los científicos (Barras)
        if 'Country' in data.columns:
            plot_and_show(data, x='Country', title='Country Distribution', xlabel='Country', ylabel='Count', plot_type='bar', color='blue')
        else:
            st.error("La columna 'Country' no se encuentra en el archivo.")

        # Gráfico de Campos de especialización (Barras)
        if 'Field of Expertise' in data.columns:
            plot_and_show(data, x='Field of Expertise', title='Field of Expertise Distribution', xlabel='Field of Expertise', ylabel='Count', plot_type='bar', color='orange')
        else:
            st.error("La columna 'Field of Expertise' no se encuentra en el archivo.")

    except pd.errors.EmptyDataError:
        st.error("El archivo está vacío. Por favor, verifique el contenido del archivo.")
    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo: {e}")
else: 
    st.info("Por favor, sube un archivo CSV para comenzar.")
