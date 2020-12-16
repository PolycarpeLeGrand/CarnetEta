"""This is an example tab layout

the content goes in a dbc.container (or html.div) component and is imported by tabindex
"""

import dash_table
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from tools.factories import jumbotron_2_columns
from dashapp import app, DF

TAB_ID = 'table-tab'

title = 'Carnet de notes'
jumbo_text_1 = 'Les 80 conseils sont répertoriés dans le tableau ci-dessous. Les détails s\'affichent dans le panneau à la droite.  \n' \
               ' Les flèches haut et bas peuvent être utillisées pour naviguer entre les rangées.'

table_tab_jumbotron = jumbotron_2_columns(title, jumbo_text_1, '')
# print(DF[['course', 'type', 'doc']].to_dict('records'))

table_card = dash_table.DataTable(
    id='data-table',
    columns=[{'name': 'Conseil', 'id': 'num'}, {'name': 'Cours', 'id': 'course'}, {'name': 'Type', 'id': 'type'}, {'name': 'Document', 'id': 'doc'}],
    data=DF[['num', 'course', 'type', 'doc']].to_dict('records'),
    active_cell={'row': 0, 'column': 0},
    page_action='none',
    style_as_list_view=True,
    style_table={'height': '60vh', 'overflowY': 'auto', 'overflowX': 'hidden'},
    style_header={'fontWeight': 'bold', 'backgroundColor': 'ghostwhite', 'border': '1px solid black', 'font-size': '1.33em', 'text-align': 'center'},
    style_data={'backgroundColor': 'ghostwhite', 'font-size': '1.0em', 'text-align': 'center'},
    style_cell={'maxWidth': 0, 'whiteSpace': 'normal', 'textOverflow': 'ellipsis'},
    style_data_conditional=[{'if': {'state': 'active'}, 'backgroundColor': 'lightblue'},
                            {'if': {'state': 'selected'}, 'backgroundColor': 'lightblue'}]
    )



side_pannel = dbc.Card([
    dbc.CardHeader(id='pannel-card-header', className='bg-primary text-light'),
    dbc.Card([
        dbc.CardBody([
            html.Br(),
            dcc.Markdown(id='pannel-card-markdown', className='h6')
        ], style={'backgroundColor': 'ghostwhite'})
    ]),
], className="card border-primary mb-3")


table_tab = dbc.Container([
    dbc.Row([
        dbc.Col([
            table_tab_jumbotron,
        ])
    ]),

    dbc.Row([
        dbc.Col([
            table_card
        ], width=6),
        dbc.Col([
            side_pannel
        ]),
    ]),
], fluid=True, id=TAB_ID)


# callback go below

@app.callback(
    [Output(component_id='pannel-card-markdown', component_property='children'),
    Output(component_id='pannel-card-header', component_property='children'),
     Output(component_id='data-table', component_property='selected_cells')],
    [Input(component_id='data-table', component_property='active_cell')]
)
def update_panel(cell_data):
    if not cell_data:
        cell_data = {'row': 0, 'column': 0}

    header = dcc.Markdown(f"{DF.iloc[cell_data['row'], 4]} - {DF.iloc[cell_data['row'], 0]}  \n"
                          f"{DF.iloc[cell_data['row'], 1]} - {DF.iloc[cell_data['row'], 2]}")
    markdown = DF.iloc[cell_data['row'], 3]
    selected_cells = [{'row': cell_data['row'], 'column': i} for i in range(4)]
    return markdown, header, selected_cells