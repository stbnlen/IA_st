import streamlit as st
import pandas as pd
from utils.column_names import new_names_final_questions
from utils.all_answers import get_all_answers, make_cloud

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("# Preguntas Abiertas")

file_path: str = "encuesta.csv"
df_question = pd.read_csv(file_path)

df_question = df_question.rename(columns=new_names_final_questions)
df_question = df_question.loc[:, "pregunta_uno":]
df_question = df_question.dropna()
index = [pd.Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])]
df_question = df_question.set_index(index)

col1, col2 = st.columns(2)
mostrar_original = col1.button(
    "¿Según su percepción qué desventajas o aspectos desfavorables podría traer a su biblioteca las nuevas tecnologías de IA?"
)
mostrar_filtrado = col2.button(
    "¿Qué reflexión tiene acerca de las bibliotecas con respecto a la Inteligencia Artificial y su proyección futura?"
)

if mostrar_original:
    first_question = get_all_answers(df_question, "pregunta_uno")
    first_question_image = make_cloud(first_question, "first_question")

    st.image(first_question_image, caption="Sunrise by the mountains")
    st.markdown(
        """Se puede apreciar una tendencia en las respuestas a un temor por parte de los funcionarios de las bibliotecas a la implementación de la
        IA dentro de las unidades de información. Esto ocurre debido a una sensación de reemplazo por parte del personal, los cambios generalmente generan
        incertidumbre por lo que es necesario informar y explicar las ventajas que esto conlleva en los distintos procesos y servicios que se brindan. “Resistencia
        al cambio” y “Temor a que la atención personal sea reemplazada” son algunas de las respuestas que evidencian esta problemática con la implementación de tecnologías de IA. """
    )

if mostrar_filtrado:
    second_question = get_all_answers(df_question, "pregunta_dos")
    second_question_image = make_cloud(second_question, "second_question")

    st.image(second_question_image, caption="Sunrise by the mountains")
    st.markdown(
        """La tendencia en las respuestas es acerca de la planificación e implementación de la IA en las bibliotecas. La reflexión que mayoritariamente fue manifestada por los
        encuestados tiene que ver con la necesidad de realizar una planificación que permita una correcta implementación de la IA pero tomando en cuenta la pregunta “¿Estima posible
        la implementación de la IA en las bibliotecas universitarias actualmente?” esta fue respondida de manera positiva con un 92,9% por lo que a pesar de la preocupación en su implementación,
        la mayoría consideró posible que ésta pudiese ser llevada a cabo actualmente. """
    )
