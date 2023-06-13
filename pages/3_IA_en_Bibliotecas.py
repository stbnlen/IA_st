import streamlit as st
from graphs.pie_charts import create_pie_chart
from Pagina_Principal import df

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("# IA en Bibliotecas 🥧")

# Crear un dropdown
dropdown = st.selectbox(
    "Seleccionar pregunta",
    [
        "¿Existe software relacionado con IA en la biblioteca?",
        "¿Se tienen planes a futuro para la implementación de IA en la biblioteca?",
        "¿Estima posible la implementación de la IA en las bibliotecas universitarias?",
        "¿Usa o usaría está herramienta (IA) en su biblioteca para realizar labores propias de esta?",
    ],
)


# Actualizar el gráfico de pastel basado en la selección del dropdown
if dropdown == "¿Existe software relacionado con IA en la biblioteca?":
    create_pie_chart(
        df, "servicios_IA", "¿Existe software relacionado con IA en la biblioteca?"
    )
    st.markdown(
        """De acuerdo a lo señalado en la descripción de la pregunta esta busca saber sí existen o no servicios asociados a la IA
        en la biblioteca del encuestado, dejando la opción “No sé” para evaluar el desconocimiento de los servicios de IA. Cómo se aprecia
        en los resultados, y puesto que el enunciado señala “algunas tecnologías asociadas a la IA” de uso, detectado por nosotros, de carácter común,
        los encuestados señalan, en su mayoría, que sí existen estos servicios asociados a la tecnología de IA. Servicios que no necesariamente utilizan esta
        tecnología pero que sí son susceptibles de una mejora a través de la IA, como es el caso de los chat."""
    )
elif (
    dropdown
    == "¿Se tienen planes a futuro para la implementación de IA en la biblioteca?"
):
    create_pie_chart(
        df,
        "planes_a_futuro",
        "¿Se tienen planes a futuro para la implementación de IA <br> en la biblioteca?",
    )
    st.markdown(
        """Los resultados de esta pregunta nos muestran que sí existen planes a futuro en la implementación de esta tecnología. Por lo que podemos señalar,
        a priori e independiente de otras respuestas, que la IA se considera una herramienta válida y se consideran planes, por parte de los encuestados,
        de aplicación en las bibliotecas universitarias chilenas. """
    )
elif (
    dropdown
    == "¿Estima posible la implementación de la IA en las bibliotecas universitarias?"
):
    create_pie_chart(
        df,
        "posible_Implementacion",
        "¿Estima posible la implementación de la IA en las <br> bibliotecas universitarias?",
    )
    st.markdown(
        """Esta pregunta está correlacionada con la anterior puesto que es completamente proporcional en el número de respuestas positivas y negativas.
        Esta respuesta se da independiente de factores que son útiles de considerar a la hora de aplicar dicha tecnología, ya que más adelante en la encuesta
        se plantea la pregunta por los factores claves de aplicación."""
    )
elif (
    dropdown
    == "¿Usa o usaría está herramienta (IA) en su biblioteca para realizar labores propias de esta?"
):
    create_pie_chart(
        df,
        "uso_de_IA",
        "¿Usa o usaría está herramienta (IA) en su biblioteca para realizar <br> labores propias de esta?",
    )
    st.markdown(
        """Respecto a las respuestas a esta interrogante, podemos ver que no se usan, por parte de ninguno de los encuestados, tecnologías de IA asociadas a
        las llamadas “Área de procesos técnicos y metadatos”, de “Desarrollo de colecciones” y de “Referencia”, proceso internos que sí se consideran susceptibles
        de mejorar con IA y que ,además, existe una amplia aceptación en su disposición a usarla. Solo un porcentaje bajo (menos del 8%) considera que no es adecuado
        usar IA en los mencionados procesos. Esto, nos puede dar luces de las respuestas a las interrogantes sobre el factor recursos humanos a la hora de implementar
        servicios basados en IA, que en las próximas preguntas se tratan más a fondo."""
    )
