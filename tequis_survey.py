import pandas as pd

from plots.histogram import Histogram
from plots.pie import PiePlot


def get_q4_data(q4):
    trafico = 0
    contaminacion = 0
    inseguridad = 0
    inundaciones = 0
    for i in q4:
        if 'Tráfico' in i:
            trafico += 1
        if 'Contaminación' in i:
            contaminacion += 1
        if 'Inseguridad' in i:
            inseguridad += 1
        if 'Inundaciones' in i:
            inundaciones += 1

    data = {
        'trafico': [trafico, total - trafico],
        'contaminacion': [contaminacion, total - contaminacion],
        'inseguridad': [inseguridad, total - inseguridad],
        'inundaciones': [inundaciones, total - inundaciones],
    }

    return data


if __name__ == '__main__':

    df = pd.read_csv('static/csv/tequisSurveyUTF8.csv')
    hist = Histogram('static/imgs/')

    """hist.hist_percents(df['Q1'], 'histograma_edades.svg', 'Porcentaje de edades')
    hist.hist_percents_accumulated(df['Q1'], 'histograma_edades_acumuladas.svg', 'Edades acumuladas')"""

    pie = PiePlot('static/imgs/')

    question4 = df['Q4']
    total = len(question4)

    data = get_q4_data(question4)

    pie.q4_pie(data, 'trafico.svg')





