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
        'video1': '5KygwcZ545U',
        'video2': 'D6yAOjTbZb8',
    }
    return html.Iframe(src=f'https://www.youtube.com/embed/{videos[value]}')

if __name__ == '__main__':
    app.run_server(debug=True)