from flask import Flask
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
import csv

from os import listdir
from os.path import isfile, join

TELEMETRY_PATH = "times/"

server = Flask(__name__)
app = dash.Dash(__name__, server=server)

telemetry_files = [
    {"label": f, "value": join(TELEMETRY_PATH, f)}
    for f in listdir(TELEMETRY_PATH)
    if isfile(join(TELEMETRY_PATH, f))
]


app.layout = html.Div(
    [
        html.H1("KSP Telemetry Archive"),
        dcc.Dropdown(
            id="my-dropdown", options=telemetry_files, value=telemetry_files[0]["value"]
        ),
        dcc.Graph(
            id="n-time"
        ),
    ]
)


@app.callback(Output("n-time", "figure"), [Input("my-dropdown", "value")])
def update_graph(selected_dropdown_value):

    alt = {"x": [], "y": []}
    with open(selected_dropdown_value, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            alt["x"].append(row[0])
            alt["y"].append(row[1])

    return {"data": [alt], 'layout': {
                'title': 'Time taken by algorithm'
            }}


if __name__ == "__main__":
    app.run_server(debug=True)
