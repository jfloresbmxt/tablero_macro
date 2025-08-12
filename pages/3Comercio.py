import streamlit as st
from assets.components.header import header, subheader, title
from assets.components.title_graphs import title_graph
from funciones.data_loader import load_trade_data
from funciones.comercio.balanza import balanza



st.set_page_config(
    page_title="Comercio",
    layout="wide"
)

def trade_page():
    df = load_trade_data()

    header("Comercio")
    subheader("Análisis del Comercio")
    
    var = st.radio("Seleccionar tipo de bien",
        ["Total", "Consumo", "Intermedios", "Capital"],
        horizontal=True
    )

    choose = {
    "Total":["Importaciones", "Exportaciones"],
    "Consumo": ["Exportacion bienes consumo", "Importacion bienes consumo"],
    "Intermedios": ["Exportacion bienes intermedios", "Importacion bienes intermedios"],
    "Capital": ["Exportacion bienes capital", "Importacion bienes capital"],
    }
    
    title_graph(f"Evolucion de la balanza comercial bienes {var}", 
            "(millones de dolares)")
    st.plotly_chart(balanza(df,choose[var]))



if __name__ == "__main__":
    trade_page()