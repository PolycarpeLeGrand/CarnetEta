import dash
import dash_bootstrap_components as dbc
import pandas as pd

from data.content import CONTENT
from config import PROJECT_TITLE

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY], suppress_callback_exceptions=True, title=PROJECT_TITLE)

DF = pd.DataFrame().from_records(CONTENT)

# TODO numeroter les conseils
DF['num'] = [f'Conseil {i+1}' for i in range(len(DF))]
# arranger le tab


