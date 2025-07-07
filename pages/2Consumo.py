import streamlit as st
from assets.components.header import header, subheader, title
from assets.components.title_graphs import title_graph
from funciones.data_loader import load_data
from funciones.consumo.grafica1 import graph_consumo
from funciones.consumo.asegurados import graph1, graph2

st.set_page_config(
    page_title="Producto Interno Bruto",
    layout="wide"
)

def consumo_page():
    df3 = load_data()[3]
    df4 = load_data()[4]
    df5 = load_data()[5]

    header("Consumo")
    subheader("Análisis del Consumo")
    
    title_graph("Evolucion del Consumo privado y su variación anual", 
            "(2018 = 100 | %)")
    st.plotly_chart(graph_consumo(df3), use_container_width=True)

    st.divider()

    title_graph("Asegurados", 
            "(numero de asegurados | %)")
    st.plotly_chart(graph1(df4), use_container_width=True)

    st.divider()

    title_graph("Asegurados por entidad", 
            "(numero de asegurados | %)")
    st.plotly_chart(graph2(df5), use_container_width=True)


if __name__ == "__main__":
    consumo_page()