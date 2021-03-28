import pandas as pd

from plots.histogram import Histogram
from ladrillera.ladrillera import get_sensors_info

if __name__ == '__main__':
    df = pd.read_csv('./ladrillera/plumelabs_pollutants.csv')
    data = get_sensors_info(df)
    pollutants = ['pm25', 'pm1', 'no2', 'voc', 'pm10']
    measurements = ['std_dev', 'mean', 'variance']
    titles = {
        'std_dev': 'Desviación estandar de ',
        'mean': 'Meadia de ',
        'variance': 'Varianza de '
    }
    hist = Histogram('ladrillera/plots/')

    for _ in pollutants:
        for measure in measurements:
            hist.hist_pollutants(
                x=data['sensors'],
                y=data['pollutants'][_][measure],
                pollutant=_,
                file_name=measure,
                title=titles[measure]
            )

    hist.hist_total_pollutants(
        x=data['sensors'],
        y=data['total_masurements'],
        file_name='total_measurements',
        title='Total de mediciones',
    )

