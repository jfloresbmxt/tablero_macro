import streamlit as st
from streamlit_extras.stylable_container import stylable_container

STYLES = {
    "title": """
        .line1 {
            font-family: 'Noto Sans';
            font-weight: 600;
            font-size: 18px;
            color: black;
            text-align: center;
            margin: 10px 0 0 0;
        }
        .line2 {
            font-family: 'Noto Sans';
            font-weight: 400;
            font-size: 16px;
            color: #555555;
            text-align: center;
            margin: 0 0 10px 0;
        }
    """
}

def title_graph(line1, line2="", key="container_title_g"):
    with stylable_container(
        key=key,
        css_styles=STYLES["title"]
    ):
        st.markdown(
            f"""
            <div class="line1">{line1}</div>
            <div class="line2">{line2}</div>
            """,
            unsafe_allow_html=True
        )
