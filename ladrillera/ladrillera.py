import pandas as pd


def get_sensors_info(df):
    polls = ['pm25', 'pm1', 'no2', 'voc', 'pm10']

    sensors_info = {}

    for i in df['sensor'].unique():
        sensors_info[str(i)] = {
            'pollutants': {},
            'total_measurements': len(df[df['sensor'] == i]),
        }
        for _ in polls:
            measures = {
                'std_dev': round(df[df['sensor'] == i][_].std(), 2),
                'mean': round(df[df['sensor'] == i][_].mean(), 2),
                'variance': round(df[df['sensor'] == i][_].var(), 2),
            }
            sensors_info[str(i)]['pollutants'][_] = measures

    return sensors_info


if __name__ == '__main__':
    df = pd.read_csv('plumelabs_pollutants.csv')

    data = get_sensors_info(df)

    print(data)

