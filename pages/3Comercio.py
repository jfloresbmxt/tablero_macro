import streamlit as st
from assets.components.header import header, subheader, title
from assets.components.title_graphs import title_graph
from funciones.data_loader import load_trade_data, load_trade_states_data
from funciones.comercio.balanza import balanza
from funciones.comercio.sector import sector_barras, sector_serie, sector_barras_v2
from funciones.comercio.entidades import mapa, bar_ent, composicion



st.set_page_config(
    page_title="Comercio",
    layout="wide"
)

def trade_page():
    df, df1, sectores, df2 = load_trade_data()
    df3 , df4, geoentidades, df5, entidades = load_trade_states_data()

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
    
    title_graph(f"Evolución de la balanza comercial - bienes de {var}", 
            "(Miles de millones de dólares)")
    
    st.plotly_chart(balanza(df,choose[var]))

    st.divider()

    title("Exportaciones por sector económico")

    tab1, tab2 = st.tabs(["Barras", "Evolución Barras"])

    with tab1:
        title_graph("Exportaciones por sector económico, 2024", 
            "(Millones de dolares)")
        st.plotly_chart(sector_barras(df1), use_container_width=True)
    with tab2:
        title_graph("Evolución de las exportaciones por sector anual",
                    "(Millones de dolares | %)")
        option = st.selectbox(
            "Selecciona un sector",
            sectores
        )
        st.plotly_chart(sector_barras_v2(df2, option), use_container_width=True)
 
    title("Exportaciones por entidad federativa")
    tab1, tab2, tab3 = st.tabs(["Mapa", "Barras", "Composicion"])
    
    with tab1:
        title_graph("Exportaciones por entidad federativa, 1er trimestre 2025", 
            "(Millones de dólares)")
        st.plotly_chart(mapa(df3, geoentidades), use_container_width=True)
    with tab2:
        title_graph("Evolución de exportaciones por entidad federativa, 1er trimestre 2025", 
            "(Millones de dólares)")
        st.plotly_chart(bar_ent(df4), use_container_width=True)
    with tab3:
        ent = st.selectbox(
            "Selecciona una entidad",
            entidades
        )
        title_graph("Composición sectorial exportaciones, 1er trimestre 2025", 
            "(Millones de dólares)")
        st.plotly_chart(composicion(df5, ent), use_container_width=True)
        # st.data_editor(composicion(df5, ent))



if __name__ == "__main__":
    trade_page()