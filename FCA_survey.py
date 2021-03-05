import pandas as pd

from plots.histogram import Histogram
from plots.pie import PiePlot
from getters.get_data import get_Q9_FCA_data


if __name__ == '__main__':
    path = './static/csv/'
    plots_path = './static/imgs/FCA/'
    hist = Histogram(plots_path)
    pie = PiePlot(plots_path)

    dfs = {
        'Negocios': pd.read_csv(path + 'Negocios.csv'),
        'Padres': pd.read_csv(path + 'Padres.csv'),
        'Vecinos': pd.read_csv(path + 'Vecinos.csv')
    }

    ranges = {
        'Negocios': ['Q6', 'Q8', 'Q10', 'Q15'],
        'Padres': ['Q6', 'Q8', 'Q10'],
        'Vecinos': ['Q6', 'Q8', 'Q10', 'Q42']
    }
    range_titles = {
        'Q6': '¿Qué tan seguro te sientes recorriendo las calles y avenidas de la zona?',
        'Q8': '¿Qué tanto crees necesario mejorar la infraestructura vial de la zona?',
        'Q10': '¿Qué tanto tráfico consideras que hay en esta zona?',
        'Q15': 'Impacto a su negocio de la instalación de una ciclo vía en la zona.',
        'Q42': 'Impacto de la instalación de una ciclo vía en la zona.',
    }

    # Age questions
    """for file in dfs:
        hist.hist_percents(dfs[file]['Q3'], 'Q1_percentage' + file + '.svg', 'Porcentaje de edades de ' + file.lower())
        hist.hist_percents_accumulated(dfs[file]['Q3'], 'Q1_accumulated' + file + '.svg', 'Edades acumuladas ' + file.lower())
    """

    # Ranged questions
    """
    for surv in ranges:
        for question in ranges[surv]:

            hist.level_histogram(dfs[surv][question], question + surv + '.svg', range_titles[question])
    """

    # Q9
    """
    for df in dfs:
        q9 = dfs[df]['Q9']
        data = get_Q9_FCA_data(q9)
        pie.q9_fca(data, 'Q9_' + df + '.svg')
    """

    #hist.hist_q12_fca(dfs['Negocios']['Q12'])

