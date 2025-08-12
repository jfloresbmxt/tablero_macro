import streamlit as st
from assets.components.header import header, subheader, title
from assets.components.title_graphs import title_graph
from funciones.data_loader import load_trade_data
from funciones.comercio.balanza import balanza
from funciones.comercio.sector import sector_barras, sector_serie



st.set_page_config(
    page_title="Comercio",
    layout="wide"
)

def trade_page():
    df, df1, sectores, df2 = load_trade_data()

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

    st.divider()

    title("Exportaciones por sector económico")

    tab1, tab2 = st.tabs(["Barras", "Serie"])

    with tab1:
        title_graph("Exportaciones por sector económico", 
            "(millones de dolares)")
        st.plotly_chart(sector_barras(df1), use_container_width=True)
    with tab2:
        title_graph("Evolución de las exportaciones por sector",
                    "(millones de dolares)")
        option = st.selectbox(
            "Selecciona un sector",
            sectores
        )
        st.plotly_chart(sector_serie(df2, option), use_container_width=True)



if __name__ == "__main__":
    trade_page()