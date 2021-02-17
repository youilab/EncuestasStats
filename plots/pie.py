import plotly.graph_objects as go
from plotly.subplots import make_subplots


class PiePlot:
    def __init__(self, path):
        self.path = path

    def q4_pie(self, data, file_name):
        colors = ['#EB89B5', 'lightgray']
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
            title_text='',
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
