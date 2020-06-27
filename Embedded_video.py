import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash()
app.layout = html.Div([
    html.Div(id='target'),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Video 1', 'value': 'video1'},
            {'label': 'Video 2', 'value': 'video2'},
        ],
        value='video1'
    )
])


@app.callback(Output('target', 'children'), [Input('dropdown', 'value')])
def embed_iframe(value):
    videos = {
        'video1': 'https://www.youtube.com/embed/Ia6c6uIIb_Q',
        'video2': 'http://94.254.52.245:8081',
    }
    return html.Iframe(src=f'{videos[value]}')

if __name__ == '__main__':
    app.run_server(debug=True)