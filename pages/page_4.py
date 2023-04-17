import streamlit as st
from func import question_four, question_five, question_six, question_eight
from main_page import df
from config import create_bar_charts

st.markdown("# Tecnologias IA en Biblioteca ❄️")
st.sidebar.markdown("# Page 4 ❄️")


# Crear un dropdown
dropdown = st.selectbox("Seleccionar pregunta", ["Aspectos relevantes en la implementación de IA en bibliotecas",
                                                   "¿Qué impacto cree que generaría la implementación de IA dentro de las bibliotecas?",
                                                   "¿Qué nuevas tecnologías basadas en IA ha implementado o considera implementar en su biblioteca?",
                                                   "¿Ha adoptado o adoptaría alguna de las siguientes tecnologías en su biblioteca?"])


# Actualizar el gráfico de pastel basado en la selección del dropdown
if dropdown == "Aspectos relevantes en la implementación de IA en bibliotecas":
    economicos, recursos_humanos, politicas_ins, politicas_pu, etico, juridico, factibilidad = question_four(df["aspectos_relevantes"])
    values = [economicos, recursos_humanos, politicas_ins, politicas_pu, etico, juridico, factibilidad]
    aspectos = ["Aspectos económicos", "Recursos humanos", "Políticas institucionales",
                "Políticas públicas", "Aspectos éticos", "Aspectos jurídicos", "Factibilidad técnica"]

    create_bar_charts(aspectos, values, "Aspectos relevantes en la implementación de IA en bibliotecas")
elif dropdown == "¿Qué impacto cree que generaría la implementación de IA dentro de las bibliotecas?":
    mejoras_atención, mejora_procesos, mejora_flujos_trabajo, satisfacción_usuarios, mejora_percepción_de_usuarios, redistribución_trabajos = question_five(df["impacto_IA"])
    values = [mejoras_atención, mejora_procesos, mejora_flujos_trabajo, satisfacción_usuarios, mejora_percepción_de_usuarios, redistribución_trabajos]
    aspectos = ["Mejoras en atención", "Mejora en procesos internos", "Mejora en flujos de trabajo",
                "Satisfacción de usuarios", "Mejora en percepción de usuarios", "Redistribución del trabajo"]
    
    create_bar_charts(aspectos, values, "¿Qué impacto cree que generaría la implementación de IA dentro de las bibliotecas?")
elif dropdown == "¿Qué nuevas tecnologías basadas en IA ha implementado o <br> considera implementar en su biblioteca?":
    servicios_de_descubrimiento, robotica, chatbots, autoprestamos_autoservicio, catalogacion_automatizada, sistemas_de_recomendación, servicios_descarte = question_six(df["nuevas_tecnologias"])
    values = [servicios_de_descubrimiento, robotica, chatbots, autoprestamos_autoservicio, catalogacion_automatizada, sistemas_de_recomendación, servicios_descarte]
    aspectos = ["Servicios de descubrimiento", "Robótica", "Servicios de ayuda vía chat",
                "Autopréstamos/autoservicio", "Catalogación/clasificación automatizada",
                "Sistemas de recomendación", "Servicios de descarte"]
    
    create_bar_charts(aspectos, values, "¿Qué nuevas tecnologías basadas en IA ha implementado o <br> considera implementar en su biblioteca?")
elif dropdown == "¿Ha adoptado o adoptaría alguna de las siguientes tecnologías en su biblioteca?":
    ia, reconocimiento_de_voz, realidad_aumentada, mineria_datos, autoprestamo, gamificacion, chatbots, otro = question_eight(df["adopcion_de_tecnologia"])
    values = [ia, reconocimiento_de_voz, realidad_aumentada, mineria_datos, autoprestamo, gamificacion, chatbots, otro]
    aspectos = ["IA / ML.", "Reconocimiento de voz", "Realidad aumentada", "Mineria de datos", "Autoprestamo", "Gamificacion", "Chatbots", "Otro"]

    create_bar_charts(aspectos, values, "¿Ha adoptado o adoptaría alguna de las siguientes tecnologías <br> en su biblioteca?")




