import pandas as pd
import streamlit as st
import json

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
    df1 = pd.read_excel("data/balanza/balanza_comercial.xlsx")
    df2 = pd.read_excel("data/balanza/sector1.xlsx")
    df3 = pd.read_excel("data/balanza/sector2.xlsx")
    with open("data/balanza/sectores.json", "r", encoding="utf-8") as f:
        sectores = json.load(f)

    return [df1, df2, sectores, df3]


@st.cache_data
def load_trade_states_data():
    df1 = pd.read_excel("data/balanza/mapa.xlsx")
    df2 = pd.read_excel("data/balanza/entidades.xlsx")
    df3 = pd.read_excel("data/balanza/entidades_comp.xlsx")

    with open("data/balanza/mx_geojson.json", "r", encoding="utf-8") as f:
        geoentidades = json.load(f)
    
    entidades = df3["entidad"].unique().tolist()
    entidades.remove("Nacional")

    return [df1, df2, geoentidades, df3, entidades]


@st.cache_data
def load_ied_data():
    df1 = pd.read_excel("data/ied/ied1.xlsx")
    df2 = pd.read_excel("data/ied/ied2.xlsx")

    return [df1, df2]