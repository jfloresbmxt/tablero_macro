import streamlit as st
from streamlit_extras.stylable_container import stylable_container

STYLES ={
    "main_box": """
         h2 {
            background-color: rgb(212, 193, 156);
            color: black;
            border: 2px solid rgb(212, 193, 156);
            border-radius: 1rem;
            font-size: 1.5rem;
            padding: 0.3em 0.5em;
            margin-bottom: 0.5rem;
            text-align: center;
            box-sizing: border-box;
        }
    """,
    "text_box": """
         h2 {
            background-color: rgb(227, 222, 209);
            color: black;
            border: 2px solid rgb(227, 222, 209);
            border-radius: 0.5rem;
            font-size: 1rem;
            padding: 0.35em 0.5em;
            margin-bottom: 0.22rem;
            text-align: center;
            box-sizing: border-box;
        }
    """,
}

def box_titulo(text, key="container_main_box"):
    # Customizing two elements in the same container.
    with stylable_container(
        key=key,
        css_styles=STYLES["main_box"],
        ):
            st.markdown(f"<h2>{text}</h2>", unsafe_allow_html=True)

def box_text(text, key="container_main_box"):
    # Customizing two elements in the same container.
    with stylable_container(
        key=key,
        css_styles=STYLES["text_box"],
        ):
            st.markdown(f"<h2>{text}</h2>", unsafe_allow_html=True)