import dash
from dash import dcc, html, dash_table, Input, Output
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

db_url = 'sqlite:///etl_pipeline.db'
engine = create_engine(db_url)

def load_raw_data():
    query = "SELECT * FROM users_transformed"
    df = pd.read_sql(query, engine)
    return df

def load_aggregated_data():
    query = """
    SELECT Education, AVG(Income) AS Avg_Income, COUNT(*) AS Num_Customers
    FROM users_transformed
    GROUP BY Education;
    """
    df = pd.read_sql(query, engine)
    return df

# Initialize Dash app
app = dash.Dash(__name__)
app.title = "Automated Reporting Dashboard"
app.layout = html.Div(children=[
    html.H1("Automated Reporting Dashboard"),
    html.P("This dashboard displays key metrics from the transformed data."),
    html.Button("Refresh Data", id="refresh-button", n_clicks=0, style={'margin-bottom': '20px'}),
    
    dcc.Graph(id="avg-income-graph"),
    
    dcc.Graph(id="customer-count-graph"),
    
    html.H2("Raw Data Preview"),
    dash_table.DataTable(
        id='data-table',
        columns=[{"name": i, "id": i} for i in load_raw_data().columns],
        data=load_raw_data().to_dict('records'),
        page_size=10,
        style_table={'overflowX': 'auto'},
        style_cell={'textAlign': 'left'},
    )
])

@app.callback(
    [Output("avg-income-graph", "figure"),
     Output("customer-count-graph", "figure"),
     Output("data-table", "data")],
    [Input("refresh-button", "n_clicks")]
)
def update_dashboard(n_clicks):
    df_agg = load_aggregated_data()
    df_raw = load_raw_data()
    fig_bar = px.bar(
        df_agg,
        x="Education",
        y="Avg_Income",
        title="Average Income by Education Level",
        labels={"Avg_Income": "Average Income", "Education": "Education Level"}
    )
    
    # Create a pie chart for customer distribution by education
    fig_pie = px.pie(
        df_agg,
        names="Education",
        values="Num_Customers",
        title="Customer Distribution by Education"
    )
    
    # Return updated figures and data table records
    return fig_bar, fig_pie, df_raw.to_dict("records")

if __name__ == '__main__':
    app.run(debug=True)
