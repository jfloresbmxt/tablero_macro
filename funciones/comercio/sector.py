import plotly.graph_objects as go
import numpy as np

def sector_barras(df):
    COLOR_BAR = "rgb(124, 143, 156)"
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x = df["2024"],
            y = df["Descripción"],
            orientation = "h",
            marker_color = COLOR_BAR,
            text = df["2024"].apply(lambda x: f"{x:,.0f}"),
            textposition = "inside",
            textfont = dict(
                color = COLOR_FONT,
                size = SIZE_TEXT
            ),
            insidetextanchor = "start",
            customdata = df[["Descripción", "2024", "participacion", "tmac", "crec_anual"]],
            hovertemplate = (
                "<b>%{customdata[0]}</b> <br>" +
                "<b>Exportaciones:</b> %{customdata[1]:,.0f}<br>" +
                "<b>Participación:</b> %{customdata[2]:.2f}%<br>" +
                "<b>Crecimiento anual:</b> %{customdata[3]:.2f}%<br>" +
                "<b>TMAC 2018-2023:</b> %{customdata[4]:.2f}%<extra></extra>"
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

def filtrar_sector(df, sector):
    df = df[["date", sector]]
    df["cambio_pct"] = (
        (df[sector] - df[sector].shift()) /
        df[sector].shift().replace(0, np.nan)) * 100
    
    return df


def sector_serie(df,s):
    COLOR_LINE_2 = "rgb(124, 143, 156)"
    COLOR_LINE_1 = "rgb(71, 85, 94)"
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    df = filtrar_sector(df, s)
    

    # Últimos valores
    last_date = df['date'].iloc[-1]
    last_total = df[s].iloc[-1]
    last_total_pct = df['cambio_pct'].iloc[-1]

    # Crear la figura
    fig = go.Figure()

    # Serie 1:
    fig.add_trace(
        go.Scatter(
            x = df["date"],
            y = df[s],
            name = s,
            line_shape='spline',
            yaxis = 'y1',
            line = dict(
                color = COLOR_LINE_1
            ),
            customdata = df[[s]],
            hovertemplate = (
                "<b>Exportaciones:</b> %{customdata[0]:,.0f} mdd<extra></extra>"
    )))

    # Serie 2: Variacion anual
    fig.add_trace(
        go.Scatter(
            x = df["date"],
            y = df["cambio_pct"],
            name = "Variación anual (%)",
            yaxis = 'y2',
            line = dict(
                color=COLOR_LINE_2, 
                dash='dot'
            ),
            customdata = df[['cambio_pct']],
            hovertemplate = (
                "<b>Variación:</b> %{customdata[0]:.2f}%<extra></extra>"
                )
        )
    )

    # Punto final para serie 1
    fig.add_trace(go.Scatter(
        x = [last_date],
        y = [last_total],
        mode = "markers",
        marker = dict(color=COLOR_LINE_1, size=8, symbol='circle'),
        showlegend = False,
        hoverinfo = 'skip'
    ))

    # Punto final para Serie 2
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
        text = f"{last_total:,.0f} mdd",
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
        yanchor = "top",
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
            color = COLOR_FONT,
        ),
        xaxis = dict(
            tickfont = dict(
                family = FONT_FAMILY,
                size = SIZE_TEXT,
                color = COLOR_FONT,
            ),
            title_font = dict(
                family = FONT_FAMILY,
                size = SIZE_TEXT,
                color = COLOR_FONT
            ),
            showgrid = True,
            tickformat="%b %Y",
            title_text = "Fecha",
            type = "date",
            range =["2020", "2024-06"],
            rangeslider = dict(visible=False),
            rangeselector = dict(
                buttons = list([
                    dict(count = 5, label = "5 años", step = "year", stepmode = "backward"),
                    dict(count = 10, label = "10 años", step = "year", stepmode = "todate"),
                    dict(count = 15, label = "15 años", step = "year", stepmode = "todate"),
                ]))
        ),
        yaxis = dict(
            tickfont = dict(color=COLOR_FONT),
            showgrid=False
            ),
        yaxis2=dict(
            tickfont=dict(color=COLOR_FONT),
            overlaying="y",
            side="right",
            ticksuffix="%",
            showgrid=False
        ),
        margin=dict(t=10, l=10, r=10, b=10),
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
    ))

    return fig