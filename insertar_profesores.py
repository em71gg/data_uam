import pandas as pd
import requests


df = pd.read_csv("./Datos_modificados_insercion_profesor_arreglado_sexo_asignatura.csv", sep=";", header=0, encoding="utf-8")

# Endpoint y token
URL = "http://localhost:5000/soled/profesor/registro"
TOKEN = ""

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

list_profesores = []
insercion_profesores = open ("insercion profesores.json", "a", encoding="utf-8")

for index, row in df.iterrows():
    nombre_profesor = row['prof_nombre']
    email_profesor = row['prof_email']

    if nombre_profesor in list_profesores:
        continue
    list_profesores.append(nombre_profesor)

    # realizar el montaje del post para el profesor

    payload = {
        "nombre": row['prof_nombre'], 
        "apellidos": row['prof_apellidos'],
        "edad": int(row['prof_edad']),
        "sexo": row['prof_sexo'],
        "nacionalidad": row['prof_nacionalidad'],
        "titulacion": row['prof_titulacion'],
        "anyos_docencia": int(row['prof_anyos_docencia']),
        "anyos_antiguedad": int(row['prof_anyos_antiguedad']),     
        "asignatura": row['prof_asignatura'],
        "acuerdo_confidencialidad": True,
        "curso_escolar_id": int(row['curso_escolar_id']),
        "email": row['prof_email'],
        "contrasenya": row['prof_contrasenya'],
        "codigo_publico_centro": row['codigo_publico']
    }

    # Realizar el post y recoger la respuesta del servidor
    try:
        response = requests.post(URL, json=payload, headers=headers)
        data = response.json()

        # Guardar la respuesta EXACTA tal cual llegó
        insercion_profesores.write(response.text + "\n")
        
        if response.status_code == 200 or response.status_code == 201:
            
            print(f"Profesor '{nombre_profesor}' registrado correctamente.")

        else:
            print(f"Error al registrar el profesor '{nombre_profesor}' con email '{email_profesor}': {response.status_code} - {response.text}")  
            print(response.text)
    except Exception as e:
        print(f"Excepción al registrar el profesor '{nombre_profesor}' con email '{email_profesor}': {str(e)}")

insercion_profesores.close()