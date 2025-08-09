import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Load and clean dataset
df = pd.read_csv("flood_data_with_coordinates.csv")
df["Latitude"] = pd.to_numeric(df["Latitude"], errors='coerce')
df["Longitude"] = pd.to_numeric(df["Longitude"], errors='coerce')

weeks = sorted(df["Week"].unique())
cities = sorted(df["City"].unique())

# Dash App
app = dash.Dash(__name__, external_stylesheets=[
    dbc.themes.BOOTSTRAP,
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;600&display=swap",
    "/assets/style.css"
])
app.title = "Flood Risk Dashboard - Pakistan"

app.layout = html.Div([
    html.Div([
        html.Img(src="/assets/hydrolytix-logo.png", style={"height": "50px", "marginRight": "15px", "verticalAlign": "middle"}),
        html.Span([
            html.H2("Hydrolytix", style={"display": "inline", "marginRight": "10px"}),
            html.Small("AI-Powered Flood Risk Intelligence", style={"color": "white", "fontWeight": "normal", "fontSize": "14px", "verticalAlign": "middle"})
        ], style={"display": "inline-block", "verticalAlign": "middle"})
    ], className="navbar", style={"display": "flex", "alignItems": "center"}),

    html.Div([  # content-wrapper starts
    html.Div([
        html.H3("📊 Filters"),
        html.Label("Select Week:"),
        dcc.Dropdown(
            id='week-dropdown',
            options=[{'label': w, 'value': w} for w in weeks],
            value=weeks[0],
            clearable=False,
            className="dropdown",
            style={'width': '200px'}
        ),
        # Removed toggle button here
        html.Label("Select City:"),
        dcc.Dropdown(
            id='city-dropdown',
            options=[{'label': c, 'value': c} for c in cities],
            value=None,
            placeholder="All cities",
            clearable=True,
            className="dropdown",
            style={'width': '200px'}
        ),
    ], className="sidebar", id="sidebar"),

        html.Div([  # main-content starts
        html.Div([
            html.Div(id='summary-cards', className="summary-cards"),
        ], style={'display': 'flex', 'justifyContent': 'center', 'marginBottom': '20px'}),

        html.Div([
            dcc.Tabs([
                dcc.Tab(label='📊 Rainfall & Risk Chart', children=[
                dcc.Loading(html.Div(dcc.Graph(id='flood-graph', config={"responsive": True, "scrollZoom": False, "displayModeBar": True, "staticPlot": False}), style={'height': '600px', 'overflow': 'hidden'}), type="circle")
                ]),
                dcc.Tab(label='🥧 Flood Risk Pie Chart', children=[
                dcc.Loading(html.Div(dcc.Graph(id='risk-pie-chart', config={"responsive": True, "scrollZoom": False, "displayModeBar": True, "staticPlot": False}), style={'height': '600px', 'overflow': 'hidden'}), type="circle")
                ]),
                dcc.Tab(label='🗺️ Map View', children=[
                dcc.Loading(html.Div(dcc.Graph(id='map-graph', config={"responsive": True, "scrollZoom": False, "displayModeBar": True, "staticPlot": False}), style={'height': '600px', 'overflow': 'hidden'}), type="circle")
                ])
            ])
        ], className="tabs-container")
    ], className="main-content")  # main-content ends
    ], className="content-wrapper", id="content-wrapper")  # content-wrapper ends
])

# Removed toggle_sidebar callback and related imports

# from dash.dependencies import State

# @app.callback(
#     Output("sidebar", "className"),
#     Input("toggle-sidebar", "n_clicks"),
#     State("sidebar", "className"),
#     prevent_initial_call=True
# )
# def toggle_sidebar(n_clicks, current_class):
#     if current_class and "collapsed" in current_class:
#         return "sidebar"
#     else:
#         return "sidebar collapsed"

# Callback for Bar Chart
@app.callback(
    Output('flood-graph', 'figure'),
    [Input('week-dropdown', 'value'),
     Input('city-dropdown', 'value')]
)
def update_bar_chart(selected_week, selected_city):
    filtered_df = df[df["Week"] == selected_week].copy()
    if selected_city and selected_city != "All cities":
        filtered_df = filtered_df[filtered_df["City"] == selected_city]

    if filtered_df.empty:
        return px.bar(title="No data available for selected filters.")

    fig = px.bar(
        filtered_df,
        x="City",
        y="Rainfall (mm)",
        color="Flood Risk Level",
        title=f"{selected_city or 'All Cities'} - {selected_week}"
    )
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig

# Remove the circular dependency callbacks to avoid infinite loop errors

# The previous callbacks resetting dropdown values caused circular dependency errors.
# Instead, we will rely on CSS fixes and user interaction to manage dropdown visibility.

# If needed, we can explore alternative UI components or JavaScript solutions for better dropdown control.

# Callback for Summary Cards
@app.callback(
    Output('summary-cards', 'children'),
    Input('week-dropdown', 'value')
)
def update_summary(selected_week):
    filtered_df = df[df["Week"] == selected_week].copy()
    total_affected = filtered_df["Affected People"].sum()
    total_camps = filtered_df["Relief Camps"].sum()

    return [
        html.Div([
            html.H4("Total Affected"),
            html.P(f"{total_affected:,}")
        ], className="card"),

        html.Div([
            html.H4("Total Camps"),
            html.P(f"{total_camps}")
        ], className="card")
    ]

# Callback for Pie Chart
@app.callback(
    Output('risk-pie-chart', 'figure'),
    [Input('week-dropdown', 'value'),
     Input('city-dropdown', 'value')]
)
def update_pie(selected_week, selected_city):
    filtered_df = df[df["Week"] == selected_week].copy()
    if selected_city and selected_city != "All cities":
        filtered_df = filtered_df[filtered_df["City"] == selected_city]

    if filtered_df.empty:
        return px.pie(title="No data available for selected filters.")

    risk_counts = filtered_df["Flood Risk Level"].value_counts().reset_index()
    risk_counts.columns = ["Risk Level", "Count"]

    fig = px.pie(
        risk_counts,
        names="Risk Level",
        values="Count",
        title="Flood Risk Distribution"
    )
    fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
    return fig

# Callback for Map
@app.callback(
    Output('map-graph', 'figure'),
    [Input('week-dropdown', 'value'),
     Input('city-dropdown', 'value')]
)
def update_map(selected_week, selected_city):
    try:
        filtered_df = df[df["Week"] == selected_week].copy()
        if selected_city and selected_city != "All cities":
            filtered_df = filtered_df[filtered_df["City"] == selected_city]

        filtered_df = filtered_df.dropna(subset=["Latitude", "Longitude"])

        if filtered_df.empty:
            return px.scatter(title="No map data for selected filters.")

        filtered_df["Rainfall (mm)"] = filtered_df["Rainfall (mm)"].clip(lower=0, upper=200)

        fig = px.scatter_map(
            filtered_df,
            lat="Latitude",
            lon="Longitude",
            color="Flood Risk Level",
            size="Rainfall (mm)",
            hover_name="City",
            zoom=4,
            title="Flood Risk Map"
        )
        fig.update_layout(mapbox_style="carto-positron", margin=dict(r=0, t=40, l=0, b=0))
        return fig

    except Exception as e:
        print(f"[Map Error] {e}")
        return px.scatter(title="⚠️ Error Generating Map")

if __name__ == '__main__':
    app.run(debug=True)
