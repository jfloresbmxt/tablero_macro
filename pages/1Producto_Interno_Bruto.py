import streamlit as st
from assets.components.header import header, subheader, title
from assets.components.title_graphs import title_graph
from funciones.data_loader import load_pib_data
from funciones.pib.grafica1 import graph1
from funciones.pib.grafica2 import graph2
from funciones.pib.grafica2_1 import graph2_1
from funciones.pib.grafica3 import graph3, graph3_1

st.set_page_config(
    page_title="Producto Interno Bruto",
    layout="wide"
)

def pib_page():
    df, df1, df2 = load_pib_data()

    header("Producto Interno Bruto")
    subheader("Análisis del Producto Interno Bruto (PIB): composición por sectores y entidades federativas")

    title_graph("Evolucion del PIB y su variación anual", 
                "(Millones de pesos | %)")

    st.plotly_chart(graph1(df), use_container_width=True)

    title("PIB por sector económico")

    tab1, tab2 = st.tabs(["Barras", "Burbujas"])

    with tab1:
        title_graph("Participacion del PIB por sector económico", 
                "(Millones de pesos)")
        st.plotly_chart(graph2(df1), use_container_width=True)

    with tab2:
        title_graph("Participacion del PIB y TMAC por sector economico", 
                "(Millones de pesos | %)")
        st.plotly_chart(graph2_1(df1), use_container_width=True)

    st.divider()

    title("PIB por entidad federativa")

    tab1, tab2 = st.tabs(["Barras", "Burbujas"])

    with tab1:
        title_graph("Participacion del PIB por entidad federativa", 
                "(Millones de pesos)")
        st.plotly_chart(graph3(df2), use_container_width=True)

    with tab2:
        title_graph("Participacion del PIB y TMAC por entidad federativa", 
                "(Millones de pesos | %)")
        st.plotly_chart(graph3_1(df2), use_container_width=True)

if __name__ == "__main__":
    pib_page()