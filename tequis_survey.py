import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('static/csv/SurveysTequis.csv')

edades = [int(x) for x in df['Q1'] if str(x).isnumeric()]
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=edades,
    histnorm='percent',
    name='Age',
    xbins=dict(# bins used for histogram
        start=0,
        end=70,
        size=5
    ),
    marker_color='#EB89B5',
    opacity=0.75,
    marker=dict(
        line=dict(
            color='black',
            width=1
        )
    ),
))

fig.update_layout(
    title_text='Edades de los participantes', # title of plot
    xaxis_title_text='Edades', # xaxis label
    yaxis_title_text='Cantidad', # yaxis label
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)


if __name__ == '__main__':
    fig.write_image('static/imgs/edades.svg')