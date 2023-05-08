import pandas as pd
import streamlit as st
import plotly.express as px


def create_pie_chart(df: pd.DataFrame, column: str, title: str) -> None:
    # Obtener los conteos de "Si" y "No"
    counts = df[column].value_counts()
    yes = counts[0]
    no = counts[1]

    # Crear la figura del gráfico de pastel
    fig = px.pie(df[column], values=[yes, no], names=["Si", "No"], title=title)

    # Configurar el título del gráfico
    TITLE_SIZE = 24
    FIG_WIDTH = 870
    FIG_HEIGHT = 400

    fig.update_layout(
        title_font=dict(size=TITLE_SIZE), width=FIG_WIDTH, height=FIG_HEIGHT
    )

    # Configurar el color de línea del marcador
    fig.update_traces(
        hoverinfo="label+percent",
        textfont_size=20,
        marker=dict(line=dict(color="#000000", width=2)),
    )

    # Mostrar el gráfico
    st.plotly_chart(fig)


def create_pie_chart_two(df: pd.DataFrame):
    fig = px.pie(
        df,
        values=df["posible_capacitacion"].value_counts(),
        names=["Sí, pienso que es posible capacitar al personal"],
        title="¿Piensa que es posible capacitar al equipo de la biblioteca en sus <br> usos?",
    )
    fig.update_traces(
        hoverinfo="label+percent",
        textfont_size=20,
        marker=dict(line=dict(color="#000000", width=2)),
    )
    st.plotly_chart(fig)


def create_pie_chart_three(df: pd.DataFrame):
    yes = df["posibilidad_reemplazo"].value_counts()[1]
    no = df["posibilidad_reemplazo"].value_counts()[0]
    otro = (
        df["posibilidad_reemplazo"].value_counts()[2]
        + df["posibilidad_reemplazo"].value_counts()[3]
        + df["posibilidad_reemplazo"].value_counts()[4]
        + df["posibilidad_reemplazo"].value_counts()[5]
    )

    labels = [
        "Sí, aunque será un cambio paulatino",
        "No, el servicio dado por personas es irremplazable",
        "Otro",
    ]
    values = [yes, no, otro]

    fig = px.pie(
        df,
        values=values,
        names=labels,
        title="¿Considera usted que sistemas automatizados puedan <br> reemplazar a los equipos de biblioteca?",
    )
    fig.update_traces(
        hoverinfo="label+percent",
        textfont_size=20,
        marker=dict(line=dict(color="#000000", width=2)),
    )
    st.plotly_chart(fig)
