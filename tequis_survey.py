import pandas as pd

from plots.histogram import Histogram
from plots.pie import PiePlot
from getters.get_data import get_q4_data, get_q10_data, \
                            get_q11_data

if __name__ == '__main__':

    df = pd.read_csv('static/csv/tequisSurveyUTF8.csv')
    hist = Histogram('static/imgs/')

    categorical_questions = ['Q5', 'Q6', 'Q7', 'Q8', 'Q16', 'Q17', 'Q18', 'Q19',
                             'Q20', 'Q21', 'Q22', 'Q23', 'Q24', 'Q25', 'Q26', 'Q27',
                             'Q28', 'Q29', 'Q30', 'Q31', 'Q32']

    categorical_titles = ['Nivel de importancia de la problemática del tráfico.',
                          'Nivel de importancia de la problemática de la inseguridad.',
                          'Nivel de importancia de la problemática de las inundaciones.',
                          'Nivel de importancia de la problemática de la contaminación.',
                          'Nivel de importancia de que la ciudadanía se junte a firmar peticiones.',
                          'Nivel de importancia de subir impuestos.',
                          'Nivel de importancia de la impartición de talleres del uso de la ciudad.',
                          'Nivel de importancia de que haya más policías.',
                          'Nivel de importancia de que se realicen más actividades recreativas en espacios públicos.',
                          'Nivel de importancia de los fondos internacionales.',
                          'Nivel de importancia de poner bardas más altas.',
                          'Nivel de importancia de que haya vigilancia pública.',
                          'Nivel de importancia de implementar zonas 30.',
                          'Nivel de importancia de tener vías más rápidas.',
                          'Nivel de importancia de tener un sistema de civlovías.',
                          'Nivel de importancia de tener un bicibus escolar.',
                          'Nivel de importancia de invertir más en infrestructura.',
                          'Nivel de importancia de tener camiones escolares.',
                          'Nivel de importancia de cerrar calles por días.',
                          "Nivel de importancia de implementar 'Hoy no circula'.",
                          'Nivel de importancia de tener vigilantes ciudadanos.'
                          ]

    hist.hist_percents(df['Q1'], 'Q1.svg', 'Porcentaje de edades')
    hist.hist_percents_accumulated(df['Q1'], 'Q1_acumuladas.svg', 'Edades acumuladas')

    for index, q in enumerate(zip(categorical_questions, categorical_titles)):
        hist.level_histogram(df[q[0]], q[0] + '.svg', q[1])

    pie = PiePlot('static/imgs/')

    question4 = df['Q4']

    data = get_q4_data(question4)

    pie.q4_pie(data, 'Q4.svg')

    quetion10 = df['Q10']

    data = get_q10_data(quetion10)

    pie.q10_pie(data, 'Q10.svg')

    quetion11 = df['Q11']

    data = get_q11_data(quetion11)

    pie.q11_pie(data, 'Q11.svg')





