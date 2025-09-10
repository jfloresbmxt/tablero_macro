import pandas as pd
import plotly.graph_objects as go

def barras_comparacion(df, var):
    COLOR_BAR = "rgb(190, 199, 206)"
    COLOR_BAR_LAST = "rgb(124, 143, 156)"
    COLOR_FONT = "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    df = df[["date", var]].copy()

    df["date"] = pd.PeriodIndex(df["date"], freq="Q")
    df["date_dt"] = df["date"].dt.to_timestamp()           # eje X (datetime, serializable)
    df["date_lbl"] = df["date"].astype(str).str.replace("Q", " - Q", regex=False)  # "2006 - Q1"
    df["top"] = df[var]*1.01
    df["variacion"] = (df[var].pct_change())*100

    # --- Colores para resaltar la última barra ---
    colors = [COLOR_BAR] * len(df)
    if len(colors) > 0:
        colors[-1] = COLOR_BAR_LAST

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x = df["date_dt"],
            y = df[var],
            name = var,
            marker_color = colors,
            yaxis="y1",
            customdata = df[["date_lbl", var, "variacion"]],
            hovertemplate = (
            "<b>%{customdata[0]}</b> <br>" +
            "<b>IED:</b> %{customdata[1]:,.0f}<br>" +
            "<b>Variación:</b> %{customdata[2]:.2f}%<extra></extra>"
    )))

    # Línea con texto del porcentaje
    fig.add_trace(
        go.Scatter(
            x=df["date_dt"],
            y=df["top"],
            name="Variación (%)",
            mode="text",
            yaxis="y1",
            text=df["variacion"].apply(lambda x: f"{x:.2f}%"),
            textposition="top center"
    ))

    fig.update_layout(
        showlegend = False,
        font = dict(
            family = FONT_FAMILY,
            size = SIZE_TEXT,
            color = COLOR_FONT
        ),
        xaxis = dict(
            type = "date",
            dtick = "M12",
            tickformat = "%Y-Q%q",
            tickangle=-90,
            title_text="Año-Trimestre",
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
            range=["2017-06-01", "2025-09-01"],
            rangeslider = dict(visible=False),
            rangeselector = dict(
                buttons = list([
                    dict(count = 6, label = "5 años", step = "year", stepmode = "backward"),
                    dict(count = 10, label = "10 años", step = "year", stepmode = "todate"),
                    dict(count = 15, label = "15 años", step = "year", stepmode = "todate"),
                    dict(count = 21, label = "20 años", step = "year", stepmode = "todate"),
                ])
            )),
        yaxis = dict(
            tickfont = dict(color=COLOR_FONT, 
                            size = SIZE_TEXT),
            showexponent="none"
        ),
        margin=dict(t=10, l=10, r=10, b=10),
        template="plotly_white",
        hoverlabel=dict(
            font_size=SIZE_TEXT,
            font_family=FONT_FAMILY,
            font_color=COLOR_FONT,
            bordercolor="gray"
    ))

    return fig