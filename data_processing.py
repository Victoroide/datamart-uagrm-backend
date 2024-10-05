import pandas as pd

def cargar_datos():
    df = pd.read_excel('data/DataMartAcademicoUAGRM.xlsx')
    return df

def obtener_facultades():
    df = cargar_datos()
    return df['FAC NOMBRE_FACULTAD'].unique().tolist()

def obtener_carreras():
    df = cargar_datos()
    return df['CARRE NOMBRE_CARRERA'].unique().tolist()

def obtener_periodos():
    df = cargar_datos()
    return df['Periodo'].unique().tolist()

def filtrar_datos(facultad, carrera, periodo):
    df = cargar_datos()

    if facultad != 'Todas':
        df = df[df['FAC NOMBRE_FACULTAD'] == facultad]
    
    if carrera != 'Todas':
        df = df[df['CARRE NOMBRE_CARRERA'] == carrera]

    if periodo:
        df = df[df['Periodo'] == periodo]

    return df
