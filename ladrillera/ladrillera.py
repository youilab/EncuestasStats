import pandas as pd


def get_sensors_info(df):
    polls = ['pm25', 'pm1', 'no2', 'voc', 'pm10']

    measures = {
        'std_dev': 0,
        'mean': 0,
        'variance': 0,
    }

    pollutants = {
        'pm25': measures,
        'pm1': measures,
        'no2': measures,
        'voc': measures,
        'pm10': measures,
    }

    sensors_info = {}

    for i in df['sensor'].unique():
        sensors_info[str(i)] = {
            'pollutants': pollutants,
            'total_measurements': len(df[df['sensor'] == i]),
        }
        for _ in polls:
            sensors_info[str(i)]['pollutants'][_]['std_dev'] = round(df[df['sensor'] == i][_].std(), 2)
            sensors_info[str(i)]['pollutants'][_]['mean'] = round(df[df['sensor'] == i][_].mean(), 2)
            sensors_info[str(i)]['pollutants'][_]['variance'] = round(df[df['sensor'] == i][_].var(), 2)

    return sensors_info


if __name__ == '__main__':
    df = pd.read_csv('plumelabs_pollutants.csv')

    data = get_sensors_info(df)

    print(data)

