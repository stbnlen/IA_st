import streamlit as st
from stop_words import get_stop_words
import stylecloud
from PIL import Image


def get_all_answers(df, column):
    return "".join(df[column][i] for i, j in enumerate(df[column]))


@st.cache_resource
def make_cloud(answers, name):
    with open(f"clouds/{name}.txt", "w", encoding="utf-8") as f:
        f.write(answers)

    palabras_irr = get_stop_words("spanish")

    stylecloud.gen_stylecloud(
        file_path=f"clouds/{name}.txt",
        icon_name="fas fa-cloud",
        output_name=f"clouds/{name}.png",
        custom_stopwords=palabras_irr,
        collocations=False,
    )

    palabras_irr = get_stop_words("spanish")

    image = Image.open(f"clouds/{name}.png")
    return image
