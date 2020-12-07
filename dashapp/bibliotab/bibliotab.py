"""This an about tab

works as any other tab but contains text about the project, authors, etc.
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from data.markdowns import PROJECT_DETAILS_MARKDOWN

biblio_card = dbc.Card([
    dbc.CardHeader('Bibliographie', className='lead'),
    dbc.CardBody(dcc.Markdown('ref1  \nref2  \n'))
])

# tab container, which is imported by tabindex
# divided in rows with dbc.Row()
# rows typically one or many cards, split by cols
# self contained cards may be placed in a separate file and imported
biblio_tab = dbc.Container([
    dbc.Row([
        dbc.Col([biblio_card], width=6),
    ], justify='left'),
], fluid=True, id='example-tab')

