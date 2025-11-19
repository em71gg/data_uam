import pandas as pd
from sqlalchemy import create_engine
import secrets
import string
import numpy as np

# --- Config ---
engine = create_engine('mysql+pymysql://root:password@localhost/soled')
ALPHANUM = string.ascii_uppercase + string.digits

def gen_codigo(long=8):
    return ''.join(secrets.choice(ALPHANUM) for _ in range(long))

# --- Leer CSV ---
df = pd.read_csv('datos_origen.csv')  # Ajusta columnas según lo que te den

with engine.begin() as conn:
    # ================================
    # 1. CENTROS (generar código)
    # ================================
    centros_raw = df[['nombre_centro', 'tipo_centro', 'calle', 'numero', 
                      'poblacion', 'provincia', 'pais', 'cod_postal']].drop_duplicates()
    centros = centros_raw.copy()
    centros.columns = ['nombre', 'tipo_centro', 'calle', 'numero', 
                       'poblacion', 'provincia', 'pais', 'cod_postal']
    centros['codigo_publico_centro'] = [gen_codigo() for _ in range(len(centros))]
    centros.to_sql('centro', conn, if_exists='append', index=False)

    # Guardar mapeo: nombre → código
    centro_map = dict(zip(centros_raw['nombre_centro'], centros['codigo_publico_centro']))

    # ================================
    # 2. CURSOS ESCOLARES
    # ================================
    cursos = df[['curso_escolar_id', 'curso_descripcion']].drop_duplicates()
    cursos.columns = ['id', 'descripcion']
    cursos.to_sql('curso_escolar', conn, if_exists='append', index=False)

    # ================================
    # 3. PROFESORES (activo=1)
    # ================================
    prof_raw = df[['prof_nombre', 'prof_apellidos', 'prof_edad', 'prof_sexo',
                   'prof_nacionalidad', 'prof_titulacion', 'prof_anyos_docencia',
                   'prof_anyos_antiguedad', 'prof_asignatura', 'prof_email',
                   'prof_contrasenya', 'nombre_centro', 'curso_escolar_id']].drop_duplicates()

    profesores = prof_raw.copy()
    profesores.columns = ['nombre', 'apellidos', 'edad', 'sexo', 'nacionalidad',
                          'titulacion', 'anyos_docencia', 'anyos_antiguedad',
                          'asignatura', 'email', 'contrasenya', 'nombre_centro', 'curso_escolar_id']
    profesores['codigo_publico_centro'] = profesores['nombre_centro'].map(centro_map)
    profesores['acuerdo_confidencialidad'] = True
    profesores['activo'] = 1  # ¡Forzado!
    profesores = profesores.drop(columns=['nombre_centro'])
    profesores.to_sql('profesor', conn, if_exists='append', index=False)

    # Mapeo: email → id_profesor
    prof_ids = pd.read_sql("SELECT id, email FROM profesor", conn)
    prof_map = dict(zip(prof_ids['email'], prof_ids['id']))

    # ================================
    # 4. CLASES (generar código)
    # ================================
    clases_raw = df[['clase_curso', 'prof_email', 'curso_escolar_id']].drop_duplicates()
    clases = clases_raw.copy()
    clases['codigo_publico_clase'] = [gen_codigo() for _ in range(len(clases))]
    clases['profesor_id'] = clases['prof_email'].map(prof_map)
    clases = clases[['clase_curso', 'curso_escolar_id', 'codigo_publico_clase', 'profesor_id']]
    clases.columns = ['curso', 'curso_escolar_id', 'codigo_publico_clase', 'profesor_id']
    clases.to_sql('clase', conn, if_exists='append', index=False)

    clase_map = dict(zip(
        zip(clases_raw['clase_curso'], clases_raw['prof_email']),
        clases['codigo_publico_clase']
    ))

    # ================================
    # 5. ALUMNOS
    # ================================
    alumnos_raw = df[['alumno_nacionalidad', 'alumno_ciudad', 'alumno_sexo',
                      'alumno_edad', 'alumno_numero_lista', 'clase_curso', 'prof_email', 'curso_escolar_id']]
    alumnos = alumnos_raw.copy()
    key = tuple(zip(alumnos['clase_curso'], alumnos['prof_email']))
    alumnos['codigo_publico_clase'] = [clase_map.get(k, gen_codigo()) for k in key]
    alumnos = alumnos[['alumno_nacionalidad', 'alumno_ciudad', 'alumno_sexo',
                       'alumno_edad', 'curso_escolar_id', 'alumno_numero_lista', 'codigo_publico_clase']]
    alumnos.columns = ['nacionalidad', 'ciudad', 'sexo', 'edad', 'curso_escolar_id', 'numero_lista', 'codigo_publico_clase']
    alumnos.to_sql('alumno', conn, if_exists='append', index=False)

    # ================================
    # 6. CUESTIONARIO CE
    # ================================
    ce_items = [col for col in df.columns if col.startswith(('D', 'P', 'A', 'F', 'SEG', 'CFIS', 'CR')) 
                and len(col) >= 5 and col[1].isdigit() and col[3].isdigit()]
    ce_data = df[['prof_email'] + ce_items].dropna(subset=['prof_email'])
    ce_data['id_profesor'] = ce_data['prof_email'].map(prof_map)
    ce_data['id_centro'] = df['nombre_centro'].map(centro_map)
    ce_data['curso_escolar_id'] = df['curso_escolar_id']
    ce_final = ce_data[ce_items + ['id_profesor', 'id_centro', 'curso_escolar_id']]
    ce_final.to_sql('ce', conn, if_exists='append', index=False)

    # ================================
    # 7. CUESTIONARIO CC
    # ================================
    cc_items = [col for col in df.columns if col in 
                [f'auton{i}' for i in range(1,3)] + 
                [f'condeval{i}' for i in range(1,3)] + 
                [f'CDC{i}' for i in range(1,16)] + 
                [f'CEM{i:02d}' for i in range(1,17)] + 
                [f'CV{i}' for i in range(1,37)]]

    cc_data = df[['clase_curso', 'prof_email'] + cc_items].copy()
    key = tuple(zip(cc_data['clase_curso'], cc_data['prof_email']))
    cc_data['codigo_clase'] = [clase_map.get(k, None) for k in key]
    cc_final = cc_data[['codigo_clase'] + cc_items]
    cc_final = cc_final.dropna(subset=['codigo_clase'])
    cc_final.to_sql('cc', conn, if_exists='append', index=False)