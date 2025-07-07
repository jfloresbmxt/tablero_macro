import plotly.graph_objects as go

def graph3(df):
    COLOR_BAR = "rgb(190, 199, 206)"
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x = df[2023],
            y = df["entidad"],
            orientation = "h",
            marker_color = COLOR_BAR,
            text = df[2023].apply(lambda x: f"${x:,.0f}"),
            textposition = "inside",
            textfont = dict(
                color = COLOR_FONT, 
                size=SIZE_TEXT
                ),
            insidetextanchor = "start",
            customdata = df[["entidad", 2023, "participacion", "tmac"]],
            hovertemplate = (
                "<b>%{customdata[0]}</b> <br>" +
                "<b>PIB:</b> %{customdata[1]:,.0f} mmdp<br>" +
                "<b>Participación:</b> %{customdata[2]:.2f}%<br>" +
                "<b>TMAC 2018-2023:</b> %{customdata[3]:.2f}%<extra></extra>"
                )
            )
        )
    
    fig.update_layout(
        height = 800,
        bargap = 0.01,
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
        margin = dict(t=30, l=0, r=0, b=0),
        font = dict(family = FONT_FAMILY, 
                  color = COLOR_FONT,
                  size = SIZE_TEXT
                  )
    )

    return fig


def graph3_1(df):
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x = df[2023],
            y = df["tmac"],
            mode = "markers",
            marker = dict(
                size = df["participacion"],
                sizemode = "area",
                sizeref = 2.*df["participacion"].max()/(60**2),
                sizemin=4,
                color=df["tmac"],
                colorscale="blues",
                line=dict(width=1, color='DarkSlateGrey')
            ),
            text = df["entidad"],
            hovertemplate="<b>%{text}</b><br>PIB: %{x:,.0f} mmdp<br>TMAC: %{y:.2f} "
            "%<br>Participación: %{marker.size:.2f} %",      
    ))

    annotations = []
    entidades = ["CDMX", "México", "Nuevo león", "Tabasco", "Jalisco", "Oaxaca"]
    df_f = df[df["entidad"].isin(entidades)]
    for i, row in df_f.iterrows():
        annotations.append(dict(
            x=row[2023],
            y=row["tmac"],
            xref="x",
            yref="y",
            text=row["entidad"],
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
                    color = "black"
                    )
                ),
            tickformat = ","
        ),
        yaxis = dict(
            title = dict(
            text = "TMAC (%)",
            font = dict(
                family = FONT_FAMILY,
                size = SIZE_TEXT,
                color = "black"
            )
        ),
        ),
        height=500,
        margin=dict(t=10, l=0, r=0, b=0),
        showlegend=False,
        template = "plotly_white",
        annotations=annotations,
        hoverlabel=dict(
                font_size=SIZE_TEXT,
                font_family=FONT_FAMILY,
                font_color=COLOR_FONT,
                bordercolor="gray",
                bgcolor = "white"
        )
        )

    return fig