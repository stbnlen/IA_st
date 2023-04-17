import streamlit as st
from func import questions
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
    aspectos_interes = ("Aspectos económicos", "Recursos humanos", "Políticas institucionales", "Políticas públicas", "Aspectos éticos", "Jurídico", "Factibilidad")

    resultados_aspectos = questions(df["aspectos_relevantes"], aspectos_interes, "Jurídico", "Factibilidad")

    values = [resultados_aspectos[aspecto] for aspecto in aspectos_interes]

    create_bar_charts(aspectos_interes, values, "Aspectos relevantes en la implementación de IA en bibliotecas")


elif dropdown == "¿Qué impacto cree que generaría la implementación de IA dentro de las bibliotecas?":
    aspectos_interes = ("Mejoras en la atención al usuario.", "Mejora de procesos internos de las bibliotecas.", "Mejoras en los flujos de trabajo.", "Satisfacción de los usuarios en los servicios.", "Mejora de percepción de los usuarios.", "Redistribución de trabajos.")

    resultados_impacto_IA = questions(df["impacto_IA"], aspectos_interes, "Mejora de percepción de los usuarios.", "Redistribución de trabajos.")

    values = [resultados_impacto_IA[aspecto] for aspecto in aspectos_interes]
        
    create_bar_charts(aspectos_interes, values, "¿Qué impacto cree que generaría la implementación de IA <br> dentro de las bibliotecas?")


elif dropdown == "¿Qué nuevas tecnologías basadas en IA ha implementado o considera implementar en su biblioteca?":
    aspectos_interes = ("Servicios de descubrimiento con asistentes inteligentes", "Robótica", "Servicios de ayuda al estudiante vía chat. (chatbots)", "Autopréstamos/autoservicio", "Catalogación/clasificación automatizada","Sistemas de recomendación", "Servicios de descarte")

    resultados_nuevas_tecnologias = questions(df["nuevas_tecnologias"], aspectos_interes, "Servicios de descarte")

    values = [resultados_nuevas_tecnologias[aspecto] for aspecto in aspectos_interes]
    
    create_bar_charts(aspectos_interes, values, "¿Qué nuevas tecnologías basadas en IA ha implementado o <br> considera implementar en su biblioteca?")


    
elif dropdown == "¿Ha adoptado o adoptaría alguna de las siguientes tecnologías en su biblioteca?":
    aspectos_interes = ("Inteligencia Artificial / Aprendizaje automático.", "Reconocimiento de voz.", "Aplicaciones de realidad aumentada.", "Minería de Datos", "Auto-Préstamos de material bibliográfico.", "Gamificación de la experiencia bibliotecaria.", "Chatbots", "Otros avances tecnológicos.")

    resultados_adopcion = questions(df["adopcion_de_tecnologia"] , aspectos_interes)

    values = [resultados_adopcion[aspecto] for aspecto in aspectos_interes]

    create_bar_charts(aspectos_interes, values, "¿Ha adoptado o adoptaría alguna de las siguientes tecnologías <br> en su biblioteca?")




