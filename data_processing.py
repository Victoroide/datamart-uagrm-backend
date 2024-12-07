import pandas as pd
from database import get_connection

def obtener_facultades():
    query = "SELECT DISTINCT NOMBRE_FACULTAD FROM Facultad ORDER BY NOMBRE_FACULTAD"
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    facultades = df['NOMBRE_FACULTAD'].tolist()
    facultades.insert(0, 'Todas')
    return facultades

def obtener_carreras():
    # Se obtiene todas las carreras distintas
    query = "SELECT DISTINCT NOMBRE_CARRERA FROM Carrera ORDER BY NOMBRE_CARRERA"
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    carreras = df['NOMBRE_CARRERA'].tolist()
    carreras.insert(0, 'Todas')
    return carreras

def obtener_periodos():
    query = "SELECT DISTINCT PERIODO FROM Periodoo ORDER BY PERIODO"
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    periodos = df['PERIODO'].tolist()
    return periodos

def filtrar_datos(facultad, carrera, periodo):
    # Construir el query con las condiciones opcionales
    base_query = """
SELECT 
  f.NOMBRE_FACULTAD AS [FAC NOMBRE_FACULTAD],
  c.NOMBRE_CARRERA AS [CARRE NOMBRE_CARRERA],
  l.nombre AS [LOCALIDAD],
  p.PERIODO AS [Periodo],
  g.T_INS AS [_INS],
  g.T_NUE,
  g.T_ANT,
  g.MAT_INS,
  g.SIN_NOT,
  g.POR_SNOT,
  g.APROBAD,
  g.POR_APRO AS [%APRO],
  g.REPROBA,
  g.POR_REPR AS [%REPR],
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
  g.TIT,
  g.MODALIDAD
FROM Gestion g
INNER JOIN carreraXlocalidad cl ON g.idFacultad = cl.idFacultad AND g.idCarre = cl.idCarre AND g.idlocalidad = cl.idlocalidad
INNER JOIN Carrera c ON cl.idFacultad = c.idFacultad AND cl.idCarre = c.id
INNER JOIN Facultad f ON c.idFacultad = f.id
INNER JOIN localidad l ON cl.idlocalidad = l.id
INNER JOIN Periodoo p ON g.PERIODO = p.PERIODO
WHERE 1=1
"""

    params = []
    if facultad and facultad != 'Todas':
        base_query += " AND f.NOMBRE_FACULTAD = ?"
        params.append(facultad)

    if carrera and carrera != 'Todas':
        base_query += " AND c.NOMBRE_CARRERA = ?"
        params.append(carrera)

    if periodo and periodo.strip() != '':
        base_query += " AND p.PERIODO = ?"
        params.append(periodo)

    conn = get_connection()
    df = pd.read_sql(base_query, conn, params=params)
    conn.close()
    return df
