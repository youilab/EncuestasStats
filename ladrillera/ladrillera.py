import copy


def get_sensors_info(df):
    polls = ['pm25', 'pm1', 'no2', 'voc', 'pm10']

    measures = {
        'std_dev': [],
        'mean': [],
        'variance': [],
    }

    sensors_info = {
        'sensors': [],
        'total_masurements': [],
        'pollutants': {
            'pm25': copy.deepcopy(measures),
            'pm1': copy.deepcopy(measures),
            'no2': copy.deepcopy(measures),
            'voc': copy.deepcopy(measures),
            'pm10': copy.deepcopy(measures),
        },
    }

    for i in df['sensor'].unique():
        sensors_info['sensors'].append(str(i))
        sensors_info['total_masurements'].append(len(df[df['sensor'] == i]))
        for _ in polls:
            sensors_info['pollutants'][_]['std_dev'].append(round(df[df['sensor'] == i][_].std(), 2))
            sensors_info['pollutants'][_]['mean'].append(round(df[df['sensor'] == i][_].mean(), 2))
            sensors_info['pollutants'][_]['variance'].append(round(df[df['sensor'] == i][_].var(), 2))

    return sensors_info
