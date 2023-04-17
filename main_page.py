import streamlit as st
import pandas as pd
from config import new_names

st.markdown("# Encuesta sobre Inteligencia Artificial en Bibliotecas Universitarias de Chile 🎈")
st.sidebar.markdown("# Pagina Principal 🎈")

# Cargar el archivo CSV
file_path = 'encuesta.csv'
columns_to_use = list(range(1, 25))
new_column_names = new_names

df = pd.read_csv(file_path, index_col=False, usecols=columns_to_use)
df = df.rename(columns=new_column_names)
df = df.loc[:,"institucion":"posibilidad_reemplazo"]