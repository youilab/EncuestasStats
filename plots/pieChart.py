import plotly.graph_objects as go
import numpy as np
from collections import Counter
import re


class Pie:

    def __init__(self, path):
        self.fig = go.Figure()
        self.path = path

    def pie_ocupation_percents(self, ocupations, name, title):

        ocupations = [x.capitalize() for x in ocupations ]
        ocupations = ["Ingeniero" if re.search("^Ing", x)else x for x in ocupations ]
        ocupations = ["Empleado" if re.search("^Emp|^Tra|^Vag", x)else x for x in ocupations ]
        ocupations = ["Academico" if re.search("^Aca|^Doc|^Mae", x)else x for x in ocupations ]
        ocupations = ["Estudiante" if re.search("^Est", x)else x for x in ocupations ]
        ocupations = ["Licenciado" if re.search("^Lic", x)else x for x in ocupations ]
 
        #ocupations = ["Otro" if re.search("^Sin", x)else x for x in ocupations ]
        
        counts = Counter(ocupations)

        self.fig = go.Figure(data=[go.Pie(labels=[*counts.keys()], values=[*counts.values()], hole=.3)])

        self.fig.update_layout(
            title_text=title,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
        )
        self.fig.write_image(self.path + name)


    

