import pandas as pd
import requests

input_file = "Datos_modificados_insercion_alumnos_numero_lista_corregido.csv"
df = pd.read_csv(input_file, sep=";", header=0, encoding="utf-8")

url_insertar_alumno = "http://localhost:5000/soled/alumno"

# End point y token
URL = "http://localhost:5000/soled/alumno/registro"
TOKEN = ""

headers = {
    "Content-Type": "application/json",
}

alumnos_ids = []

for index, row in df.iterrows():
    payload = {
        "codigo_publico_clase": row['codigo_clase'],
        "nacionalidad": row['alumno_nacionalidad'],
        "ciudad": row['alumno_ciudad'],
        "sexo": row['alumno_sexo'],
        "edad": row['alumno_edad'],
        "curso_escolar_id": int(row['curso_escolar_id']),
        "numero_lista": int(row['alumno_numero_lista']),
    }
    try:
        response = requests.post(URL, json=payload, headers=headers)
        data = response.json()
        
        if response.status_code == 200 or response.status_code == 201:
            id_alumno = data.get("alumno", {}).get('id')
            alumnos_ids.append(id_alumno)
            print(f"Alumno '{id_alumno}' registrado correctamente.")

        else:
            alumnos_ids.append(None)
            print(f"Error al registrar el alumno nº de lista '{row['alumno_numero_lista']}' de la clase '{row['codigo_clase']}': {response.status_code} - {response.text}")  
            print(response.text)

    except requests.exceptions.RequestException as e:
        alumnos_ids.append(None)
        print(f"Error de conexión al registrar el alumno nº de lista '{row['alumno_numero_lista']}' de la clase '{row['codigo_clase']}': {e}")

# Actualizar dataframe

df['alumno_id'] = alumnos_ids


# Reordenar las columnas para insertar la nueva columna en la posición deseada
cols = list(df.columns)
posicion  = cols.index('alumno_numero_lista') + 1
cols.insert(posicion, cols.pop(cols.index('alumno_id')))
df = df[cols]

# Guardar csv con la nueva columna
output_file = "datos_finales_alumnos_preparados.csv"
df.to_csv(output_file, sep=";", index=False, encoding="utf-8-sig")