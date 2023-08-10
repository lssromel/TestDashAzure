## Complejizamos el dashboard, incluimos un gráfico de barras

# Importamos las librerías necesarias

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, Output, html, Input, Dash, callback


# Importamos el dataset

results_df = pd.read_csv("export_data.csv", encoding="utf8")

# Creamos la aplicación

app = dash.Dash()

# Run Server
dash_app = Dash()
app = dash_app.server

dash_app.layout = html.Div(
    [
        html.H1("Creación de un dashboard"),
        dcc.Graph(id="graph-with-slider"),
        dcc.Slider(
            id="year-slider",
            min=results_df["Year"].min(),
            max=results_df["Year"].max(),
            value=results_df["Year"].max(),
            marks={str(year): str(year) for year in results_df["Year"].unique()},
            step=None,
        ),
    ]
)

# Creamos la función que actualiza el gráfico


@dash_app.callback(Output("graph-with-slider", "figure"), Input("year-slider", "value"))
def update_figure(selected_year):
    filtered_df = results_df[results_df["Year"] == selected_year]
    fig = px.scatter(filtered_df, x="Valor", y="Tipo", color="Municipio", log_x=False)
    fig.update_layout(transition_duration=500)
    return fig


# Ejecutamos la aplicación
if __name__ == "__main__":
    dash_app.run_server(debug=False)
