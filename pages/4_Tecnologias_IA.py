import streamlit as st
from Pagina_Principal import df
from utils.question import questions
from graphs.bar_charts import create_bar_charts

# st.set_page_config(page_title="Tecnologias IA")

st.markdown("# Tecnologias IA en Biblioteca 📊")
st.sidebar.markdown("# Page 4 📊")


# Crear un dropdown
dropdown = st.selectbox(
    "Seleccionar pregunta",
    [
        "Aspectos relevantes en la implementación de IA en bibliotecas",
        "¿Qué impacto cree que generaría la implementación de IA dentro de las bibliotecas?",
        "¿Qué nuevas tecnologías basadas en IA ha implementado o considera implementar en su biblioteca?",
        "¿Ha adoptado o adoptaría alguna de las siguientes tecnologías en su biblioteca?",
    ],
)


# Actualizar el gráfico de pastel basado en la selección del dropdown
if dropdown == "Aspectos relevantes en la implementación de IA en bibliotecas":
    aspectos_interes = (
        "Aspectos económicos",
        "Recursos humanos",
        "Políticas institucionales",
        "Políticas públicas",
        "Aspectos éticos",
        "Jurídico",
        "Factibilidad",
    )

    resultados_aspectos = questions(
        df["aspectos_relevantes"], aspectos_interes, "Jurídico", "Factibilidad"
    )

    values = [resultados_aspectos[aspecto] for aspecto in aspectos_interes]

    create_bar_charts(
        aspectos_interes,
        values,
        "Aspectos relevantes en la implementación de IA en bibliotecas",
    )
    st.markdown(
        """Respecto a los factores de aplicación sobresale claramente que el aspecto monetario y el de los recursos humanos son los más relevantes a la
        hora de pensar en la implementación de tecnologías de IA. Por lo que, si bien en la respuesta anterior 13 de 14 encuestados (el 92,9%) considera posible
        aplicar IA, el factor monetario puede ser un obstáculo importante para llevar esto a la realidad. También lo es la variable de los recursos humanos que en la
        pregunta relacionada a ellos se pueden obtener más datos sobre de cómo esto puede llegar a ser una dificultad de implementación."""
    )
    st.markdown(
        """Por otra parte, es importante mencionar que los aspectos ético-jurídicos no son consideradas mayormente relevantes (menos del 50% considera importantes
        los aspectos éticos y solo el 7% los legales) , lo que puede llegar a ser un grave problema a la hora de implementar tecnologías de IA, ya que de acuerdo a
        la investigación hemos detectado que el almacenamiento y manejo de datos (de carácter personal) puede derivar en graves problemas de carácter legal sino se aplican adecuadamente
        las reglas y normas de nuestra legislación, deviniendo, además, en graves problemas éticos o de sesgos discriminatorios no compatibles con los derechos de las persona"""
    )

elif (
    dropdown
    == "¿Qué impacto cree que generaría la implementación de IA dentro de las bibliotecas?"
):
    aspectos_interes = (
        "Mejoras en la atención al usuario.",
        "Mejora de procesos internos de las bibliotecas.",
        "Mejoras en los flujos de trabajo.",
        "Satisfacción de los usuarios en los servicios.",
        "Mejora de percepción de los usuarios.",
        "Redistribución de trabajos.",
    )

    resultados_impacto_IA = questions(
        df["impacto_IA"],
        aspectos_interes,
        "Mejora de percepción de los usuarios.",
        "Redistribución de trabajos.",
    )

    values = [resultados_impacto_IA[aspecto] for aspecto in aspectos_interes]

    create_bar_charts(
        aspectos_interes,
        values,
        "¿Qué impacto cree que generaría la implementación de IA <br> dentro de las bibliotecas?",
    )

    st.markdown(
        """Que plantea la interrogante sobre qué áreas de la biblioteca se verían favorecidas por la implementación de IA, podemos observar en primer lugar, que las mejoras en los servicios
        al usuario es lo que más destaca en la suma total de las respuestas ya que entre las dos variables relacionadas a los usuarios suman 25 respuestas positivas.
        Ya que a las mejoras en la atención se suma la satisfacción de los mismos con el servicio recibido, esto ya que si consideramos que el eje de título vertical del gráfico muestra la
        cantidad de respuestas positivas, podemos señalar que casi el 93% de los encuestados señala que estas son las variables más valiosas, junto con el 85,7% de respuestas que apuntan a
        las mejoras en la atención al público. Por otra parte, las mejoras en la biblioteca a nivel organizacional también tienen su relevancia, dentro de las respuestas obtenidas, así un 50% de
        los encuestados considera que habrán mejoras en los flujos de trabajo y el 64,3% considera que existirán mejoras en los procesos internos de las bibliotecas."""
    )


elif (
    dropdown
    == "¿Qué nuevas tecnologías basadas en IA ha implementado o considera implementar en su biblioteca?"
):
    aspectos_interes = (
        "Servicios de descubrimiento con asistentes inteligentes",
        "Robótica",
        "Servicios de ayuda al estudiante vía chat. (chatbots)",
        "Autopréstamos/autoservicio",
        "Catalogación/clasificación automatizada",
        "Sistemas de recomendación",
        "Servicios de descarte",
    )

    resultados_nuevas_tecnologias = questions(
        df["nuevas_tecnologias"], aspectos_interes, "Servicios de descarte"
    )

    values = [resultados_nuevas_tecnologias[aspecto] for aspecto in aspectos_interes]

    create_bar_charts(
        aspectos_interes,
        values,
        "¿Qué nuevas tecnologías basadas en IA ha implementado o <br> considera implementar en su biblioteca?",
    )

    st.markdown(
        """Respecto a las tecnologías más prácticas, o las formas en que se puede aplicar la IA, los encuestados nuevamente consideran más útiles de utilizar
        aquellas centradas en el usuario, ya que la mayoría de las respuestas apuntan a los servicios enfocados en estos. Así, todas las opciones asociadas a los
        usuarios muestran un alto porcentaje, en comparación con los servicios o aplicaciones centrados en los procesos internos de la biblioteca."""
    )

elif (
    dropdown
    == "¿Ha adoptado o adoptaría alguna de las siguientes tecnologías en su biblioteca?"
):
    aspectos_interes = (
        "Inteligencia Artificial / Aprendizaje automático.",
        "Reconocimiento de voz.",
        "Aplicaciones de realidad aumentada.",
        "Minería de Datos",
        "Auto-Préstamos de material bibliográfico.",
        "Gamificación de la experiencia bibliotecaria.",
        "Chatbots",
        "Otros avances tecnológicos.",
    )

    resultados_adopcion = questions(df["adopcion_de_tecnologia"], aspectos_interes)

    values = [resultados_adopcion[aspecto] for aspecto in aspectos_interes]

    create_bar_charts(
        aspectos_interes,
        values,
        "¿Ha adoptado o adoptaría alguna de las siguientes tecnologías <br> en su biblioteca?",
    )

    st.markdown(
        """A la luz de los resultados de esta pregunta, nuevamente salta a la vista el enfoque en los usuarios que perciben de mayor utilidad los encuestados, ya que
        podemos ver que la mayoría de respuestas apuntan a servicios destinados a estos: Chatbots (71,4%), auto-préstamos de material bibliográfico (64,3%) y aplicaciones de
        realidad aumentada (57,1%). Por otro lado la minería de datos (64,3%), asociada al big data también, es una herramienta considerada útil, la cual es posible de aplicar
        tanto para los usuarios (al ser susceptible de aplicar en entornos investigativos y en la recuperación de información), como también para la mejora de los procesos
        internos de la organización (mejoras en los flujos de trabajo, dashboard en tiempo real para conocer y comprender aspectos relevantes de la biblioteca)."""
    )
