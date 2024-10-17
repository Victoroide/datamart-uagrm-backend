import pandas as pd
import pyodbc

def get_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=dataMart;'
        'UID=usersql;'  
        'PWD=password;'
        'Trusted_Connection=no;'
    )
    return conn

def cargar_datos_excel():
    df = pd.read_excel('data/DataMartAcademicoUAGRM.xlsx')
    return df

def insertar_facultades(df):
    conn = get_connection()
    cursor = conn.cursor()
    facultades = df[['FAC', 'FAC NOMBRE_FACULTAD', 'LOCALIDAD']].drop_duplicates()

    for _, row in facultades.iterrows():
        cursor.execute("""
            INSERT INTO Facultad (FAC, NOMBRE_FACULTAD, LOCALIDAD) VALUES (?, ?, ?)
        """, row['FAC'], row['FAC NOMBRE_FACULTAD'], row['LOCALIDAD'])
    
    conn.commit()
    cursor.close()
    conn.close()

def insertar_carreras(df):
    conn = get_connection()
    cursor = conn.cursor()
    carreras = df[['CARRE', 'CARRE NOMBRE_CARRERA', 'FAC']].drop_duplicates()

    for _, row in carreras.iterrows():
        cursor.execute("""
            INSERT INTO Carrera (CARRE, NOMBRE_CARRERA, FAC) VALUES (?, ?, ?)
        """, row['CARRE'], row['CARRE NOMBRE_CARRERA'], row['FAC'])
    
    conn.commit()
    cursor.close()
    conn.close()

def insertar_periodos(df):
    conn = get_connection()
    cursor = conn.cursor()
    periodos = df[['Periodo']].drop_duplicates()

    for _, row in periodos.iterrows():
        cursor.execute("""
            INSERT INTO Period (PERIODO) VALUES (?)
        """, row['Periodo'])
    
    conn.commit()
    cursor.close()
    conn.close()

def insertar_gestion(df):
    conn = get_connection()
    cursor = conn.cursor()
    gestion = df[[
        'CARRE', 'Periodo', 'MODALIDAD', 'T_INS', 'T_NUE', 'T_ANT', 'MAT_INS', 'SIN_NOT', 
        'POR_SNOT', 'APROBAD', 'POR_APRO', 'REPROBA', 'POR_REPR', 'R_CON_0', 'MORAS', 
        'MORA_PERCENT', 'RETIR', 'PPA', 'PPS', 'PPA1', 'PPAC', 'EGRE', 'TIT'
    ]].drop_duplicates()

    for _, row in gestion.iterrows():
        cursor.execute("""
            INSERT INTO Gestion (CARRE, PERIODO, MODALIDAD, T_INS, T_NUE, T_ANT, MAT_INS, SIN_NOT, POR_SNOT, 
            APROBAD, POR_APRO, REPROBA, POR_REPR, R_CON_0, MORAS, MORA_PERCENT, RETIR, PPA, PPS, PPA1, PPAC, EGRE, TIT) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, row['CARRE'], row['Periodo'], row['MODALIDAD'], row['T_INS'], row['T_NUE'], row['T_ANT'],
           row['MAT_INS'], row['SIN_NOT'], row['POR_SNOT'], row['APROBAD'], row['POR_APRO'], row['REPROBA'],
           row['POR_REPR'], row['R_CON_0'], row['MORAS'], row['MORA_PERCENT'], row['RETIR'], row['PPA'],
           row['PPS'], row['PPA1'], row['PPAC'], row['EGRE'], row['TIT'])
    
    conn.commit()
    cursor.close()
    conn.close()

df = cargar_datos_excel()
insertar_facultades(df)
insertar_carreras(df)
insertar_periodos(df)
insertar_gestion(df)
