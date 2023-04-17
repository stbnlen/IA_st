import math
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from typing import Dict

new_names: Dict[str, str] = {
    "Indique su institución": "institucion",
    "Indique la cantidad de Bibliotecas en su institución": "nro_bibliotecas",
    "¿En su biblioteca existen software que dispongan de elementos asociados a la Inteligencia Artificial?. Por ejemplo: servicios de descubrimiento, chats.":"servicios_IA",
    "¿Se tienen planes a futuro para la implementación de IA en su biblioteca?":"planes_a_futuro",
    "¿Estima posible la implementación de la IA en las bibliotecas universitarias actualmente? ":"posible_Implementacion",
    "¿Qué aspectos considera que son relevantes en la implementación de IA en su biblioteca?. Puede seleccionar más de una.":"aspectos_relevantes",
    "Tomando en consideración aspectos como la atención al usuario, los servicios de la biblioteca, mejora de procesos internos de las bibliotecas, los trabajadores de las bibliotecas, entre otros. ¿Qué impacto cree que generaría la implementación de IA dentro de las  bibliotecas?. Puede seleccionar más de una.":"impacto_IA",
    "¿Qué nuevas tecnologías basadas en IA ha implementado o considera implementar en su biblioteca?. Puede seleccionar más de una.":"nuevas_tecnologias",
    "Entendiendo el aprendizaje automático como un tipo de IA que proporciona a las computadoras la capacidad de aprender, sin ser programadas explícitamente. ¿Usa o usaría está herramienta en su biblioteca para realizar labores propias de esta tales como: desarrollar las colecciones, recuperar información, agregar metadatos?":"uso_de_IA",
    "Ha adoptado o adoptaría alguna de las siguientes tecnologías en su biblioteca. Puede seleccionar más de una": "adopcion_de_tecnologia",
    "Tomando en consideración los próximos 10 años, ¿qué impacto tendría la IA en alguno de los siguientes aspectos de su biblioteca? ( Considere que 1 es poco impacto y 5 alto impacto) [Internet de las cosas]":"impacto_en_bibliotecas_iot",
    "Tomando en consideración los próximos 10 años, ¿qué impacto tendría la IA en alguno de los siguientes aspectos de su biblioteca? ( Considere que 1 es poco impacto y 5 alto impacto) [Acceso Abierto]":"impacto_en_bibliotecas_open",
    "Tomando en consideración los próximos 10 años, ¿qué impacto tendría la IA en alguno de los siguientes aspectos de su biblioteca? ( Considere que 1 es poco impacto y 5 alto impacto) [Software Libre]":"impacto_en_bibliotecas_libre",
    "Tomando en consideración los próximos 10 años, ¿qué impacto tendría la IA en alguno de los siguientes aspectos de su biblioteca? ( Considere que 1 es poco impacto y 5 alto impacto) [Política Nacional sobre avances tecnológicos (como la IA)]":"impacto_en_bibliotecas_politica",
    "Tomando en consideración los próximos 10 años, ¿qué impacto tendría la IA en alguno de los siguientes aspectos de su biblioteca? ( Considere que 1 es poco impacto y 5 alto impacto) [Asesores virtuales para estudiantes]":"impacto_en_bibliotecas_asesores",
    "Tomando en consideración los próximos 10 años, ¿qué impacto tendría la IA en alguno de los siguientes aspectos de su biblioteca? ( Considere que 1 es poco impacto y 5 alto impacto) [Protección de datos personales]":"impacto_en_bibliotecas_datos_personales",
    "Tomando en consideración los próximos 10 años, ¿qué impacto tendría la IA en alguno de los siguientes aspectos de su biblioteca? ( Considere que 1 es poco impacto y 5 alto impacto) [Privacidad de la información]":"impacto_en_bibliotecas_privacidad",
    "Tomando en consideración los próximos 10 años, ¿qué impacto tendría la IA en alguno de los siguientes aspectos de su biblioteca? ( Considere que 1 es poco impacto y 5 alto impacto) [Derechos de autor]":"impacto_en_bibliotecas:derechosautor",
    "Tomando en consideración los próximos 10 años, ¿qué impacto tendría la IA en alguno de los siguientes aspectos de su biblioteca? ( Considere que 1 es poco impacto y 5 alto impacto) [Recursos educacionales de acceso abierto a través de internet]":"impacto_en_bibliotecas_internet",
    "Tomando en consideración los próximos 10 años, ¿qué impacto tendría la IA en alguno de los siguientes aspectos de su biblioteca? ( Considere que 1 es poco impacto y 5 alto impacto) [Inteligencia artificial]":"impacto_en_bibliotecas_ia",
    "Tomando en consideración los próximos 10 años, ¿qué impacto tendría la IA en alguno de los siguientes aspectos de su biblioteca? ( Considere que 1 es poco impacto y 5 alto impacto) [Humanidades digitales]":"impacto_en_bibliotecas_humanidades",
    "¿Considera que su biblioteca está preparada para los cambios que podría traer el avance de la tecnología de IA?":"cambios_en_biblioteca",
    "Considerando lo anterior ¿ante los constantes y acelerados avances en la tecnología y los modelos de IA, piensa que es posible capacitar al equipo de la biblioteca en sus usos?":"posible_capacitacion",
    "¿Considera usted que sistemas automatizados o máquinas inteligentes pueden reemplazar a los equipos de biblioteca?":"posibilidad_reemplazo"
}

def freedman_diaconis_bindwidth(x: pd.Series) -> float:
            """Find optimal bandwidth using Freedman-Diaconis rule."""
            IQR = x.quantile(0.75) - x.quantile(0.25)
            N = x.size
            return 2 * IQR / N ** (1 / 3)


def nbins(x: pd.Series, nb: float) -> float:
            return math.ceil((x.max() - x.min()) / nb)


def library_distribution(df: pd.DataFrame, nbins):
    # Crear los subplots con 1 fila y 2 columnas
    fig = sp.make_subplots(rows=1, cols=2)

    # Crear el gráfico de violín en el primer subplot con transparencia (opacidad) de 0.7
    fig.add_trace(
        go.Violin(x=df['nro_bibliotecas'], box_visible=True, line_color='black', points='all', 
                  fillcolor='#636EFA', opacity=0.7),
        row=1, col=1
    )

    # Configurar el título y etiquetas de los ejes del primer subplot
    fig.update_xaxes(title_text="Número de Bibliotecas", row=1, col=1)
    fig.update_yaxes(title_text="", showticklabels=False, row=1, col=1)  # Mostrar tick labels en el eje x solamente

    # Crear el gráfico de histograma en el segundo subplot
    fig.add_trace(
        go.Histogram(x=df['nro_bibliotecas'], nbinsx=nbins, text=df['nro_bibliotecas'], 
                     marker_color='rgba(99, 110, 250, 0.7)', opacity=0.7),
        row=1, col=2
    )

    # Configurar el título y etiquetas de los ejes del segundo subplot
    fig.update_xaxes(title_text="Número de Bibliotecas", row=1, col=2)
    fig.update_yaxes(title_text="Instituciones", row=1, col=2)

    # Agregar contorno negro a las barras del histograma
    fig.update_traces(marker_line_color='rgb(0,0,0)',
                      marker_line_width=1.5, opacity=0.9, row=1, col=2)

    # Configurar el diseño de la figura y mostrarla
    fig.update_layout(
        title="Distribución de Número de Bibliotecas",
        showlegend=False,
        width=870,
        height=400
    )

    st.plotly_chart(fig)


def create_pie_chart(df, column, title):
    # Obtener los conteos de "Si" y "No"
    yes = df[column].value_counts()[0]
    no = df[column].value_counts()[1]

    # Crear la figura del gráfico de pastel
    fig = px.pie(df[column], values=[yes, no], names=["Si", "No"], title=title)

    # Configurar el título del gráfico
    fig.update_layout(
        title_font=dict(size=24),
        width=870,
        height=400
    )

    # Configurar el color de línea del marcador
    fig.update_traces(
        hoverinfo='label+percent',
        textfont_size=20,
        marker=dict(line=dict(color='#000000', width=2))
    )

    # Mostrar el gráfico
    st.plotly_chart(fig)


def create_bar_charts(aspectos, values, titulo):
    # Crear la figura del gráfico de barras
    fig = go.Figure()

    # Añadir barras al gráfico
    fig.add_trace(go.Bar(x=aspectos, y=values, text=[f'{round(i*100/14, 1)}%' for i in values],
                    textposition='auto', opacity=0.9))

    # Configurar el título del gráfico
    fig.update_layout(title=titulo,
                  xaxis_title="", yaxis_title="Instituciones", title_font=dict(size=24))

    # Configurar las etiquetas del eje x
    fig.update_xaxes(tickangle=-45, tickfont=dict(size=12))

    # Configurar las etiquetas del eje y
    fig.update_yaxes(tickfont=dict(size=12))

    fig.update_traces(
        marker=dict(line=dict(color='#000000', width=2))
    )

    # Mostrar el gráfico
    st.plotly_chart(fig)


def create_histogram_subplots(df, colums, titles):
    """
    Crea subplots de histogramas con datos de un DataFrame.
    
    Args:
    - df (pd.DataFrame): DataFrame con los datos para los histogramas.
    - cols (list): Lista de nombres de columnas del DataFrame para los histogramas.
    - titles (list): Lista de títulos para cada subplot.
    
    Returns:
    - fig (plotly.graph_objects.Figure): Figura con los subplots de histogramas.
    """
    # Crear subplots con 1 fila y 3 columnas, y agregar títulos a cada subplot
    fig = make_subplots(rows=1, cols=3, subplot_titles=titles)

    # Agregar histogramas a cada subplot con datos de las columnas correspondientes del DataFrame "df"
    for i, col in enumerate(colums):
        fig.add_trace(go.Histogram(x=df[col], texttemplate="%{y}"), row=1, col=i+1)

    # Actualizar el diseño del gráfico, incluyendo el título, leyenda, altura y anchura
    fig.update_layout(
        showlegend=False,
        height=450,
        width=850,
        title_text="¿Qué impacto tendría la IA en alguno de los siguientes aspectos <br> de su biblioteca?",
        title_font=dict(size=18),
        xaxis_title="Nivel de Impacto",
        yaxis_title="Frecuencia",
        font=dict(size=12)
    )

    # Actualizar las propiedades de las barras en los histogramas, incluyendo el color del borde y la opacidad
    fig.update_traces(
        marker_line_color='rgb(0,0,0)',
        marker_line_width=1.5,
        opacity=0.9
    )

    # Mostrar el gráfico
    st.plotly_chart(fig)


def create_pie_chart_two(df):
    fig = px.pie(df, values=df["posible_capacitacion"].value_counts(), names=["Sí, pienso que es posible capacitar al personal"],
                 title='¿Piensa que es posible capacitar al equipo de la biblioteca en sus <br> usos?')
    fig.update_traces(hoverinfo='label+percent', textfont_size=20,
                      marker=dict(line=dict(color='#000000', width=2)))
    st.plotly_chart(fig)


def create_pie_chart_three(df):
    yes = df["posibilidad_reemplazo"].value_counts()[1]
    no = df["posibilidad_reemplazo"].value_counts()[0]
    otro = df["posibilidad_reemplazo"].value_counts()[2] + df["posibilidad_reemplazo"].value_counts()[3] + df["posibilidad_reemplazo"].value_counts()[4] + df["posibilidad_reemplazo"].value_counts()[5]

    labels = ["Sí, aunque será un cambio paulatino", "No, el servicio dado por personas es irremplazable", "Otro"]
    values = [yes, no, otro]

    fig = px.pie(df, values=values, names=labels,
                 title="¿Considera usted que sistemas automatizados puedan <br> reemplazar a los equipos de biblioteca?")
    fig.update_traces(hoverinfo='label+percent', textfont_size=20,
                      marker=dict(line=dict(color='#000000', width=2)))
    st.plotly_chart(fig)