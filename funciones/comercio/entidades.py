import pandas as pd
import plotly.graph_objects as go
import json

def mapa(df, geojson):
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"
    
    df["quintil"] = pd.qcut(df["Exportaciones"], 5)
    unique_intervals = sorted(df["quintil"].unique())

    colors = ["rgb(229,233,235)", "rgb(190,199,206)", "rgb(124,143,156)", "rgb(71,85,94)", "rgb(42,49,55)"]
    interval_color_map = dict(zip(unique_intervals, colors))

    interval_label_map = {
        interval: f"{int(interval.left):,} – {int(interval.right):,}"
        for interval in unique_intervals
    }

    df["color"] = df["quintil"].map(interval_color_map)
    df["label"] = df["quintil"].map(interval_label_map)
    unique_intervals = sorted(df["quintil"].unique())
    colors = ["rgb(229,233,235)", "rgb(190,199,206)", "rgb(124,143,156)", "rgb(71,85,94)", "rgb(42,49,55)"]
    interval_color_map = dict(zip(unique_intervals, colors))

    interval_label_map = {
        interval: f"{int(interval.left):,} – {int(interval.right):,}"
        for interval in unique_intervals
    }

    # # Crear figura
    fig = go.Figure()

    # Agregar los estados coloreados
    for _, row in df.iterrows():
        estado = row["entidad"]
        color = row["color"]
        remesa = row["Exportaciones"]
        participacion = row["participacion"]

        over_text = (
        f"<b>{estado}</b><br>"
        f"Exportaciones: {remesa:,.2f}<br>"
        f"Participación: {participacion:.2f}%<extra></extra>"
    )

        for feature in geojson["features"]:
            if feature["properties"]["name"] == estado:
                fig.add_trace(go.Choropleth(
                    geojson={"type": "FeatureCollection", "features": [feature]},
                    locations=[estado],
                    z=[remesa],
                    locationmode="geojson-id",
                    featureidkey="properties.name",
                    colorscale=[[0, color], [1, color]],
                    showscale=False,
                    hovertemplate = over_text
                        
    
                ))
                break

    # Leyenda manual con rectángulos
    for interval in unique_intervals:
        label = interval_label_map[interval]
        color = interval_color_map[interval]

        fig.add_trace(go.Scattergeo(
            lon=[None], lat=[None],
            mode='markers',
            marker=dict(size=12, color=color, symbol='square'),
            name=label,
            showlegend=True
        ))

    # Layout sin fondo en la leyenda
    fig.update_layout(
        geo=dict(
            scope='north america',
            projection_scale=4.5,
            center=dict(lat=23, lon=-102),
            showcountries=False,
            showcoastlines=False,
            showland=True,
            showocean=True,
            oceancolor="white",
            landcolor="white",
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        height=700,
        showlegend=True,
        hoverlabel=dict(
            font_size=SIZE_TEXT,
            font_family=FONT_FAMILY,
            font_color=COLOR_FONT,
            bordercolor="gray"),
        legend=dict(
            title=dict(
            text = "Exportaciones (millones de dólares)",      # <— texto del título de la leyenda
            font = dict(
                family="Noto Sans",
                size=SIZE_TEXT + 2,
                color=COLOR_FONT      # <— color del título
            )),
            y=0.6,
            x=0.66,
            bordercolor="black",
            borderwidth=.1,
            font=dict(size=SIZE_TEXT,
                      color = COLOR_FONT)
        ),
        font = dict(family = FONT_FAMILY, 
                  color = COLOR_FONT,
                  size = SIZE_TEXT
                  )
    )

    return fig


def bar_ent(df):
    COLOR_BAR = "rgb(229, 233, 235)"
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x = df["2025/01"],
            y = df["entidad"],
            orientation = "h",
            marker_color = COLOR_BAR,
            text = df["2025/01"].apply(lambda x: f"{x:,.0f}"),
            # textposition = "inside",
            textfont = dict(
                color = COLOR_FONT,
                size = SIZE_TEXT
            ),
            insidetextanchor = "start",
            customdata = df[["entidad", "2025/01", "participacion", "tmac", "crec_anual"]],
            hovertemplate = (
                "<b>%{customdata[0]}</b> <br>" +
                "<b>Exportaciones:</b> %{customdata[1]:,.0f}<br>" +
                "<b>Participación:</b> %{customdata[2]:.2f}%<br>" +
                "<b>Crecimiento anual:</b> %{customdata[3]:.2f}%<br>" +
                "<b>TMAC 2018-2025:</b> %{customdata[4]:.2f}%<extra></extra>"
                )
        )
    )

    fig.update_layout(
        height = 800,
        bargap = 0.1,
        xaxis = dict(
            title = dict(
                text = "", 
                font = dict(
                    color=COLOR_FONT
                    )),
            tickfont = dict(
                color=COLOR_FONT
                ),
            showticklabels=False,
            showgrid = False,
        ),
        yaxis = dict(
            tickfont = dict(color=COLOR_FONT,
                            size = SIZE_TEXT),
            showgrid = False,
            fixedrange = False,
            automargin = True,
            autorange = 'reversed',
            ),
        showlegend = False,
        template = "plotly_white",
        margin = dict(t=10, l=0, r=0, b=0),
        font = dict(family = FONT_FAMILY, 
                  color = COLOR_FONT,
                  size = SIZE_TEXT
                  ),
        hoverlabel=dict(
            font_size=SIZE_TEXT,
            font_family=FONT_FAMILY,
            font_color=COLOR_FONT,
            bordercolor="gray"
    )
    )

    return fig


def summarize_entity(df,entidad):
    df_e = df[df["entidad"] == entidad].copy()
    total = df_e.query("sector == '00'")["2025/01"].iloc[0]
    df_e = df_e.query("sector != '00'")
    df_e["participacion"] = df_e["2025/01"] / total * 100
    df_e = df_e.sort_values("participacion", ascending=False)
    df_e["acum"] = df_e["participacion"].cumsum()

    top = df_e.query("acum <= 95").drop(columns="acum")
    resto = (
        df_e.query("acum > 95")
            .groupby("entidad")
            .agg({"2025/01":"sum","participacion":"sum"})
            .reset_index()
    )
    resto["sector"] = "000"
    resto["titulo"] = "Resto de sectores"

    return pd.concat([top, resto])


def composicion(df, entidad):
    COLOR_LINE_1 = "rgb(229, 233, 235)"
    COLOR_LINE_2 = "rgb(190, 199, 206)"
    COLOR_LINE_3= "rgb(124, 143, 156)"
    COLOR_LINE_4 = "rgb(71, 85, 94)"
    COLOR_LINE_5 = "rgb(42, 49, 55)"
    COLOR_BAR = "rgb(124, 143, 156)"
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    df = summarize_entity(df,entidad)
    
    custom_blues = [
        [0.0, COLOR_LINE_1],  # Azul claro
        [0.25, COLOR_LINE_2],  # Azul medio
        [0.5, COLOR_LINE_3],  # Azul medio
        [0.75, COLOR_LINE_4],   # Azul oscuro
        [1.0, COLOR_LINE_5]   # Azul oscuro
    ]
    
    parents = [""] * len(df)

    fig = go.Figure()

    fig.add_trace(
        go.Treemap(
            labels = df["titulo"],
            parents = parents,
             values=df["2025/01"],
             textinfo="label+value+percent parent",
             marker = dict(
                colors = df["2025/01"],
                colorscale = custom_blues,
            ),
            # root_color="white"  # Fondo blanco para el nodo raíz invisible
        )
    )

    fig.update_layout(
        height = 500,
        xaxis = dict(
            title = dict(
                text = "", 
                font = dict(
                    color=COLOR_FONT
                    )),
            tickfont = dict(
                color=COLOR_FONT
                ),
            showticklabels=False,
            showgrid = False,
        ),
        yaxis = dict(
            tickfont = dict(color=COLOR_FONT),
            showgrid = False,
            fixedrange = False,
            automargin = True,
            autorange = 'reversed',
            ),
        showlegend = False,
        template = "plotly_white",
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin = dict(t=0, l=0, r=0, b=0),
        font = dict(family = FONT_FAMILY, 
                  color = COLOR_FONT,
                  size = SIZE_TEXT
                  )
    )

    return fig