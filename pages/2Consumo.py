import streamlit as st
from assets.components.header import header, subheader, title
from assets.components.title_graphs import title_graph
from funciones.data_loader import load_consumo_data, load_remesas_data
from funciones.consumo.grafica1 import graph_consumo
from funciones.consumo.asegurados import graph1, graph2, graph3
from funciones.remesas.remesas import remesas_bar, remesas_line, remesas_map

st.set_page_config(
    page_title="Producto Interno Bruto",
    layout="wide"
)

def consumo_page():
    df, df1, df2, df3 = load_consumo_data()
    df4, df5 = load_remesas_data()

    header("Consumo")
    subheader("Análisis del Consumo")
    
    title_graph("Evolucion del Consumo privado y su variación anual", 
            "(2018 = 100 | %)")
    st.plotly_chart(graph_consumo(df), use_container_width=True)

    st.divider()

    title_graph("Asegurados totales del IMSS", 
            "(número de asegurados | %)")
    st.plotly_chart(graph1(df1), use_container_width=True)

    st.divider()
  
    tab1, tab2 = st.tabs(["Barras", "Tops"])
    
    with tab1:
        title_graph("Asegurados totales del IMSS por entidad", 
            "(número de asegurados)")
        st.plotly_chart(graph2(df2), use_container_width=True)
    with tab2:
        title_graph("Entidades con mayores cambios en el número de asegurados en lo que va del año")
        st.plotly_chart(graph3(df3), use_container_width=True)
    
    st.divider()

    title_graph("Evolución de las remesas", 
            "(Millones de UDS | %)")
    
    st.plotly_chart(remesas_line(df4), use_container_width=True)
    tab1, tab2 = st.tabs(["Mapa", "Barras"])
    
    with tab1:
        title_graph("Remesas recibidas por entidad federativa", 
            "(Millones de UDS)")
        st.plotly_chart(remesas_map(df5), use_container_width=True)
    with tab2:
        title_graph("Remesas recibidas por entidad federativa", 
            "(Millones de UDS)")
        st.plotly_chart(remesas_bar(df5), use_container_width=True)

if __name__ == "__main__":
    consumo_page()