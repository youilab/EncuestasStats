import pandas as pd

from plots.histogram import Histogram

if __name__ == '__main__':

    df = pd.read_csv('static/csv/SurveysTequis.csv')
    hist = Histogram('static/imgs/')

    hist.hist_age_percents(df['Q1'], 'histograma_edades.svg')
    hist.hist_age_accumulated(df['Q1'], 'histograma_edades_acumuladas.svg')
