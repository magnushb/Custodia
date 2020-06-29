import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash()
app.layout = html.Div([
    

    html.Div(id='target1'),
    html.Label('First Camera'),
    dcc.Dropdown(
        id='dropdown1',
        options=[
            {'label': 'HHG', 'value': 'video1'},
            {'label': 'Refocus', 'value': 'video2'},
        ],
        value='video1'
    ),
    html.Div(id='target2'),
    html.Label('Second Camera'),
    dcc.Dropdown(
        id='dropdown2',
        options=[
            {'label': 'HHG', 'value': 'video1'},
            {'label': 'Refocus', 'value': 'video2'},
        ],
        value='video1'
    )
])


@app.callback(Output('target1', 'children'), [Input('dropdown1', 'value')])
def embed_iframe(value):
    videos = {
        'video1': 'https://www.youtube.com/embed/Ia6c6uIIb_Q',
        'video2': 'http://94.254.52.245:8081',
    }
    return html.Iframe(src=f'{videos[value]}')

@app.callback(Output('target2', 'children'), [Input('dropdown2', 'value')])
def embed_iframe(value):
    videos = {
        'video1': 'https://www.youtube.com/embed/Ia6c6uIIb_Q',
        'video2': 'http://94.254.52.245:8081',
    }
    return html.Iframe(src=f'{videos[value]}')

if __name__ == '__main__':
    app.run_server(debug=True)