import plotly.graph_objects as go

def graph2(df):
    COLOR_BAR = "rgb(190, 199, 206)"
    COLOR_FONT= "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"


    fig = go.Figure()
    fig.add_trace(
        go.Bar(
        x=df["2024"],
        y=df["sector"],
        orientation="h",
        marker_color=COLOR_BAR,
        text=df["2024_"].apply(lambda x: f"${x:,.0f}"),
        textposition="inside",
        textfont=dict(color="black", size=SIZE_TEXT),  # Ajusta color y tamaño
        insidetextanchor="start",  # Opcional: mejora alineación a la izquierda
        customdata=df[["sector","2024_", "participacion", "tmac"]],
        hovertemplate = (
            "<b>%{customdata[0]}</b> <br>" +
            "<b>PIB:</b> %{customdata[1]:,.0f}<br>" +
            "<b>Participación:</b> %{customdata[2]:.2f}%<br>" +
            "<b>TMAC 2018-2024:</b> %{customdata[3]:.2f}<extra></extra>"
            )
    ))

    fig.update_layout(
        height=500,
        bargap=0.01,  # reduce el espacio entre barras
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
            tickfont = dict(color=COLOR_FONT),
            showgrid = False,
            fixedrange=False,
            automargin=True,
            autorange='reversed',
            ),
        showlegend=False,
        template="plotly_white",
        margin=dict(t=10, l=0, r=0, b=0),
        # hovermode="x unified",
        hoverlabel=dict(
            font_size=SIZE_TEXT,
            font_family=FONT_FAMILY,
            font_color=COLOR_FONT,
            bordercolor="gray"
    )
    )
    
    return fig