import plotly.graph_objects as go

def graph2_1(df):
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = df["2024_"],
            y = df["tmac"],
            mode = "markers",
            marker = dict(
                size = df["participacion"],
                sizemode = "area",
                sizeref = 2.*df["participacion"].max()/(60**2),
                sizemin=4,
                color=df["tmac"],
                colorscale="blues",
                colorbar = dict(
                    title = dict(
                        text = "TMAC (%)",
                        font = dict(
                            family = FONT_FAMILY,
                            size = SIZE_TEXT,
                            color = COLOR_FONT
                        )
                    )
                ),
                line=dict(width=1, color='DarkSlateGrey'),
            ),
            text = df["sector"],
            customdata=df[["sector","2024_", "participacion", "tmac"]],
            hovertemplate = (
            "<b>%{customdata[0]}</b> <br>" +
            "<b>PIB:</b> %{customdata[1]:,.0f}<br>" +
            "<b>Participación:</b> %{customdata[2]:.2f}%<br>" +
            "<b>TMAC 2018-2024:</b> %{customdata[3]:.2f}%<extra></extra>"
            )
    ))

    annotations = []
    for i, row in df.iterrows():
        annotations.append(dict(
            x=row["2024_"],
            y=row["tmac"],
            xref="x",
            yref="y",
            text=row["sector"],
            showarrow=True,
            arrowhead=2,
            ax=20,   # desplazamiento horizontal del texto
            ay=-20,  # desplazamiento vertical del texto
            font=dict(size=10),
            bgcolor="white",
            bordercolor="gray",
            borderwidth=0.5,
            opacity=0.8
        ))

    fig.add_annotation(
    text="Fuente: Elaboración propia con datos de INEGI",
    xref="paper", yref="paper",
    x=0, y=-0.07,  # esquina inferior izquierda del área del gráfico
    xanchor="left",
    yanchor="top",
    showarrow=False,
    font=dict(
        family=FONT_FAMILY,
        size=SIZE_TEXT - 1,
        color=COLOR_FONT
    ),
    align="left",
    bgcolor="rgba(255,255,255,0.8)"  # fondo semitransparente opcional
)


    fig.update_layout(
        font = dict(
            family = FONT_FAMILY,
            size = SIZE_TEXT,
            color = "black"
        ),
        xaxis = dict(
            title = dict(
                text = "PIB (miles de millones de pesos)",
                font = dict(
                    family = FONT_FAMILY,
                    size = SIZE_TEXT,
                    color = COLOR_FONT
                    )
                ),
            tickfont=dict(
                family=FONT_FAMILY, 
                size=SIZE_TEXT, 
                color=COLOR_FONT),
            tickformat = ","
        ),
         yaxis=dict(
            title=dict(
                text="TMAC (%)",
                font=dict(family=FONT_FAMILY, size=SIZE_TEXT, color=COLOR_FONT)
            ),
            tickfont=dict(family=FONT_FAMILY, size=SIZE_TEXT, color=COLOR_FONT)
        ),
        height=500,
        margin=dict(t=10, l=10, r=10, b=10),
        showlegend=False,
        template = "plotly_white",
        annotations=annotations,
        hoverlabel=dict(
                font_size=SIZE_TEXT,
                font_family=FONT_FAMILY,
                font_color=COLOR_FONT,
                bordercolor="gray",
                bgcolor = "white"
        ))

    return fig