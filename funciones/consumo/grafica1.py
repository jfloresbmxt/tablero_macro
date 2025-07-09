import plotly.graph_objects as go

def graph_consumo(df):
    COLOR_LINE_1 = "rgb(71, 85, 94)"       # Línea TOTAL
    COLOR_LINE_2 = "rgb(124, 143, 156)"    # Línea TOTAL_pct
    COLOR_FONT = "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"
    
    # Últimos valores
    last_date = df['date_dt_pct'].iloc[-1]
    last_total = df['TOTAL'].iloc[-1]
    last_total_pct = df['TOTAL_pct'].iloc[-1]
    # df = df.rename(columns = {"TOTAL":"Consumo", "TOTAL_pct":"Variación"})
    
    # Crear figura
    fig = go.Figure()

    # Serie 1: TOTAL (eje primario)
    fig.add_trace(go.Scatter(
        x = df['date_dt_pct'],
        y = df['TOTAL'],
        name = 'Indice de consumo',
        yaxis = 'y1',
        line = dict(color=COLOR_LINE_1),
        text = df["TOTAL"].apply(lambda x: f"{x:.2f}"),
        customdata = df[["TOTAL"]],
        hovertemplate = "<b>Índice:</b> %{customdata[0]:.2f}<extra></extra>"
    ))

    # Serie 2: TOTAL_pct (eje secundario)
    fig.add_trace(go.Scatter(
        x = df['date_dt_pct'],
        y = df['TOTAL_pct'],
        name = 'Variación anual (%)',
        yaxis = 'y2',
        line = dict(color=COLOR_LINE_2, dash='dot'),
        text = df["TOTAL_pct"].apply(lambda x: f"{x:.2f}"),
        customdata = df[["TOTAL_pct"]],
        hovertemplate = "<b>Variación:</b> %{customdata[0]:.2f}%<extra></extra>"
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
        text = f"{last_total:.2f}",
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

    # Layout
    fig.update_layout(
        height = 500,
        font = dict(
            family = FONT_FAMILY,
            size = SIZE_TEXT,
            color = COLOR_FONT
        ),
        xaxis = dict(
            tickfont = dict(family=FONT_FAMILY, size=SIZE_TEXT, color=COLOR_FONT),
            title_font = dict(family=FONT_FAMILY, size=SIZE_TEXT, color=COLOR_FONT),
            showgrid = False,
            title_text = "Fecha",
            type = "date",
            range = ["2018-01", "2025-04"],
            rangeslider = dict(visible=False),
            rangeselector = dict(
                buttons = list([
                    dict(count=5, label="5 años", step="year", stepmode="backward"),
                    dict(count=10, label="10 años", step="year", stepmode="todate"),
                    dict(count=15, label="15 años", step="year", stepmode="todate"),
                    dict(count=20, label="20 años", step="year", stepmode="todate"),
                    dict(label = "Mostrar toda la serie", step = "all")
                ])
            )
        ),
        yaxis = dict(
            tickfont = dict(color=COLOR_FONT),
            showgrid = False
        ),
        yaxis2 = dict(
            tickfont = dict(color=COLOR_FONT),
            overlaying = "y",
            side = "right",
            showgrid = False
        ),
        margin = dict(t=10, l=10, r=10, b=10),
        showlegend = True,
        template = "plotly_white",
        hovermode = "x unified",
        hoverlabel = dict(
            font_size = SIZE_TEXT,
            font_family = FONT_FAMILY,
            font_color = COLOR_FONT,
            bordercolor = "gray"
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