import plotly.graph_objects as go
import numpy as np


class Histogram:
    def __init__(self, path):
        self.path = path

    def _age_histogram_setup(self, fig, bins, percentages, title, xaxis):
        fig.add_trace(go.Bar(
            x=bins,
            y=percentages,
            name='Age',
            marker_color='#FD9D24',
            opacity=0.75,
            marker=dict(
                line=dict(
                    color='black',
                    width=1
                )
            ),
        ))

        fig.update_traces(texttemplate=[str(x) + '' if x > 0 else '' for x in percentages],
                          textposition='outside')
        fig.update_layout(
            title_text=title,
            xaxis_title_text=xaxis,  # xaxis label
            yaxis_title_text='Porcentaje',  # yaxis label
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            bargap=0.2,
        )

        return fig

    def hist_percents(self, ages, file_name, title):
        edades = [int(x) for x in ages if str(x).isnumeric()]

        bin = [x for x in range(0, 61, 5) if x > 1]

        counts, bins = np.histogram(edades, bins=bin)

        percentages = [round(((x / sum(counts)) * 100), 2) for x in counts]
        bins = 0.5 * (bins[:-1] + bins[1:])

        fig = go.Figure()

        fig = self._age_histogram_setup(fig, bins, percentages, title, 'Edades')

        fig.write_image(self.path + file_name)

    def hist_percents_accumulated(self, ages, file_name, title):
        edades = [int(x) for x in ages if str(x).isnumeric()]

        bin = [x for x in range(0, 61, 5) if x > 1]

        counts, bins = np.histogram(edades, bins=bin)

        aux = 0
        for x in range(len(counts)):
            aux += counts[x]
            counts[x] = aux

        percentages = [round((x / counts[-1]) * 100, 2) for x in counts]
        bins = 0.5 * (bins[:-1] + bins[1:])

        fig = go.Figure()

        fig = self._age_histogram_setup(fig, bins, percentages, title, 'Edades')

        fig.write_image(self.path + file_name)

    def level_histogram(self, data, file_name, title):
        levels = [int(x) for x in data if str(x).isnumeric()]

        counts, bins = np.histogram(levels, bins=range(1, 12))

        percentages = [round(((x / sum(counts)) * 100), 2) for x in counts]

        fig = go.Figure()

        fig = self._age_histogram_setup(fig, bins, percentages, title, 'Importancia')

        fig.update_layout(
            xaxis=dict(
                showticklabels=True,
                tickmode='linear'
            )
        )

        fig.write_image(self.path + file_name)

    def hist_q12_fca(self, data):

        count = {
            'Caminando': 0,
            'Bicicleta': 0,
            'Transporte privado': 0,
            'Transporte público': 0,
            'Vehículo propio': 0,
        }

        for i in data:
            count[i] += 1

        y = [(count[i]/len(data))*100 for i in count]
        x = [i for i in count]

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=y,
            y=x,
            opacity=0.75,
            marker=dict(
                color='#FD9D24',
                line=dict(
                    color='black',
                    width=1
                ),
            ),
            orientation='h',
        ))

        fig.update_traces(texttemplate=[str(x) + '%' if x > 0 else '' for x in y], textposition='inside')
        fig.update_layout(
            title_text='¿Qué medio usas para llegar al negocio?',
            # xaxis_title_text=xaxis,  # xaxis label
            xaxis_title_text='Porcentaje',  # yaxis label
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            bargap=0.2,
        )

        fig.write_image(self.path + 'Q12_FCA.svg')

    def hist_pollutants(self, x, y, pollutant, file_name, title):

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=x,
            y=y,
            name=pollutant,
            marker_color='#FD9D24',
            opacity=0.75,
            marker=dict(
                line=dict(
                    color='black',
                    width=1
                )
            ),
        ))

        fig.update_traces(texttemplate=[x for x in y],
                          textposition='outside')
        fig.update_layout(
            title_text=title + pollutant.upper(),
            xaxis_title_text='Flows',  # xaxis label
            yaxis_title_text='',  # yaxis label
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            bargap=0.2,
        )

        fig.write_image(self.path + file_name + "_" + pollutant + ".svg")

    def hist_total_pollutants(self, x, y, file_name, title):
        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=x,
            y=y,
            marker_color='#FD9D24',
            opacity=0.75,
            marker=dict(
                line=dict(
                    color='black',
                    width=1
                )
            ),
        ))

        fig.update_traces(texttemplate=[x for x in y],
                          textposition='outside')
        fig.update_layout(
            title_text=title,
            xaxis_title_text='Flows',  # xaxis label
            yaxis_title_text='',  # yaxis label
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            bargap=0.2,
        )

        fig.write_image(self.path + file_name + ".svg")
