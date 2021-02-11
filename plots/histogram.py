import plotly.graph_objects as go
import numpy as np


class Histogram:

    def __init__(self, path):
        self.fig = go.Figure()
        self.path = path

    def hist_age_percents(self, ages, name):
        edades = [int(x) for x in ages if str(x).isnumeric()]

        bin = [x for x in range(0, 61, 5) if x > 1]

        counts, bins = np.histogram(edades, bins=bin)

        percentages = [round(((x / len(edades)) * 100), 2) for x in counts]
        bins = 0.5 * (bins[:-1] + bins[1:])

        self.fig = go.Figure()

        self.fig.add_trace(go.Bar(
            x=bins,
            y=percentages,
            name='Age',
            marker_color='#EB89B5',
            opacity=0.75,
            marker=dict(
                line=dict(
                    color='black',
                    width=1
                )
            ),
        ))

        self.fig.update_traces(texttemplate=[str(x) + '%' if x > 0 else '' for x in percentages], textposition='outside')
        self.fig.update_layout(
            title_text='Edades de los participantes',
            xaxis_title_text='Edades',  # xaxis label
            yaxis_title_text='Porcentaje',  # yaxis label
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
        )
        self.fig.write_image(self.path + name)
