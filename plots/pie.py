import plotly.graph_objects as go
from plotly.subplots import make_subplots


class PiePlot:
    def __init__(self, path):
        self.path = path

    def q4_pie(self, data, file_name):
        colors = ['#FD9D24', 'lightgray']
        percentages = [round(x[0] / (x[0] + x[1]) * 100, 2) for x in data.values()]

        # Create subplots, using 'domain' type for pie charts
        specs = [[{'type': 'domain'}, {'type': 'domain'}], [{'type': 'domain'}, {'type': 'domain'}]]
        fig = make_subplots(rows=2, cols=2, specs=specs)

        fig.add_trace(go.Pie(values=data['trafico'], hole=0.8, textinfo='none',
                             marker_colors=colors), 1, 1)
        fig.add_trace(go.Pie(values=data['contaminacion'], hole=0.8, textinfo='none',
                             marker_colors=colors), 1, 2)
        fig.add_trace(go.Pie(values=data['inseguridad'], hole=0.8, textinfo='none',
                             marker_colors=colors), 2, 1)
        fig.add_trace(go.Pie(values=data['inundaciones'], hole=0.8, textinfo='none',
                             marker_colors=colors), 2, 2)

        # Use `hole` to create a donut-like pie chart
        fig.update_traces(textinfo='none')

        fig.update_layout(
            title_text='Elementos que se encuentran con más frecuencia',
            # Add annotations in the center of the donut pies.
            annotations=[dict(text=str(percentages[0]) + '%',
                              x=0.15, y=0.83, font_size=20, showarrow=False),
                         dict(text='Tráfico',
                              x=0.15, y=0.52, font_size=20, showarrow=False),
                         dict(text=str(percentages[1]) + '%',
                              x=0.86, y=0.83, font_size=20, showarrow=False),
                         dict(text='Contaminación',
                              x=0.92, y=0.52, font_size=20, showarrow=False),
                         dict(text=str(percentages[2]) + '%',
                              x=0.163, y=0.17, font_size=20, showarrow=False),
                         dict(text='Inseguridad',
                              x=0.11, y=-0.09, font_size=20, showarrow=False),
                         dict(text=str(percentages[3]) + '%',
                              x=0.86, y=0.17, font_size=20, showarrow=False),
                         dict(text='Inundaciones',
                              x=0.91, y=-0.09, font_size=20, showarrow=False),
                         ])

        fig.update(layout_showlegend=False)

        fig.write_image(self.path + file_name)

    def q10_pie(self, data, file_name):
        colors = ['#FD9D24', 'lightgray']
        percentages = [round(x[0] / (x[0] + x[1]) * 100, 2) for x in data.values()]

        # Create subplots, using 'domain' type for pie charts
        specs = [[{'type': 'domain'}, {'type': 'domain'}], [{'type': 'domain'}, {'type': 'domain'}]]
        fig = make_subplots(rows=2, cols=2, specs=specs)

        fig.add_trace(go.Pie(values=data['politica'], hole=0.8, textinfo='none',
                             marker_colors=colors), 1, 1)
        fig.add_trace(go.Pie(values=data['social'], hole=0.8, textinfo='none',
                             marker_colors=colors), 1, 2)
        fig.add_trace(go.Pie(values=data['propuestas'], hole=0.8, textinfo='none',
                             marker_colors=colors), 2, 1)
        fig.add_trace(go.Pie(values=data['recursos'], hole=0.8, textinfo='none',
                             marker_colors=colors), 2, 2)

        # Use `hole` to create a donut-like pie chart
        fig.update_traces(textinfo='none')

        fig.update_layout(
            title_text='Obstáculos para solucionar problemática ambiental.',
            # Add annotations in the center of the donut pies.
            annotations=[dict(text=str(percentages[0]) + '%',
                              x=0.15, y=0.83, font_size=20, showarrow=False),
                         dict(text='Falta de voluntad política',
                              x=0.05, y=0.52, font_size=15, showarrow=False),
                         dict(text=str(percentages[1]) + '%',
                              x=0.86, y=0.83, font_size=20, showarrow=False),
                         dict(text='Falta de paticipación social',
                              x=0.96, y=0.52, font_size=15, showarrow=False),
                         dict(text=str(percentages[2]) + '%',
                              x=0.163, y=0.17, font_size=20, showarrow=False),
                         dict(text='Falta de propuestas',
                              x=0.08, y=-0.09, font_size=15, showarrow=False),
                         dict(text=str(percentages[3]) + '%',
                              x=0.86, y=0.17, font_size=20, showarrow=False),
                         dict(text='Falta de recursos económicos',
                              x=0.98, y=-0.09, font_size=15, showarrow=False),
                         ])

        fig.update(layout_showlegend=False)

        fig.write_image(self.path + file_name)

    def q11_pie(self, data, file_name):
        colors = ['#FD9D24', 'lightgray']
        percentages = [round(x[0] / (x[0] + x[1]) * 100, 2) for x in data.values()]

        # Create subplots, using 'domain' type for pie charts
        specs = [[{'type': 'domain'}, {'type': 'domain'}],
                 [{'type': 'domain'}, {'type': 'domain'}],
                 [{'type': 'domain', "colspan": 2}, None]]
        fig = make_subplots(rows=3, cols=2, specs=specs)

        fig.add_trace(go.Pie(values=data['academia'], hole=0.8, textinfo='none',
                             marker_colors=colors), 1, 1)
        fig.add_trace(go.Pie(values=data['gobierno'], hole=0.8, textinfo='none',
                             marker_colors=colors), 1, 2)
        fig.add_trace(go.Pie(values=data['sociedad'], hole=0.8, textinfo='none',
                             marker_colors=colors), 2, 1)
        fig.add_trace(go.Pie(values=data['comercio'], hole=0.8, textinfo='none',
                             marker_colors=colors), 2, 2)
        fig.add_trace(go.Pie(values=data['industria'], hole=0.8, textinfo='none',
                             marker_colors=colors), row=3, col=1)

        # Use `hole` to create a donut-like pie chart
        fig.update_traces(textinfo='none')

        fig.update_layout(
            title_text='Organismos que los participantes involucrarían.',
            # Add annotations in the center of the donut pies.
            annotations=[dict(text=str(percentages[0]) + '%',
                              x=0.17, y=0.9, font_size=15, showarrow=False),
                         dict(text='Academia (Universidades)',
                              x=0.06, y=0.73, font_size=13, showarrow=False),
                         dict(text=str(percentages[1]) + '%',
                              x=0.835, y=0.9, font_size=15, showarrow=False),
                         dict(text='Gobierno (Autoridades)',
                              x=0.92, y=0.73, font_size=13, showarrow=False),
                         dict(text=str(percentages[2]) + '%',
                              x=0.17, y=0.5, font_size=15, showarrow=False),
                         dict(text='Sociedad (Ciudadanos)',
                              x=0.08, y=0.3, font_size=13, showarrow=False),
                         dict(text=str(percentages[3]) + '%',
                              x=0.835, y=0.5, font_size=15, showarrow=False),
                         dict(text='Comercio (Negocios)',
                              x=0.91, y=0.3, font_size=13, showarrow=False),
                         dict(text=str(percentages[4]) + '%',
                              x=0.5, y=0.1, font_size=15, showarrow=False),
                         dict(text='Industria (Empresas)',
                              x=0.5, y=-0.07, font_size=13, showarrow=False),
                         ])
        fig.update(layout_showlegend=False)

        fig.write_image(self.path + file_name)
