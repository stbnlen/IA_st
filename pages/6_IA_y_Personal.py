import streamlit as st
from Pagina_Principal import df
from graphs.pie_charts import (
    create_pie_chart,
    create_pie_chart_two,
    create_pie_chart_three,
)

# st.set_page_config(page_title="IA y Personal")

st.markdown("# IA y personal de biblioteca 🥧")
st.sidebar.markdown("# Page 3 🥧")


# Crear un dropdown
dropdown = st.selectbox(
    "Seleccionar pregunta",
    [
        "¿Considera que su biblioteca está preparada para los cambios asociados a IA?",
        "¿Piensa que es posible capacitar al equipo de la biblioteca en sus usos?",
        "¿Considera usted que sistemas automatizados puedan reemplazar a los equipos de biblioteca?",
    ],
)


# Actualizar el gráfico de pastel basado en la selección del dropdown
if (
    dropdown
    == "¿Considera que su biblioteca está preparada para los cambios asociados a IA?"
):
    create_pie_chart(
        df,
        "cambios_en_biblioteca",
        "¿Considera que su biblioteca está preparada para los cambios <br> asociados a IA?",
    )

    st.markdown(
        """Si bien la respuestas positivas muestran un alto porcentaje (71,4%), existe un porcentaje que no se muestra de acuerdo y puede ser debido a
        factores que pudimos ver en preguntas anteriores, en las cuales el aspecto monetario y los recursos humanos son consideraciones muy importantes."""
    )
elif (
    dropdown
    == "¿Piensa que es posible capacitar al equipo de la biblioteca en sus usos?"
):
    create_pie_chart_two(df)

    st.markdown(
        """La percepción de los encuestados sobre esta pregunta es 100% positiva, todos consideran que es posible capacitar a su personal actual
        puede adaptarse a los avances tecnológicos al menos en su uso."""
    )
elif (
    dropdown
    == "¿Considera usted que sistemas automatizados puedan reemplazar a los equipos de biblioteca?"
):
    create_pie_chart_three(df)

    st.markdown(
        """Existe una alta valoración del servicio que entregan las personas, prueba de ello, es que la mitad de los encuestados considera que el servicio que brindan
        los bibliotecarios no puede ser reemplazado por alguna máquina, en tanto un 21% considera que si se puede reemplazar pero lentamente y el porcentaje restante cree que lo 
        que realmente va a ser reemplazado son las formas en que las personas trabajan creando nuevos puestos de trabajo y la suma de funciones para el personal."""
    )
