import streamlit as st
from PIL import Image
from streamlit_extras.stylable_container import stylable_container

STYLES = {
    "header": """
        h2 {
            background-color: rgb(55, 91, 78);
            font-family: 'Noto Sans';
            color: white;
            border-radius: 0.1rem;
            text-align: center;
            margin:0px 0px 10px;
        }
        header {
            padding: 0px;
            font-size: 1.5rem;
            font-weight: 800;
        }
    """,
    "subheader": """
        h3 {
            background-color: rgb(217, 217, 217);
            font-family: 'Noto Sans';
            color: black;
            border-radius: 0.1rem;
            text-align: center;
            font-size: 20px;
            padding: calc(0.5em - 1px);
        }
    """,
    "title": """
        h3 {
            background-color: #ffffff;
            font-family: 'Noto Sans';
            color: black;
            border-radius: 0.1rem;
            text-align: center;
            font-size: 18px;
            padding: calc(0.5em - 1px);
        }
    """
}

def styled_text(content, key, style_key, level="subheader"):
    with stylable_container(
        key=key,
        css_styles=STYLES[style_key],
    ):
        if level == "header":
            st.header(content)
        elif level == "subheader":
            st.subheader(content)
        else:
            st.markdown(f"### {content}")

def header(sector):
    col1, col2 = st.columns(2)
    with col1:
        styled_text(sector, key="container_header", style_key="header", level="header")
    with col2:
        image = Image.open('assets/Imagen1.png')
        st.image(image)

def subheader(text):
    styled_text(text, key="container_subheader", style_key="subheader")

def title(text):
    styled_text(text, key="container_title", style_key="title")
