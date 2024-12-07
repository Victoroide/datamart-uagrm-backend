# app.py
from flask import Flask, request, jsonify
import data_processing as dp
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/facultades')
def facultades():
    facultades=dp.obtener_facultades()
    return jsonify(facultades)

@app.route('/carreras')
def carreras():
    carreras=dp.obtener_carreras()
    return jsonify(carreras)

@app.route('/periodos')
def periodos():
    periodos=dp.obtener_periodos()
    return jsonify(periodos)

@app.route('/carreras_por_facultad')
def carreras_por_facultad():
    facultad=request.args.get('facultad','Todas')
    if facultad=='Todas':
        carreras=dp.obtener_carreras()
        carreras=[c for c in carreras if c!='Todas']
        return jsonify(carreras)
    carreras=dp.obtener_carreras_por_facultad(facultad)
    return jsonify(carreras)

@app.route('/inscritos')
def inscritos():
    facultad=request.args.get('facultad','Todas')
    carrera=request.args.get('carrera','Todas')
    periodo=request.args.get('periodo',None)
    df=dp.filtrar_datos(facultad,carrera,periodo)
    df=df[df['T_INS'].notna()&df['T_INS'].apply(lambda x:isinstance(x,(int,float)))]
    df_grouped=df.groupby('LOCALIDAD')['T_INS'].sum().reset_index()
    data=df_grouped.to_dict(orient='records')
    return jsonify(data)

@app.route('/rendimiento')
def rendimiento():
    facultad=request.args.get('facultad','Todas')
    carrera=request.args.get('carrera','Todas')
    periodo=request.args.get('periodo',None)
    df=dp.filtrar_datos(facultad,carrera,periodo)
    df=df[df['POR_APRO'].notna()&df['POR_APRO'].apply(lambda x:isinstance(x,(int,float)))]
    df_grouped=df.groupby('LOCALIDAD')['POR_APRO'].mean().reset_index()
    data=df_grouped.to_dict(orient='records')
    return jsonify(data)

@app.route('/promedios')
def promedios():
    facultad=request.args.get('facultad','Todas')
    carrera=request.args.get('carrera','Todas')
    periodo=request.args.get('periodo',None)
    df=dp.filtrar_datos(facultad,carrera,periodo)
    df=df[df['PPS'].notna()&df['PPS'].apply(lambda x:isinstance(x,(int,float)))]
    df_grouped=df.groupby('LOCALIDAD')['PPS'].mean().reset_index()
    df_grouped['PPS']=df_grouped['PPS'].round(2)
    data=df_grouped.to_dict(orient='records')
    return jsonify(data)

@app.route('/nuevos_inscritos')
def nuevos_inscritos():
    facultad=request.args.get('facultad','Todas')
    carrera=request.args.get('carrera','Todas')
    periodo=request.args.get('periodo',None)
    df=dp.filtrar_datos(facultad,carrera,periodo)
    df=df[df['T_NUE'].notna()&df['T_NUE'].apply(lambda x:isinstance(x,(int,float)))]
    df_grouped=df.groupby('LOCALIDAD')['T_NUE'].sum().reset_index()
    data=df_grouped.to_dict(orient='records')
    return jsonify(data)

@app.route('/egresados')
def egresados():
    facultad=request.args.get('facultad','Todas')
    carrera=request.args.get('carrera','Todas')
    periodo=request.args.get('periodo',None)
    df=dp.filtrar_datos(facultad,carrera,periodo)
    df=df[df['EGRE'].notna()&df['EGRE'].apply(lambda x:isinstance(x,(int,float)))]
    df_grouped=df.groupby('LOCALIDAD')['EGRE'].sum().reset_index()
    data=df_grouped.to_dict(orient='records')
    return jsonify(data)

@app.route('/desercion')
def desercion():
    facultad=request.args.get('facultad','Todas')
    carrera=request.args.get('carrera','Todas')
    periodo=request.args.get('periodo',None)
    df=dp.filtrar_datos(facultad,carrera,periodo)
    if 'POR_REPR' not in df.columns:
        return jsonify([]),200
    df=df[df['POR_REPR'].notna()&df['POR_REPR'].apply(lambda x:isinstance(x,(int,float)))]
    df_grouped=df.groupby('LOCALIDAD')['POR_REPR'].sum().reset_index()
    data=df_grouped.to_dict(orient='records')
    return jsonify(data)

@app.route('/ppac')
def ppac():
    facultad=request.args.get('facultad','Todas')
    carrera=request.args.get('carrera','Todas')
    periodo=request.args.get('periodo',None)
    df=dp.filtrar_datos(facultad,carrera,periodo)
    df=df[df['PPAC'].notna()&df['PPAC'].apply(lambda x:isinstance(x,(int,float)))]
    df_grouped=df.groupby('LOCALIDAD')['PPAC'].mean().reset_index()
    data=df_grouped.to_dict(orient='records')
    return jsonify(data)

@app.route('/preset_data')
def preset_data():
    preset=request.args.get('preset',type=int)
    facultad=request.args.get('facultad','Todas')
    carrera=request.args.get('carrera','Todas')
    periodo=request.args.get('periodo','')
    localidad=request.args.get('localidad','Todas')
    modalidad=request.args.get('modalidad','Todas')
    df=dp.filtrar_preset_datos(preset,facultad,carrera,periodo,localidad,modalidad)
    if len(df)==0:
        return jsonify([])
    cols={
        1:("LOCALIDAD",["T_INS"]),
        2:("NOMBRE_CARRERA",["T_INS"]),
        3:("LOCALIDAD",["T_NUE"]),
        4:("NOMBRE_FACULTAD",["T_INS"]),
        5:("LOCALIDAD",["T_INS"]),
        6:("NOMBRE_CARRERA",["T_INS"]),
        7:("MODALIDAD",["T_INS"]),
        8:("PERIODO",["TIT"]),
        9:("NOMBRE_FACULTAD",["TIT"]),
        10:("PERIODO",["EGRE"]),
        11:("NOMBRE_FACULTAD",["EGRE"]),
        12:("PERIODO",["T_INS","TIT"]),
        13:("NOMBRE_FACULTAD",["T_INS","TIT"]),
        14:("PERIODO",["POR_SNOT"]),
        15:("NOMBRE_FACULTAD",["POR_SNOT"]),
        16:("PERIODO",["POR_SNOT","POR_APRO","POR_REPR","MORA_PERCENT"]),
        17:("NOMBRE_FACULTAD",["POR_SNOT","POR_APRO","POR_REPR","MORA_PERCENT"]),
        18:("PERIODO",["PPS"]),
        19:("NOMBRE_FACULTAD",["PPS"]),
        20:("PERIODO",["PPAC"]),
        21:("NOMBRE_FACULTAD",["PPAC"]),
        22:("PERIODO",["POR_CON_0"]),
        23:("NOMBRE_FACULTAD",["POR_CON_0"])
    }
    if preset==0:
        return jsonify([])
    ejeX,campos=cols[preset]
    agg={}
    for c in campos:
        if c in ["T_INS","T_NUE","TIT","EGRE"]:
            agg[c]='sum'
        else:
            agg[c]='mean'
    grouped=df.groupby(ejeX).agg(agg).reset_index()
    data=grouped.to_dict(orient='records')
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)
