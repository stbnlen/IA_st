import streamlit as st
from Pagina_Principal import df
from graphs.histogram_chart import library_distribution
from utils.number_of_bins import get_number_of_bins
from utils.freedman_diaconis import freedman_diaconis_bandwidth

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("# Numero de Bibliotecas 📉")

# Crear dos botones en Streamlit y organizarlos en una misma fila
col1, col2 = st.columns(2)
mostrar_original = col1.button("Mostrar gráfico con DataFrame original")
mostrar_filtrado = col2.button("Mostrar gráfico con DataFrame filtrado")

# Variable booleana para controlar la visualización del gráfico
mostrar_grafico = True

# Comprobar si se ha pulsado el botón para mostrar el gráfico con el DataFrame original
if mostrar_original:
    nb = freedman_diaconis_bandwidth(df["nro_bibliotecas"])
    nbins_df = get_number_of_bins(df["nro_bibliotecas"], nb)
    library_distribution(df, nbins_df)
    mostrar_grafico = True
    st.markdown(
        """El siguiente gráfico muestra el número de bibliotecas por institución (solo considerando las que respondieron la encuesta) siendo 9 la media
        de los datos. Pero si observamos tenemos un “outlier” que afecta esta medida además sus medidas de dispersión como su rango (46) y su desviación
        estándar (11.7) muestran una gran variabilidad."""
    )

# Comprobar si se ha pulsado el botón para mostrar el gráfico con el DataFrame filtrado
if mostrar_filtrado:
    # Filtrar el DataFrame original para excluir las filas donde "institucion" es igual a "UCH"
    df_filtered = df[df["institucion"] != "UCH"]
    nb = freedman_diaconis_bandwidth(df_filtered["nro_bibliotecas"])
    nbins_df_filtered = get_number_of_bins(df_filtered["nro_bibliotecas"], nb)
    library_distribution(df_filtered, nbins_df_filtered)
    mostrar_grafico = True
    st.markdown(
        """Ahora que los datos muestran una distribución más normal tenemos medidas de tendencia central más normalizadas indicando que la 
        media de bibliotecas por institución es de 6. Cabe destacar que este tratamiento solo se hace para describir los datos y no en el resto del análisis."""
    )
