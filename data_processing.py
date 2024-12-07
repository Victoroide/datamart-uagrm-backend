# data_processing.py
import pandas as pd
from database import get_connection

def obtener_facultades():
    query="SELECT DISTINCT NOMBRE_FACULTAD FROM Facultad ORDER BY NOMBRE_FACULTAD"
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    facultades=df['NOMBRE_FACULTAD'].tolist()
    facultades.insert(0,'Todas')
    return facultades

def obtener_carreras():
    query="SELECT DISTINCT NOMBRE_CARRERA FROM Carrera ORDER BY NOMBRE_CARRERA"
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    carreras=df['NOMBRE_CARRERA'].tolist()
    carreras.insert(0,'Todas')
    return carreras

def obtener_carreras_por_facultad(facultad):
    query="""
SELECT c.NOMBRE_CARRERA
FROM Carrera c
INNER JOIN Facultad f ON c.idFacultad=f.id
WHERE f.NOMBRE_FACULTAD=?
ORDER BY c.NOMBRE_CARRERA
"""
    conn=get_connection()
    df=pd.read_sql(query,conn,params=[facultad])
    conn.close()
    return df['NOMBRE_CARRERA'].tolist()

def obtener_periodos():
    query="SELECT DISTINCT PERIODO FROM Periodoo ORDER BY PERIODO"
    conn=get_connection()
    df=pd.read_sql(query,conn)
    conn.close()
    return df['PERIODO'].tolist()

def cargar_datos():
    conn=get_connection()
    query="""
SELECT 
f.NOMBRE_FACULTAD,
c.NOMBRE_CARRERA,
l.nombre AS LOCALIDAD,
p.PERIODO,
g.MODALIDAD,
g.T_INS,
g.T_NUE,
g.T_ANT,
g.MAT_INS,
g.SIN_NOT,
g.POR_SNOT,
g.APROBAD,
g.POR_APRO,
g.REPROBA,
g.POR_REPR,
g.R_CON_0,
g.POR_CON_0,
g.MORAS,
g.MORA_PERCENT,
g.RETIR,
g.PPA,
g.PPS,
g.PPA1,
g.PPAC,
g.EGRE,
g.TIT
FROM Gestion g
INNER JOIN carreraXlocalidad cl ON g.idFacultad=cl.idFacultad AND g.idCarre=cl.idCarre AND g.idlocalidad=cl.idlocalidad
INNER JOIN Carrera c ON cl.idFacultad=c.idFacultad AND cl.idCarre=c.id
INNER JOIN Facultad f ON c.idFacultad=f.id
INNER JOIN localidad l ON cl.idlocalidad=l.id
INNER JOIN Periodoo p ON g.PERIODO=p.PERIODO
"""
    df=pd.read_sql(query,conn)
    conn.close()
    return df

def filtrar_datos(facultad,carrera,periodo):
    df=cargar_datos()
    if facultad!='Todas':
        df=df[df['NOMBRE_FACULTAD']==facultad]
    if carrera!='Todas':
        df=df[df['NOMBRE_CARRERA']==carrera]
    if periodo and periodo.strip():
        df=df[df['PERIODO']==periodo]
    return df

def filtrar_preset_datos(preset,facultad,carrera,periodo,localidad='Todas',modalidad='Todas'):
    df=cargar_datos()
    if facultad!='Todas':
        df=df[df['NOMBRE_FACULTAD']==facultad]
    if carrera!='Todas':
        df=df[df['NOMBRE_CARRERA']==carrera]
    if periodo and periodo.strip():
        df=df[df['PERIODO']==periodo]
    if localidad!='Todas':
        df=df[df['LOCALIDAD']==localidad]
    if modalidad!='Todas':
        df=df[df['MODALIDAD']==modalidad]
    return df
