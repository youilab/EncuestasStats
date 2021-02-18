def get_q4_data(q4):
    total = len(q4)
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


def get_q10_data(q10):
    total = len(q10)
    politica = 0
    social = 0
    propuestas = 0
    recursos = 0
    for i in q10:
        if 'política' in i:
            politica += 1
        if 'social' in i:
            social += 1
        if 'propuestas' in i:
            propuestas += 1
        if 'recursos' in i:
            recursos += 1

    data = {
        'politica': [politica, total - politica],
        'social': [social, total - social],
        'propuestas': [propuestas, total - propuestas],
        'recursos': [recursos, total - recursos],
    }

    return data


def get_q11_data(q11):
    total = len(q11)
    academia = 0
    gobierno = 0
    sociedad = 0
    comercio = 0
    industria = 0
    for i in q11:
        if 'Academia' in i:
            academia += 1
        if 'Gobierno' in i:
            gobierno += 1
        if 'Sociedad' in i:
            sociedad += 1
        if 'Comercio' in i:
            comercio += 1
        if 'Industria' in i:
            industria += 1

    data = {
        'academia': [academia, total - academia],
        'gobierno': [gobierno, total - gobierno],
        'sociedad': [sociedad, total - sociedad],
        'comercio': [comercio, total - comercio],
        'industria': [industria, total - industria],
    }

    return data
