import streamlit as st
import plotly.graph_objects as go
from typing import Tuple, List


def create_bar_charts(aspectos: Tuple[str], values: List[int], titulo: str):
    # Crear la figura del gráfico de barras
    fig = go.Figure()

    # Añadir barras al gráfico
    fig.add_trace(
        go.Bar(
            x=aspectos,
            y=values,
            text=[f"{round(i*100/14, 1)}%" for i in values],
            textposition="auto",
            opacity=0.9,
        )
    )

    # Configurar el título del gráfico
    fig.update_layout(
        title=titulo,
        xaxis_title="",
        yaxis_title="Instituciones",
        title_font=dict(size=24),
    )

    # Configurar las etiquetas del eje x
    fig.update_xaxes(tickangle=-45, tickfont=dict(size=12))

    # Configurar las etiquetas del eje y
    fig.update_yaxes(tickfont=dict(size=12))

    fig.update_traces(marker=dict(line=dict(color="#000000", width=2)))

    # Mostrar el gráfico
    st.plotly_chart(fig)
