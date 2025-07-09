import plotly.graph_objects as go
import requests
import pandas as pd

def remesas_line(df):
    COLOR_LINE_2 = "rgb(124, 143, 156)"
    COLOR_LINE_1 = "rgb(71, 85, 94)"
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    # Últimos valores
    last_date = df['date'].iloc[-1]
    last_total = df['remesas'].iloc[-1]
    last_total_pct = df['variacion'].iloc[-1]

    fig = go.Figure()

    # Serie 1: TOTAL (eje primario, izquierdo)
    fig.add_trace(go.Scatter(
        x = df['date'],
        y = df['remesas'],
        name = 'Remesas',
        yaxis = 'y1',
        line = dict(
            color = COLOR_LINE_1 
            ),
        text=df["remesas"].apply(lambda x: f"{x:.2f}"),
        customdata = df[["remesas"]],
        hovertemplate = (
                "<b>Remesas:</b> %{customdata[0]:.2f} mdd<extra></extra>"
                )
    ))

    # Serie 2: TOTAL_pct (eje secundario, derecho)
    fig.add_trace(go.Scatter(
        x = df['date'],
        y = df['variacion'],
        name = 'Variación anual',
        yaxis = 'y2',
        line = dict(
            color=COLOR_LINE_2, 
            dash='dot'
            ),
        text=df["variacion"].apply(lambda x: f"{x:.2f}"),
        customdata = df[["variacion"]],
        hovertemplate = (
                "<b>Variación:</b> %{customdata[0]:.2f}%<extra></extra>"
                )
    ))

    # Punto final para TOTAL
    fig.add_trace(go.Scatter(
        x = [last_date],
        y = [last_total],
        mode = "markers",
        marker = dict(color=COLOR_LINE_1, size=8, symbol='circle'),
        showlegend = False,
        hoverinfo = 'skip'
    ))

    # Punto final para TOTAL_pct
    fig.add_trace(go.Scatter(
        x = [last_date],
        y = [last_total_pct],
        mode = "markers",
        marker = dict(color=COLOR_LINE_2, size=8, symbol='diamond'),
        yaxis = "y2",
        showlegend = False,
        hoverinfo = 'skip'
    ))

    # Anotación para TOTAL
    fig.add_annotation(
        x = last_date,
        y = last_total,
        text = f"{last_total:,.0f}",
        yanchor = "bottom",
        showarrow = False,
        bordercolor = COLOR_LINE_1,
        borderpad = 4,
    )

    # Anotación para TOTAL_pct
    fig.add_annotation(
        x = last_date,
        y = last_total_pct,
        text = f"{last_total_pct:.2f}%",
        yanchor = "auto",
        yref = "y2",
        showarrow = False,
        bordercolor = COLOR_LINE_2,
        borderpad = 4,
    )

    fig.update_layout(
        height = 500,
        font = dict(
            family = FONT_FAMILY,
            size = SIZE_TEXT,
            color = "black"
        ),
        xaxis = dict(
            tickfont = dict(
                family = FONT_FAMILY,
                size = SIZE_TEXT,
                color = COLOR_FONT
            ),
            title_font = dict(
                family = FONT_FAMILY,
                size = SIZE_TEXT,
                color = COLOR_FONT
            ),
            showgrid = False,
            title_text = "Fecha",
            type = "date",
            range=["2018-01", "2025-06"],
            rangeslider = dict(visible=False),
            rangeselector = dict(
                buttons = list([
                    dict(count = 5, label = "5 años", step = "year", stepmode = "backward"),
                    dict(count = 10, label = "10 años", step = "year", stepmode = "todate"),
                    dict(count = 15, label = "15 años", step = "year", stepmode = "todate"),
                    dict(count = 20, label = "20 años", step = "year", stepmode = "todate"),
                ])
            )
        ),
        yaxis = dict(
            tickfont = dict(color=COLOR_FONT),
            showgrid=False
            ),
        yaxis2=dict(
            tickfont=dict(color=COLOR_FONT),
            overlaying="y",
            side="right",
            showgrid=False
        ),
        margin=dict(t=10, l=10, r=10, b=10),
        showlegend = True, 
        template="plotly_white",
        hovermode="x unified",
        hoverlabel=dict(
            font_size=SIZE_TEXT,
            font_family=FONT_FAMILY,
            font_color=COLOR_FONT,
            bordercolor="gray"
    ),
    legend = dict(
            orientation = "h",
            yanchor = "bottom",
            y = 1.12,  # Ajusta para posicionar más arriba si hace falta
            xanchor = "center",
            x = 0.5
        ),
    )

    return fig


def remesas_map(df):
    # Cargar GeoJSON de los estados de México
    url = "https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json"
    geojson = requests.get(url).json()

    # Suponiendo que ya tienes el DataFrame `df` con columnas 'Entidad' y 'Remesas'
    # df = pd.DataFrame(...)

    # Crear quintiles, etiquetas y colores
    df["quintil"] = pd.qcut(df["Remesas"], 5)
    unique_intervals = sorted(df["quintil"].unique())

    colors = ["rgb(229,233,235)", "rgb(190,199,206)", "rgb(124,143,156)", "rgb(71,85,94)", "rgb(42,49,55)"]
    interval_color_map = dict(zip(unique_intervals, colors))
    interval_label_map = {
        interval: f"{int(interval.left):,} – {int(interval.right):,}"
        for interval in unique_intervals
    }

    df["color"] = df["quintil"].map(interval_color_map)
    df["label"] = df["quintil"].map(interval_label_map)

    # Crear figura
    fig = go.Figure()

    # Agregar los estados coloreados
    for _, row in df.iterrows():
        estado = row["Entidad"]
        color = row["color"]
        remesa = row["Remesas"]

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
                    hovertemplate=f"<b>{estado}</b><br>Remesas: {remesa:,.2f} millones<extra></extra>"
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
        legend_title_text="Remesas (millones USD)",
        legend=dict(
            y=0.6,
            x=0.7,
            bordercolor="black",
            borderwidth=.1,
            font=dict(size=12)
        )
    )

    return fig


def remesas_bar(df):
    COLOR_BAR = "rgb(124, 143, 156)"
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    df = df.sort_values("Remesas", ascending = False)

    fig = go.Figure()
    
    fig.add_trace(
        go.Bar(
            x = df["Remesas"],
            y = df["Entidad"],
            orientation = "h",
            marker_color = COLOR_BAR,
            text = df["Remesas"].apply(lambda x: f"{x:,.0f}"),
            textposition = "inside",
            textfont = dict(
                color = COLOR_FONT, 
                size=SIZE_TEXT
                ),
            insidetextanchor = "start",
            customdata = df[["Entidad", "Remesas", "participacion", "tmac"]],
            hovertemplate = (
                "<b>%{customdata[0]}</b> <br>" +
                "<b>Remesas:</b> %{customdata[1]:,.0f} millones de USD<br>" +
                "<b>Participación:</b> %{customdata[2]:.2f}%<br>" +
                "<b>TMAC 2018-2023:</b> %{customdata[3]:.2f}%<extra></extra>"
                )
        )
    )

    fig.update_layout(
        height = 700,
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
            tickfont = dict(color=COLOR_FONT),
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
                  )
    )

    return fig