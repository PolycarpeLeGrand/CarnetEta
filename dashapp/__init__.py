import dash
import dash_bootstrap_components as dbc
import pandas as pd

from data.content import CONTENT

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY], suppress_callback_exceptions=True)

DATA = [2312, 34234, 3453]  # with temp as open(): DATA = pickle.load(PATH)

DF = pd.DataFrame({'course': ['Cours 1', 'Cours 2', 'Cours 3'],
                   'type': ['Notes', 'Texte', 'Notes'],
                   'doc': ['Notes du cours 1', 'La cigale et la fourmis', 'Notes capsule 13 nov'],
                   'markdown': ['Ceci est le texte du conseil  \n* Bullet', '#### BlaBla  \nBlaBlaBla', '#### Allo  \nBye']})

a = [f'Cours {n+1}' for n in range(80)]
b = ['Notes' for _ in range(80)]
b2 = ['Notes shufweifh hueiiue hfwuiehf huihiu hiuh hiuiwhefiuw huih wefwh uhiuh f wefihui wf hihuhhuiu fhwi huh hfwiehf uibui buwub buibe biub f fwe  ibuibiub' for _ in range(80)]
c = [f'Cours {n+1} sdfsdfdfgdgdgdf  \n* asdsfsfdf' for n in range(80)]

d = {'course': a, 'type': b, 'doc': b2, 'markdown': c}
DF = pd.DataFrame().from_records(CONTENT)
