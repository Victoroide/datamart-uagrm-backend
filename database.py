import pyodbc

def get_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=DESKTOP-MNBF1KF\SQLEXPRESS;'
        'DATABASE=dataMart;'
        'Trusted_Connection=yes;'
    )
    return conn