import streamlit as st
from assets.components.header import header, subheader, title
from assets.components.title_graphs import title_graph
from funciones.data_loader import load_ied_data
from funciones.ied.evolucion import barras_comparacion
from funciones.ied.composicion_sector import pie_ied_kind


st.set_page_config(
    page_title="IED",
    layout="wide"
)

def ied_page():
    df1 , df2 = load_ied_data()
    
    header("Inversión Extranjera Directa")
    subheader("Análisis de la Inversión Extranjera Directa (IED)")

    var = st.radio("Seleccionar tipo de IED",
        ["Total general", 
         "Nuevas inversiones", 
         "Reinversión de utilidades", 
         "Cuentas entre compañías"],
        horizontal=True
    )

    title_graph(f"Evolución de la IED - {var}", 
            "(Millones de dólares)")
    
    st.plotly_chart(barras_comparacion(df1, var))

    st.divider()

    title("Composición de la IED")
    dates = reversed(df2["date"].unique().tolist())

    date = st.selectbox(
        "Selecciona un trimestre",
        dates
    )

    tab1, tab2, tab3 = st.tabs(["Tipo de inversión", "Sector", "Subsector"])

    with tab1:
        title_graph("Composición de la IED por tipo de inversión, 1er trimestre 2025", 
            "(Millones de dólares)")
        st.plotly_chart(pie_ied_kind(df2, date), use_container_width=True)
    with tab2:
        title_graph("Composición de la IED por tipo de inversión, 1er trimestre 2025", 
            "(Millones de dólares)")
        st.plotly_chart(pie_ied_kind(df2, date), use_container_width=True)
    with tab3:
        title_graph("Composición de la IED por tipo de inversión, 1er trimestre 2025", 
            "(Millones de dólares)")
        st.plotly_chart(pie_ied_kind(df2, date), use_container_width=True)




if __name__ == "__main__":
    ied_page()