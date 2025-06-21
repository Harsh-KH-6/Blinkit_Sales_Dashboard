# app.py - Deployment version of blinkit_dashboard.py
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, State
import urllib
import io
import os

# ---------- data ----------
# Use absolute path for deployment
current_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(current_dir, 'Blinkit_Sales.xlsx')

df = pd.read_excel(excel_path)  # Adjust or confirm sheet_name if needed
df['Unit_Sales'] = 1
df['Revenue'] = df['Item_Outlet_Sales']

# ---------- app ----------
app = Dash(__name__, title='Blinkit Sales Dashboard')

item_opts   = [{'label': i, 'value': i} for i in sorted(df['Item_Type'].unique())]
outlet_opts = [{'label': i, 'value': i} for i in sorted(df['Outlet_Type'].unique())]
tier_opts   = [{'label': t, 'value': t} for t in sorted(df['Outlet_Location_Type'].unique())]

# ---------- layout ----------
app.layout = html.Div([
    html.Div([
        html.Img(src='/assets/blinkit_logo.webp', title="Powered by Blinkit", style={'height': '60px'}),
        html.H1('Blinkit Sales Dashboard', style={'marginLeft': '20px', 'color': '#2b9348'}),
    ], style={'display': 'flex', 'alignItems': 'center', 'padding': '10px', 'backgroundColor': '#d8f3dc'}),

    html.Div([
        html.Div([dcc.Dropdown(item_opts, [], id='item_dd', multi=True)], style={'width':'32%'}),
        html.Div([dcc.Dropdown(outlet_opts, [], id='outlet_dd', multi=True)], style={'width':'32%'}),
        html.Div([dcc.RadioItems(tier_opts, tier_opts[0]['value'], id='tier_radio', inline=True)], style={'width':'32%'})
    ], style={
        'display':'flex', 'gap':'1%', 'padding': '10px',
        'flexWrap': 'wrap', 'justifyContent': 'space-between'
    }),

    html.Br(),

    html.Div([
        html.A("📥 Download Filtered Data", id='download-link', download="filtered_data.csv", href="", target="_blank",
               style={'marginLeft': '10px', 'color': '#007bff', 'textDecoration': 'none'})
    ]),

    html.Br(),

    html.Div(id='kpi_row', style={'display':'flex','gap':'1%', 'textAlign':'center'}),

    dcc.Graph(id='bar_item'),
    dcc.Graph(id='pie_outlet'),
    dcc.Graph(id='scatter_mrp'),
    dcc.Graph(id='line_year'),

    html.Footer("© 2025 Blinkit Insights • Made by Harsh 💚",
                style={'textAlign': 'center', 'padding': '20px', 'color': '#555'})

], style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f8f9fa'})

# ---------- filter helper ----------
def filter_df(df, items, outlets, tier):
    d = df.copy()
    if items:   d = d[d['Item_Type'].isin(items)]
    if outlets: d = d[d['Outlet_Type'].isin(outlets)]
    if tier:    d = d[d['Outlet_Location_Type'] == tier]
    return d

# ---------- callback ----------
@app.callback(
    Output('kpi_row','children'),
    Output('bar_item','figure'),
    Output('pie_outlet','figure'),
    Output('scatter_mrp','figure'),
    Output('line_year','figure'),
    Output('download-link','href'),
    Input('item_dd','value'),
    Input('outlet_dd','value'),
    Input('tier_radio','value')
)
def update_all(items, outlets, tier):
    d = filter_df(df, items, outlets, tier)

    # KPIs
    kpi1 = html.Div([html.H3(f"₹{d['Revenue'].sum():,.0f}"), html.P('Total Revenue')], style={'flex':'1'})
    kpi2 = html.Div([html.H3(f"{len(d):,}"), html.P('Total Units')], style={'flex':'1'})
    kpi3 = html.Div([html.H3(f"₹{d['Item_MRP'].mean():.2f}"), html.P('Avg MRP')], style={'flex':'1'})
    kpi4 = html.Div([html.H3(f"₹{(d['Item_MRP'] - d['Revenue']).mean():.2f}"), html.P('Avg Discount')], style={'flex':'1'})
    kpis = [kpi1, kpi2, kpi3, kpi4]

    # Figures
    bar = px.bar(d.groupby('Item_Type')['Revenue'].sum().sort_values(), orientation='h',
                 labels={'value':'Revenue','index':'Item Type'})
    pie = px.pie(d, names='Outlet_Type', values='Revenue', hole=.4)
    scat = px.scatter(d, x='Item_MRP', y='Revenue', color='Item_Fat_Content',
                      size='Item_Visibility', hover_data=['Item_Type'])
    line = px.line(d.groupby(['Outlet_Establishment_Year','Outlet_Identifier'])['Revenue'].sum().reset_index(),
                   x='Outlet_Establishment_Year', y='Revenue', color='Outlet_Identifier')

    for fig in (bar, pie, scat, line):
        fig.update_layout(margin=dict(l=20,r=20,t=40,b=20))

    # Create downloadable CSV from filtered dataframe
    csv_string = d.to_csv(index=False, encoding='utf-8')
    csv_bytes = csv_string.encode()
    b64 = urllib.parse.quote(csv_bytes)

    return kpis, bar, pie, scat, line, f"data:text/csv;charset=utf-8,{b64}"

# For deployment platforms that need a server variable
server = app.server

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8050))) 