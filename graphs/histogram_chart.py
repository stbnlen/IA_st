import pandas as pd
import streamlit as st
import plotly.subplots as sp
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def library_distribution(df: pd.DataFrame, num_bins: int) -> None:
    # Crear los subplots con 1 fila y 2 columnas
    fig = sp.make_subplots(rows=1, cols=2)

    # Crear el gráfico de violín en el primer subplot con transparencia (opacidad) de 0.7
    FILL_COLOR = "#636EFA"

    fig.add_trace(
        go.Violin(
            x=df["nro_bibliotecas"],
            box_visible=True,
            line_color="black",
            points="all",
            fillcolor=FILL_COLOR,
            opacity=0.7,
        ),
        row=1,
        col=1,
    )

    # Configurar el título y etiquetas de los ejes del primer subplot
    fig.update_xaxes(title_text="Número de Bibliotecas", row=1, col=1)
    fig.update_yaxes(
        title_text="", showticklabels=False, row=1, col=1
    )  # Mostrar tick labels en el eje x solamente

    # Crear el gráfico de histograma en el segundo subplot
    fig.add_trace(
        go.Histogram(
            x=df["nro_bibliotecas"],
            nbinsx=num_bins,
            text=df["nro_bibliotecas"],
            marker_color="rgba(99, 110, 250, 0.7)",
            opacity=0.7,
        ),
        row=1,
        col=2,
    )

    # Configurar el título y etiquetas de los ejes del segundo subplot
    fig.update_xaxes(title_text="Número de Bibliotecas", row=1, col=2)
    fig.update_yaxes(title_text="Instituciones", row=1, col=2)

    # Agregar contorno negro a las barras del histograma
    fig.update_traces(
        marker_line_color="rgb(0,0,0)", marker_line_width=1.5, opacity=0.9, row=1, col=2
    )

    # Configurar el diseño de la figura y mostrarla
    CHART_WIDTH = 870
    CHART_HEIGHT = 400

    fig.update_layout(
        title="Distribución de Número de Bibliotecas",
        showlegend=False,
        width=CHART_WIDTH,
        height=CHART_HEIGHT,
    )

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
        fig.add_trace(go.Histogram(x=df[col], texttemplate="%{y}"), row=1, col=i + 1)

    # Actualizar el diseño del gráfico, incluyendo el título, leyenda, altura y anchura
    fig.update_layout(
        showlegend=False,
        height=450,
        width=850,
        title_text="¿Qué impacto tendría la IA en alguno de los siguientes aspectos <br> de su biblioteca?",
        title_font=dict(size=18),
        xaxis_title="Nivel de Impacto",
        yaxis_title="Frecuencia",
        font=dict(size=12),
    )

    # Actualizar las propiedades de las barras en los histogramas, incluyendo el color del borde y la opacidad
    fig.update_traces(
        marker_line_color="rgb(0,0,0)", marker_line_width=1.5, opacity=0.9
    )

    # Mostrar el gráfico
    st.plotly_chart(fig)
