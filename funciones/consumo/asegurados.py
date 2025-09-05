import plotly.graph_objects as go

def graph1(df):
    COLOR_LINE_2 = "rgb(124, 143, 156)"
    COLOR_LINE_1 = "rgb(71, 85, 94)"
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    df["ta"] = df["ta"]/1000000

    # Últimos valores
    last_date = df['date_df'].iloc[-1]
    last_total = df['ta'].iloc[-1]
    last_total_pct = df['variacion'].iloc[-1]
    
    # Crear la figura
    fig = go.Figure()

    # Serie 1: TOTAL (eje primario, izquierdo)
    fig.add_trace(go.Scatter(
        x = df['date_df'],
        y = df['ta'],
        name = 'ta',
        yaxis = 'y1',
        line = dict(
            color = COLOR_LINE_1 
            ),
        text=df["ta"].apply(lambda x: f"{x:,.0f}"),
        customdata = df[["ta"]],
        hovertemplate = (
                "<b>Asegurados:</b> %{customdata[0]:,.2f}<extra></extra>"
                )
    ))

    # Serie 2: TOTAL_pct (eje secundario, derecho)
    fig.add_trace(go.Scatter(
        x = df['date_df'],
        y = df['variacion'],
        name = 'variacion',
        yaxis = 'y2',
        line = dict(
            color=COLOR_LINE_2, 
            dash='dot'
            ),
        text=df['variacion'].apply(lambda x: f"{x:.2f}"),
        customdata = df[['variacion']],
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
        text = f"{last_total:,.2f};",
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
            range=["2018-01", "2025-09"],
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
            tickfont = dict(color=COLOR_FONT,
                            size = SIZE_TEXT
                            ),
            showgrid=False
            ),
        yaxis2=dict(
            tickfont = dict(color=COLOR_FONT,
                            size = SIZE_TEXT),
            overlaying="y",
            side="right",
            showgrid=False
        ),
        margin=dict(t=10, l=10, r=10, b=10),
        showlegend = False, 
        template="plotly_white",
        hovermode="x unified",
        hoverlabel=dict(
            font_size=SIZE_TEXT,
            font_family=FONT_FAMILY,
            font_color=COLOR_FONT,
            bordercolor="gray"
    ))

    return fig


def graph2(df):
    COLOR_BAR = "rgb(229, 233, 235)"
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x = df["2025"],
            y = df["entidad"],
            orientation = "h",
            marker_color = COLOR_BAR,
            text = df["2025"].apply(lambda x: f"{x:,.0f}"),
            textposition = "inside",
            textfont = dict(
                color = COLOR_FONT, 
                size=SIZE_TEXT
                ),
            insidetextanchor = "start",
            customdata = df[["entidad", "2025", "participacion", "tmac"]],
            hovertemplate = (
                "<b>%{customdata[0]}</b> <br>" +
                "<b>Asegurados:</b> %{customdata[1]:,.0f}<br>" +
                "<b>Participación:</b> %{customdata[2]:.2f}%<br>" +
                "<b>TMAC 2018-2025:</b> %{customdata[3]:.2f}%<extra></extra>"
                )
        )
    )

    fig.update_layout(
        height = 900,
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
                            size = SIZE_TEXT
                            ),
            showgrid = False,
            fixedrange = False,
            automargin = True,
            autorange = 'reversed',
            ),
        showlegend = False,
        template = "plotly_white",
        margin = dict(t=10, l=10, r=10, b=10),
        hoverlabel = dict(
            font_size = SIZE_TEXT,
            font_family = FONT_FAMILY,
            font_color = COLOR_FONT,
            bordercolor = "gray"
        ),
        font = dict(family = FONT_FAMILY, 
                  color = COLOR_FONT,
                  size = SIZE_TEXT
                  )
    )
    return fig


def graph3(df):
    COLOR_LINE_2 = "rgb(229, 233, 235)"
    # COLOR_LINE_2 = "rgb(114, 47, 55)"
    COLOR_LINE_1 = "rgb(71, 85, 94)"
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    # Colores para texto según signo
    text_colors = ['white' if x > 0 else 'black' for x in df['dif']]

    # Texto formateado con comas
    text_formatted = df['dif'].apply(lambda x: f"{x:,}")
    
    # Crear la figura
    fig = go.Figure()

    fig.add_trace(go.Bar(
        y = df['entidad'],
        x = df['dif'],
        orientation='h',  # Horizontal
        marker_color = df['dif'].apply(lambda x: COLOR_LINE_1 if x > 0 else COLOR_LINE_2),
        textfont = dict(size=SIZE_TEXT),  # Ajusta color y tamaño
        text = text_formatted,
        textfont_color=text_colors,
        textposition = 'inside',
        insidetextanchor="start",  # Opcional: mejora alineación a la izquierda
        customdata=df[["entidad", "dic-2024", "jun-2025", "dif", "dif_pct"]],
        hovertemplate = (
            "<b>%{customdata[0]}</b><br>" +
            "<b>Asegurados dic-2024:</b> %{customdata[1]:,.0f}<br>" +
            "<b>Asegurados jun-2025:</b> %{customdata[2]:,.0f}<br>" +
            "<b>Diferencia:</b> %{customdata[3]:,.0f}<extra></extra><br>" +
            "<b>Diferencia porcentual:</b> %{customdata[4]:.2f}%"
            )
        ))
    
    fig.update_layout(
        height=600,
        bargap=0.1,  # reduce el espacio entre barras
        font = dict(
            family = FONT_FAMILY,
            size = SIZE_TEXT,
            color = "black"
        ),
        xaxis=dict(
            showticklabels = False,
            showgrid = False
        ),
        yaxis = dict(
            tickfont = dict(color=COLOR_FONT,
                            size = SIZE_TEXT
                            ),
            showgrid = False,
            fixedrange=False,
            automargin=True,
            autorange='reversed',
            ),
        showlegend=False,
        template="plotly_white",
        margin=dict(t=10, l=10, r=10, b=10),
        hoverlabel=dict(
            font_size=SIZE_TEXT,
            font_family=FONT_FAMILY,
            font_color=COLOR_FONT,
            bordercolor="gray"
))

    return fig