import pandas as pd
import plotly.graph_objects as go
import numpy as np

def pie_ied_kind(df, fecha_objetivo):
    # ==== Estilo ====
    COLOR_FONT = "#000000"
    SIZE_TEXT = 10
    FONT_FAMILY = "Noto Sans"

    # Colores solicitados
    COLOR_LINE_1 = "rgb(229, 233, 235)"  # Gris claro
    COLOR_LINE_2 = "rgb(190, 199, 206)"  # Gris medio
    COLOR_LINE_3 = "rgb(124, 143, 156)"  # Gris oscuro
    COLORS = [COLOR_LINE_1, COLOR_LINE_2, COLOR_LINE_3]

    # ==== Columnas esperadas ====
    cols_tipo = ["Cuentas entre compañías", "Nuevas inversiones", "Reinversión de utilidades"]
    assert "date" in df.columns, "Falta columna 'date' en el DataFrame"
    for c in cols_tipo:
        assert c in df.columns, f"Falta columna '{c}'"

    # ==== Filtro por fecha (soporte para Period o string) ====
    if isinstance(df["date"].dtype, pd.PeriodDtype):
        mask = (df["date"].astype(str) == str(pd.Period(fecha_objetivo, freq="Q")))
    else:
        mask = (df["date"].astype(str) == str(fecha_objetivo))

    if not mask.any():
        raise ValueError(f"No se encontró la fecha '{fecha_objetivo}' en df['date']")

    fila = df.loc[mask].iloc[0].copy()

    # ==== Preparar datos ====
    vals = pd.to_numeric(fila[cols_tipo], errors="coerce").fillna(0.0)
    vals = vals.where(vals > 0, 0.0)

    labels = cols_tipo
    values = vals.values

    if np.isclose(values.sum(), 0.0):
        raise ValueError("Todos los valores son 0 o no válidos para esa fecha; no se puede graficar el pie.")

    # Texto al centro: total
    total = float(values.sum())
    center_text = f"Total<br><b>{total:,.0f}</b>"

    # ==== Colores del texto interno ====
    text_colors = [COLOR_FONT, COLOR_FONT, "white"]  # blanco para el gris más oscuro

    # ==== Gráfico ====
    fig = go.Figure(
        go.Pie(
            labels=labels,
            values=values,
            hole=0.4,                      # dona
            sort=False,
            textinfo="label+percent",
            textfont=dict(color=text_colors, size=SIZE_TEXT),
            marker=dict(colors=COLORS),
            hovertemplate="<b>%{label}</b><br>IED: %{value:,.0f}<extra></extra>"
        )
    )

    # ==== Layout ====
    fig.update_layout(
        title=None,          # Quitar título
        showlegend=False,    # Quitar leyenda
        template="plotly_white",
        margin=dict(t=10, l=10, r=10, b=10),
        font=dict(family=FONT_FAMILY, size=SIZE_TEXT, color=COLOR_FONT),
        hoverlabel=dict(
            font_size=SIZE_TEXT,
            font_family=FONT_FAMILY,
            font_color=COLOR_FONT,
            bordercolor="gray"
        ),
        # Texto centrado en la dona
        annotations=[dict(
            text=center_text,
            showarrow=False,
            font=dict(family=FONT_FAMILY, size=SIZE_TEXT+8, color=COLOR_FONT)
        )]
    )

    return fig