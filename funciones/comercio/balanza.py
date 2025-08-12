import plotly.graph_objects as go

def balanza(df, vars):
    COLOR_LINE_2 = "rgb(124, 143, 156)"
    COLOR_LINE_1 = "rgb(71, 85, 94)"
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    # Últimos valores
    last_date = df['date_dt'].iloc[-1]
    last_xs = df[vars[0]].iloc[-2]
    last_ms = df[vars[1]].iloc[-2]
    
    # Crear la figura
    fig = go.Figure()

    # Serie 1: exportaciones
    fig.add_trace(
        go.Scatter(
            x = df["date_dt"],
            y = df[vars[0]],
            name = "Exportaciones",
            line_shape='spline',
            line = dict(
                color = COLOR_LINE_1
            ),
            text = df[vars[0]].apply(lambda x: f"{x:,.0f}"),
            customdata = df[[vars[0]]],
            hovertemplate = (
                "<b>Exportaciones:</b> %{customdata[0]:,.0f} mdd<extra></extra>"
            )))
    
    # Serie 2: importaciones
    fig.add_trace(
        go.Scatter(
            x = df["date_dt"],
            y = df[vars[1]],
            name = "Importaciones",
            line = dict(
                color = COLOR_LINE_2
            ),
            line_shape='spline',
            text = df[vars[1]].apply(lambda x: f"{x:,.0f}"),
            customdata = df[[vars[1]]],
            hovertemplate = (
                "<b>Importaciones:</b> %{customdata[0]:,.0f} mdd<extra></extra>"
            )))
    
    # Punto final para Exportaciones
    fig.add_trace(go.Scatter(
        x = [last_date],
        y = [last_xs],
        mode = "markers",
        marker = dict(color=COLOR_LINE_1, size=8, symbol='circle'),
        showlegend = False,
        hoverinfo = 'skip'
    ))

    # Punto final para Importaciones
    fig.add_trace(go.Scatter(
        x = [last_date],
        y = [last_ms],
        mode = "markers",
        marker = dict(color=COLOR_LINE_2, size=8, symbol='diamond'),
        showlegend = False,
        hoverinfo = 'skip'
    ))

    # Anotación para TOTAL
    fig.add_annotation(
        x = last_date,
        y = last_xs,
        text = f"{last_xs:,.0f}",
        yanchor = "bottom",
        showarrow = False,
        bordercolor = COLOR_LINE_1,
        borderpad = 4,
    )

    # Anotación para TOTAL_pct
    fig.add_annotation(
        x = last_date,
        y = last_ms,
        text = f"{last_ms:,.0f}",
        yanchor = "top",
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
            range =["2022-01", "2025-09"],
            rangeslider = dict(visible=False),
            rangeselector = dict(
                buttons = list([
                    dict(count = 5, label = "5 años", step = "year", stepmode = "backward"),
                    dict(count = 10, label = "10 años", step = "year", stepmode = "todate"),
                    dict(count = 15, label = "15 años", step = "year", stepmode = "todate"),
                    dict(count = 20, label = "20 años", step = "year", stepmode = "todate"),
                ]))
        ),
        yaxis = dict(
            tickfont = dict(color=COLOR_FONT),
            showgrid=True,
            # range=[y_min - padding, y_max + padding]
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