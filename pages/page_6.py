import streamlit as st
from main_page import df
from graphs.pie_charts import (
    create_pie_chart,
    create_pie_chart_two,
    create_pie_chart_three,
)

st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")


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
elif (
    dropdown
    == "¿Piensa que es posible capacitar al equipo de la biblioteca en sus usos?"
):
    create_pie_chart_two(df)
elif (
    dropdown
    == "¿Considera usted que sistemas automatizados puedan reemplazar a los equipos de biblioteca?"
):
    create_pie_chart_three(df)
