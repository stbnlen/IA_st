import streamlit as st
from Pagina_Principal import df
from graphs.histogram_chart import create_histogram_subplots

# st.set_page_config(page_title="Impacto IA")

st.markdown("# Impacto IA en Bibliotecas 📉")
st.sidebar.markdown("# Page 5 📉")

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

    st.markdown(
        """La respuesta que más sobresale entre los encuestados es la importancia que tendrá la Política Nacional de IA, toda vez que está parte de la
        base de que el desarrollo de esta tecnología es un pilar fundamental para el desarrollo integral de nuestro país. Lo que tiene un claro sentido, también,
        respecto a la necesidad de recibir apoyo para la implementación de esta tecnología (en términos de capacitación, y sobre todo infraestructura) como se apoyaría
        en la realidad es aún algo que dependerá de las leyes y presupuestos asignados desde el Estado para la implementación de la IA, que de acuerdo a la Política
        Nacional tiene un pilar fundamental en las universidades y por ende sus bibliotecas."""
    )

    st.markdown(
        """También es de destacar la importancia dada al software libre y los programas de código abierto, esto nos abre su sinnúmero de aplicaciones y mejoras que
        dependen, eso sí, de la propia preparación que tengan los encargados de áreas relacionadas dentro de la biblioteca. Aplicar software libre y/o de código abierto
        es gratis en términos de licencias, pero puede llegar a ser oneroso al momento de aplicar software de estas características y contratar especialistas en él.
        Las respuestas positivas a este tipo de software nos muestran un interés importante por conocer y aplicar estas programaciones libres que poco a poco se acercan a
        la IA libre de cargos monetarios."""
    )

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

    st.markdown(
        """También es clara la tendencia a darle importancia a temas relacionados a lo llamado ético jurídico, lo que no es baladí ya que una de principales desventajas que
        hemos detectado es la relacionada a una aplicación poco ética de la IA, toda vez que se trabajará con datos personales y obras protegidas por derechos de autor, temas
        que cobrarán realmente una gran importancia en futuras implementaciones de IA en bibliotecas universitarias."""
    )
