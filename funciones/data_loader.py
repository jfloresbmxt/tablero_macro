import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_excel("data/pib_graph1.xlsx", dtype={"year":str})
    df1 = pd.read_excel("data/pib_graph2.xlsx", dtype={"year":str})
    df2 = pd.read_excel("data/pib_graph3.xlsx")
    df3 = pd.read_excel("data/consumo_graph.xlsx")
    df4 = pd.read_excel("data/asegurados_graph1.xlsx")
    df5 = pd.read_excel("data/asegurados_graph2.xlsx")

    return [df, df1, df2, df3, df4, df5]