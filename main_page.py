import pandas as pd
import streamlit as st
from typing import List, Dict
from utils.column_names import new_names

st.markdown(
    "# Encuesta sobre Inteligencia Artificial en Bibliotecas Universitarias de Chile 🎈"
)
st.markdown(
    """La investigación evalúa la implementación de servicios que contengan inteligencia artificial en las bibliotecas universitarias de Chile.
    Se revisan los avances de la capacidad del hardware en las computadoras y cómo esto ha permitido que los modelos de inteligencia artificial
    tengan una mayor capacidad para resolver tareas. Se describen los conflictos éticos y jurídicos en torno. Se consulta a los directores de bibliotecas
    sobre sus percepciones y evaluación de los servicios disponibles. Los resultados muestran cómo se está implementando la tecnología de inteligencia artificial,
    sus principales falencias y dificultades en su implementación, la visión a futuro y cómo es percibida por los diferentes directores de las bibliotecas encuestadas.
    Finalmente, se establecen los factores a tener en cuenta al momento de implementar algún sistema de IA en bibliotecas."""
)
st.markdown(
    """
    #### Palabras claves:
    **Inteligencia Artificial (IA), Bibliotecas universitarias, Política Nacional de IA, IA aspectos éticos, IA aspectos jurídicos, Big Data.**
"""
)


st.sidebar.markdown("# Pagina Principal 🎈")
st.sidebar.markdown("## Introduccion")

# Cargar el archivo CSV
file_path: str = "encuesta.csv"
columns_to_use: List[int] = list(range(1, 25))
new_column_names: Dict[str, str] = new_names

df: pd.DataFrame = pd.read_csv(file_path, index_col=False, usecols=columns_to_use)
df: pd.DataFrame = df.rename(columns=new_column_names)
df: pd.DataFrame = df.loc[:, "institucion":"posibilidad_reemplazo"]
