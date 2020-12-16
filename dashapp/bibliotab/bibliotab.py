"""This an about tab

works as any other tab but contains text about the project, authors, etc.
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from data.biblio import BIBLIO
from dashapp import DF

biblio_card = dbc.Card([
    dbc.CardHeader('Bibliographie', className='lead'),
    dbc.CardBody([
        dcc.Markdown(BIBLIO),
        dbc.Label('Site web réalisé avec ', className='h5'),
        html.A(' Plotly Dash', href='https://plotly.com/dash/', className='h5', target='_blank'),
        html.Br(),
        dbc.Label('Code de l\'application disponible ', className='h5'),
        html.A(' ici', href='https://github.com/PolycarpeLeGrand/CarnetEta', className='h5', target='_blank'),
    ]),
])

stats_card = dbc.Card([
    dbc.CardHeader('Statistiques', className='lead'),
    dbc.CardBody([
        dbc.Label(f'Nombre de conseils: {len(DF)}', className='h6'), html.Br(),
        dbc.Label(f'Nombre de cours: {len(DF["course"].unique())}', className='h6'), html.Br(),
        dbc.Label(f'Nombre de textes: {len(DF[DF["type"]=="Notes de lecture"]["doc"].unique())}', className='h6'), html.Br(), html.Br(),
        dbc.Label(f'Entrées par cours', className='h5'), html.Br(),
        dcc.Markdown('  \n'.join(f'{name} - {count}' for name, count in DF["course"].value_counts().items()), className='h6'), html.Br(),
    ]),
])


# tab container, which is imported by tabindex
# divided in rows with dbc.Row()
# rows typically one or many cards, split by cols
# self contained cards may be placed in a separate file and imported
biblio_tab = dbc.Container([
    dbc.Row([
        dbc.Col([biblio_card], width=6),
        dbc.Col([stats_card], width=4)
    ], justify='left'),
], fluid=True, id='example-tab')

