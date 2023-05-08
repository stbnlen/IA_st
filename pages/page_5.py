import streamlit as st
from main_page import df
from graphs.histogram_chart import create_histogram_subplots

st.markdown("# Impacto IA en Bibliotecas ❄️")
st.sidebar.markdown("# Page 5 ❄️")

col1, col2 = st.columns(2)
mostrar_original = col1.button("Mostrar gráfico Nro1")
mostrar_filtrado = col2.button("Mostrar gráfico Nro2")


# Comprobar si se ha pulsado el botón para mostrar el gráfico con el DataFrame original
if mostrar_original:
    cols = [
        "impacto_en_bibliotecas_open",
        "impacto_en_bibliotecas_libre",
        "impacto_en_bibliotecas_politica",
    ]
    titles = ["Acceso abierto", "Software libre", "Política Nacional"]
    create_histogram_subplots(df, cols, titles)

# Comprobar si se ha pulsado el botón para mostrar el gráfico con el DataFrame filtrado
if mostrar_filtrado:
    cols = [
        "impacto_en_bibliotecas_datos_personales",
        "impacto_en_bibliotecas_privacidad",
        "impacto_en_bibliotecas:derechosautor",
    ]
    titles = [
        "Protección de Datos Personales",
        "Privacidad de la Información",
        "Derechos de Autor",
    ]
    create_histogram_subplots(df, cols, titles)
