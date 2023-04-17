import streamlit as st
from config import create_pie_chart
from main_page import df

st.markdown("# IA en Bibliotecas 🎉")
st.sidebar.markdown("# Pagina 3 🎉")


# Crear un dropdown
dropdown = st.selectbox("Seleccionar pregunta", ["¿Existe software relacionado con IA en la biblioteca?",
                                                   "¿Se tienen planes a futuro para la implementación de IA en la biblioteca?",
                                                   "¿Estima posible la implementación de la IA en las bibliotecas universitarias?",
                                                   "¿Usa o usaría está herramienta (IA) en su biblioteca para realizar labores propias de esta?"])


# Actualizar el gráfico de pastel basado en la selección del dropdown
if dropdown == "¿Existe software relacionado con IA en la biblioteca?":
    create_pie_chart(df, "servicios_IA", "¿Existe software relacionado con IA en la biblioteca?")
elif dropdown == "¿Se tienen planes a futuro para la implementación de IA en la biblioteca?":
    create_pie_chart(df, "planes_a_futuro", "¿Se tienen planes a futuro para la implementación de IA <br> en la biblioteca?")
elif dropdown == "¿Estima posible la implementación de la IA en las bibliotecas universitarias?":
    create_pie_chart(df, "posible_Implementacion", "¿Estima posible la implementación de la IA en las <br> bibliotecas universitarias?")
elif dropdown == "¿Usa o usaría está herramienta (IA) en su biblioteca para realizar labores propias de esta?":
    create_pie_chart(df, "uso_de_IA", "¿Usa o usaría está herramienta (IA) en su biblioteca para realizar <br> labores propias de esta?")