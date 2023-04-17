import streamlit as st
from config import freedman_diaconis_bindwidth, nbins, library_distribution
from main_page import df

st.markdown("# Numero de Bibliotecas ❄️")
st.sidebar.markdown("# Pagina 2 ❄️")

# Crear dos botones en Streamlit y organizarlos en una misma fila
col1, col2 = st.columns(2)
mostrar_original = col1.button("Mostrar gráfico con DataFrame original")
mostrar_filtrado = col2.button("Mostrar gráfico con DataFrame filtrado")

# Variable booleana para controlar la visualización del gráfico
mostrar_grafico = True

# Comprobar si se ha pulsado el botón para mostrar el gráfico con el DataFrame original
if mostrar_original:
    nb, ibi, iba, ibia = freedman_diaconis_bindwidth(df)
    nbins_df = nbins(df['nro_bibliotecas'], nb)
    library_distribution(df, nbins_df)
    mostrar_grafico = True

# Comprobar si se ha pulsado el botón para mostrar el gráfico con el DataFrame filtrado
if mostrar_filtrado:
    # Filtrar el DataFrame original para excluir las filas donde "institucion" es igual a "UCH"
    df_filtered = df[df["institucion"] != "UCH"]
    nb, ibi, iba, ibia = freedman_diaconis_bindwidth(df_filtered)
    nbins_df_filtered = nbins(df_filtered['nro_bibliotecas'], nb)
    library_distribution(df_filtered, nbins_df_filtered)
    mostrar_grafico = True