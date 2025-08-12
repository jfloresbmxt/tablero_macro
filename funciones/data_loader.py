import pandas as pd
import streamlit as st

@st.cache_data
def load_pib_data():
    df = pd.read_excel("data/pib_graph1.xlsx", dtype={"year":str})
    df1 = pd.read_excel("data/pib_graph2.xlsx", dtype={"year":str})
    df2 = pd.read_excel("data/pib_graph3.xlsx")

    return [df, df1, df2]

@st.cache_data
def load_consumo_data():
    df = pd.read_excel("data/consumo_graph.xlsx")
    df1 = pd.read_excel("data/asegurados_graph1.xlsx")
    df2 = pd.read_excel("data/asegurados_graph2.xlsx")
    df3 = pd.read_excel("data/asegurados_graph3.xlsx")

    return [df, df1, df2, df3]


@st.cache_data
def load_remesas_data():
    df = pd.read_excel("data/remesas_graph1.xlsx")
    df1 = pd.read_excel("data/remesas_graph2_3.xlsx")

    return [df, df1]


@st.cache_data
def load_trade_data():
    df = pd.read_excel("data/balanza/balanza_comercial.xlsx")

    return df