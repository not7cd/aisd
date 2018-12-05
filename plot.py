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
        html.H1("AiSD"),
        dcc.Dropdown(
            id="my-dropdown",
            options=telemetry_files,
            value=telemetry_files[0]["value"],
            multi=True,
        ),
        dcc.Graph(id="n-time"),
    ]
)


def open_options(values):
    for value in values:
        alt = {"x": [], "y": [], "name": value}
        with open(value, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                alt["x"].append(row[0])
                alt["y"].append(row[1])

        yield alt


@app.callback(Output("n-time", "figure"), [Input("my-dropdown", "value")])
def update_graph(selected_dropdown_value):

    return {
        "data": [d for d in open_options(selected_dropdown_value)],
        "layout": {"title": "Time taken by algorithm"},
    }


if __name__ == "__main__":
    app.run_server(debug=True)
