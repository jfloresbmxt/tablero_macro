import plotly.graph_objects as go

def graph1(df) -> go.Figure:
    """
    Genera una figura con barras de Totales y línea de variación porcentual,
    incluyendo los valores sobre cada punto.
    
    Returns:
        go.Figure: Gráfico interactivo con doble eje Y.
    """
    COLOR_BAR = "rgb(190, 199, 206)"

    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    df["pib_top"] = df["PIB"]*1.01

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x = df["year"],
            y = df["PIB"],
            name = "PIB",
            marker_color = COLOR_BAR,
            yaxis="y1",
            customdata=df[["year","PIB_", "variacion"]],
            hovertemplate = (
            "<b>%{customdata[0]}</b> <br>" +
            "<b>PIB:</b> %{customdata[1]:,.0f}<br>" +
            "<b>Variación:</b> %{customdata[2]:.2f}%<extra></extra>"
            )
    ))

    # Línea con texto del porcentaje
    fig.add_trace(
        go.Scatter(
            x=df["year"],
            y=df["pib_top"],
            name="Variación (%)",
            mode="text",
            yaxis="y1",
            text=df["variacion"].apply(lambda x: f"{x:.2f}%"),
            textposition="top center",
            customdata=df["variacion"],
    ))

    fig.add_annotation(
            text="*Para 2025 se tomó en cuenta solo el primer trimeste que es la información disponible",
            xref="paper", yref="paper",
            x=0, y=-0.07,  # esquina inferior izquierda del área del gráfico
            xanchor="left",
            yanchor="top",
            showarrow=False,
            font=dict(
                family=FONT_FAMILY,
                size=SIZE_TEXT,
                color=COLOR_FONT
            ),
            align="left",
            bgcolor="rgba(255,255,255,0.8)"  # fondo semitransparente opcional
        )

    fig.update_layout(
        showlegend = False,
        font = dict(
            family = FONT_FAMILY,
            size = SIZE_TEXT,
            color = "black"
        ),
        xaxis = dict(
            hoverformat="%Y",
            tickformat="%Y",
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
            title_text = "Año",
            type = "date",
            range=["2019-06", "2025-06"],
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
                            size = SIZE_TEXT),
            showexponent="none"
    ),
        yaxis2=dict(
            tickfont=dict(color=COLOR_FONT),
            overlaying="y",
            side="right"
        ),
        margin=dict(t=10, l=10, r=10, b=10),
        template="plotly_white",
        hoverlabel=dict(
            font_size=SIZE_TEXT,
            font_family=FONT_FAMILY,
            font_color=COLOR_FONT,
            bordercolor="gray"
        )
    )

    return fig