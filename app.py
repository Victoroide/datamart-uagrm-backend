from flask import Flask, request, jsonify
import data_processing as dp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/facultades')
def facultades():
    facultades = dp.obtener_facultades()
    return jsonify(facultades)

@app.route('/carreras')
def carreras():
    carreras = dp.obtener_carreras()
    return jsonify(carreras)

@app.route('/periodos')
def periodos():
    periodos = dp.obtener_periodos()
    return jsonify(periodos)

@app.route('/inscritos')
def inscritos():
    facultad = request.args.get('facultad', 'Todas')
    carrera = request.args.get('carrera', 'Todas')
    periodo = request.args.get('periodo', None)
    df = dp.filtrar_datos(facultad, carrera, periodo)
    # Filtramos las filas con _INS numérico
    df = df[df['_INS'].notna() & df['_INS'].apply(lambda x: isinstance(x, (int, float)))]
    df_grouped = df.groupby('LOCALIDAD')['_INS'].sum().reset_index()
    data = df_grouped.to_dict(orient='records')
    return jsonify(data)

@app.route('/rendimiento')
def rendimiento():
    facultad = request.args.get('facultad', 'Todas')
    carrera = request.args.get('carrera', 'Todas')
    periodo = request.args.get('periodo', None)
    df = dp.filtrar_datos(facultad, carrera, periodo)
    # Filtramos filas con %APRO numérico
    df = df[df['%APRO'].notna() & df['%APRO'].apply(lambda x: isinstance(x, (int, float)))]
    df_grouped = df.groupby('LOCALIDAD')['%APRO'].mean().reset_index()
    data = df_grouped.to_dict(orient='records')
    return jsonify(data)

@app.route('/promedios')
def promedios():
    facultad = request.args.get('facultad', 'Todas')
    carrera = request.args.get('carrera', 'Todas')
    periodo = request.args.get('periodo', None)
    df = dp.filtrar_datos(facultad, carrera, periodo)
    # Filtramos filas con PPS numérico
    df = df[df['PPS'].notna() & df['PPS'].apply(lambda x: isinstance(x, (int, float)))]
    df_grouped = df.groupby('LOCALIDAD')['PPS'].mean().reset_index()
    df_grouped['PPS'] = df_grouped['PPS'].round(2)
    data = df_grouped.to_dict(orient='records')
    return jsonify(data)

@app.route('/nuevos_inscritos')
def nuevos_inscritos():
    facultad = request.args.get('facultad', 'Todas')
    carrera = request.args.get('carrera', 'Todas')
    periodo = request.args.get('periodo', None)
    df = dp.filtrar_datos(facultad, carrera, periodo)
    df = df[df['T_NUE'].notna() & df['T_NUE'].apply(lambda x: isinstance(x, (int, float)))]
    df_grouped = df.groupby('LOCALIDAD')['T_NUE'].sum().reset_index()
    data = df_grouped.to_dict(orient='records')
    return jsonify(data)

@app.route('/egresados')
def egresados():
    facultad = request.args.get('facultad', 'Todas')
    carrera = request.args.get('carrera', 'Todas')
    periodo = request.args.get('periodo', None)
    df = dp.filtrar_datos(facultad, carrera, periodo)
    df = df[df['EGRE'].notna() & df['EGRE'].apply(lambda x: isinstance(x, (int, float)))]
    df_grouped = df.groupby('LOCALIDAD')['EGRE'].sum().reset_index()
    data = df_grouped.to_dict(orient='records')
    return jsonify(data)

@app.route('/desercion')
def desercion():
    facultad = request.args.get('facultad', 'Todas')
    carrera = request.args.get('carrera', 'Todas')
    periodo = request.args.get('periodo', None)
    df = dp.filtrar_datos(facultad, carrera, periodo)
    # El código original verifica %REPR, ya lo tenemos como %REPR
    if '%REPR' not in df.columns:
        return jsonify({'error': "No se encontró la columna '%REPR' en los datos"}), 400

    df = df[df['%REPR'].notna() & df['%REPR'].apply(lambda x: isinstance(x, (int, float)))]
    df_grouped = df.groupby('LOCALIDAD')['%REPR'].sum().reset_index()
    data = df_grouped.to_dict(orient='records')
    return jsonify(data)

@app.route('/ppac')
def ppac():
    facultad = request.args.get('facultad', 'Todas')
    carrera = request.args.get('carrera', 'Todas')
    periodo = request.args.get('periodo', None)
    df = dp.filtrar_datos(facultad, carrera, periodo)
    df = df[df['PPAC'].notna() & df['PPAC'].apply(lambda x: isinstance(x, (int, float)))]
    df_grouped = df.groupby('LOCALIDAD')['PPAC'].mean().reset_index()
    data = df_grouped.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
