import pandas as pd
import requests


# Parse the provided dict text into a Python dictionary
clases_text = """
Profesor 01 Centro 1: 1º de ESO
Profesor 02 Centro 1: 1º de ESO
Profesor 03 Centro 1: 1º de ESO
Profesor 04 Centro 1: 1º de ESO
Profesor 05 Centro 1: 2º de ESO, 1º de ESO
Profesor 06 Centro 1: 4º de ESO
Profesor 07 Centro 1: 4º de ESO
Profesor 08 Centro 1: 3º de ESO
Profesor 09 Centro 1: 2º de ESO
Profesor 10 Centro 1: 2º de ESO
Profesor 11 Centro 1: 2º de Bachillerato
Profesor 12 Centro 1: 4º de ESO
Profesor 13 Centro 1: 1º de ESO
Profesor 14 Centro 1: 2º de ESO
Profesor 15 Centro 1: 2º de Bachillerato
Profesor 16 Centro 1: 2º de Bachillerato
Profesor 17 Centro 1: 2º de Bachillerato
Profesor 18 Centro 1: 1º de ESO
Profesor 01 Centro 2: 1º de Bachillerato
Profesor 02 Centro 2: 2º de ESO
Profesor 03 Centro 2: 2º de ESO
Profesor 04 Centro 2: 1º de ESO
Profesor 05 Centro 2: 3º de ESO
Profesor 07 Centro 2: 2º de ESO
Profesor 08 Centro 2: 3º de ESO
Profesor 09 Centro 2: 4º de ESO
Profesor 10 Centro 2: 1º de Bachillerato
Profesor 01 Centro 3: 2º de ESO
Profesor 02 Centro 3: 1º de ESO
Profesor 03 Centro 3: 2º de ESO
Profesor 04 Centro 3: 3º de ESO
Profesor 06 Centro 3: 1º de ESO
Profesor 07 Centro 3: 2º de ESO
Profesor 08 Centro 3: 3º de ESO
Profesor 09 Centro 3: 1º de Bachillerato
Profesor 10 Centro 3: 1º de ESO
Profesor 11 Centro 3: 1º de Bachillerato
Profesor 12 Centro 3: 3º de ESO
Profesor 13 Centro 3: 4º de ESO
Profesor 15 Centro 3: 1º de Bachillerato
Profesor 01 Centro 4: 1º de ESO
Profesor 02 Centro 4: 1º de ESO
Profesor 03 Centro 4: 2º de ESO
Profesor 04 Centro 4: 2º de ESO
Profesor 05 Centro 4: 3º de ESO
Profesor 06 Centro 4: 3º de ESO
Profesor 07 Centro 4: 1º de Bachillerato
Profesor 08 Centro 4: 1º de ESO
Profesor 09 Centro 4: 4º de ESO
Profesor 10 Centro 4: 4º de ESO
Profesor 01 Centro 5: 1º de ESO
Profesor 03 Centro 5: 4º de ESO
Profesor 05 Centro 5: 1º de Bachillerato
Profesor 06 Centro 5: 3º de ESO
Profesor 01 Centro 6: 4º de ESO
Profesor 02 Centro 6: 3º de ESO
Profesor 03 Centro 6: 1º de Bachillerato
Profesor 04 Centro 6: 2º de ESO
Profesor 05 Centro 6: 1º de ESO
Profesor 06 Centro 6: 1º de ESO
Profesor 07 Centro 6: 1º de ESO
Profesor 01 Centro 7: 1º de Bachillerato
Profesor 02 Centro 7: 2º de ESO
Profesor 03 Centro 7: 1º de ESO
Profesor 04 Centro 7: 1º de ESO
Profesor 05 Centro 7: 2º de ESO
Profesor 06 Centro 7: 2º de ESO
Profesor 07 Centro 7: 3º de ESO
Profesor 08 Centro 7: 3º de ESO
Profesor 09 Centro 7: 4º de ESO
Profesor 10 Centro 7: 4º de ESO
Profesor 01 Centro 8: 1º de ESO
Profesor 02 Centro 8: 3º de ESO
Profesor 03 Centro 8: 1º de Bachillerato
Profesor 01 Centro 9: 1º de Bachillerato, 2º de Bachillerato
Profesor 03 Centro 9: 1º de ESO, 2º de ESO
Profesor 02 Centro 10: 1º de ESO
Profesor 03 Centro 10: 3º de ESO
Profesor 05 Centro 10: 2º de ESO
Profesor 06 Centro 10: 2º de ESO, 3º de ESO
Profesor 07 Centro 10: 1º de Bachillerato
Profesor 08 Centro 10: 2º de ESO
Profesor 09 Centro 10: 2º de ESO
Profesor 10 Centro 10: 1º de ESO
Profesor 11 Centro 10: 4º de ESO
Profesor 01 Centro 11: 1º de ESO
Profesor 02 Centro 11: 1º de ESO
Profesor 03 Centro 11: 2º de ESO
Profesor 04 Centro 11: 2º de ESO
Profesor 05 Centro 11: 3º de ESO
Profesor 06 Centro 11: 3º de ESO
Profesor 07 Centro 11: 4º de ESO
Profesor 08 Centro 11: 1º de Bachillerato
Profesor 09 Centro 11: 4º de ESO
Profesor 10 Centro 11: 1º de Bachillerato
Profesor 01 Centro 12: 2º de ESO
Profesor 02 Centro 12: 1º de Bachillerato
Profesor 04 Centro 12: 1º de ESO
Profesor 05 Centro 12: 4º de ESO
Profesor 06 Centro 12: 2º de ESO
Profesor 07 Centro 12: 2º de ESO
Profesor 08 Centro 12: 2º de ESO, 3º de ESO
Profesor 09 Centro 12: 2º de ESO
Profesor 10 Centro 12: 1º de ESO
Profesor 01 Centro 13: 4º de ESO
Profesor 02 Centro 13: 4º de ESO
Profesor 03 Centro 13: 4º de ESO, 1º de Bachillerato
Profesor 04 Centro 13: 1º de Bachillerato, 1º de ESO
Profesor 05 Centro 13: 1º de Bachillerato
Profesor 06 Centro 13: 4º de ESO
Profesor 07 Centro 13: 4º de ESO
Profesor 08 Centro 13: 1º de Bachillerato
Profesor 09 Centro 13: 1º de Bachillerato, 4º de ESO
Profesor 10 Centro 13: 4º de ESO
Profesor 01 Centro 14: 1º de ESO
Profesor 02 Centro 14: 2º de ESO
Profesor 03 Centro 14: 1º de Bachillerato
Profesor 04 Centro 14: 1º de ESO
Profesor 05 Centro 14: 4º de ESO
Profesor 07 Centro 14: 2º de ESO
Profesor 01 Centro 27: 1º de ESO
Profesor 02 Centro 27: 1º de ESO
Profesor 03 Centro 27: 2º de ESO
Profesor 04 Centro 27: 2º de ESO, 4º de ESO
Profesor 05 Centro 27: 3º de ESO
Profesor 06 Centro 27: 3º de ESO
Profesor 07 Centro 27: 4º de ESO
Profesor 08 Centro 27: 4º de ESO
Profesor 09 Centro 27: 1º de Bachillerato
Profesor 10 Centro 27: 1º de Bachillerato
Profesor 11 Centro 27: 2º de Bachillerato
Profesor 12 Centro 27: 2º de Bachillerato
Profesor 01 Centro 28: 1º de ESO
Profesor 02 Centro 28: 1º de ESO
Profesor 03 Centro 28: 2º de ESO
Profesor 04 Centro 28: 2º de ESO
Profesor 05 Centro 28: 3º de ESO
Profesor 06 Centro 28: 3º de ESO
Profesor 07 Centro 28: 4º de ESO
Profesor 08 Centro 28: 4º de ESO
Profesor 09 Centro 28: 1º de Bachillerato
Profesor 10 Centro 28: 1º de Bachillerato
Profesor 01 Centro 29: 1º de ESO
Profesor 02 Centro 29: 1º de ESO
Profesor 04 Centro 29: 2º de ESO
Profesor 05 Centro 29: 3º de ESO
Profesor 07 Centro 29: 4º de ESO
Profesor 09 Centro 29: 1º de Bachillerato
Profesor 11 Centro 29: 2º de ESO
Profesor 01 Centro 30: 1º de ESO
Profesor 02 Centro 30: 1º de ESO
Profesor 03 Centro 30: 2º de ESO
Profesor 04 Centro 30: 2º de ESO
Profesor 05 Centro 30: 3º de ESO
Profesor 06 Centro 30: 3º de ESO
Profesor 07 Centro 30: 4º de ESO
Profesor 09 Centro 30: 1º de Bachillerato
Profesor 10 Centro 30: 1º de Bachillerato
Profesor 11 Centro 30: 2º de Bachillerato, 4º de ESO
Profesor 12 Centro 30: 2º de Bachillerato, 1º de Bachillerato
Profesor 01 Centro 31: 1º de ESO
Profesor 02 Centro 31: 1º de ESO
Profesor 03 Centro 31: 2º de ESO
Profesor 04 Centro 31: 2º de ESO
Profesor 05 Centro 31: 3º de ESO
Profesor 06 Centro 31: 3º de ESO
Profesor 07 Centro 31: 4º de ESO
Profesor 08 Centro 31: 4º de ESO
Profesor 09 Centro 31: 1º de Bachillerato
Profesor 10 Centro 31: 1º de Bachillerato
Profesor 11 Centro 31: 2º de Bachillerato
Profesor 12 Centro 31: 2º de Bachillerato
Profesor 01 Centro 32: 1º de ESO
Profesor 02 Centro 32: 1º de ESO
Profesor 03 Centro 32: 2º de ESO
Profesor 04 Centro 32: 2º de ESO
Profesor 05 Centro 32: 3º de ESO
Profesor 06 Centro 32: 3º de ESO
Profesor 07 Centro 32: 4º de ESO
Profesor 08 Centro 32: 4º de ESO
Profesor 09 Centro 32: 1º de Bachillerato
Profesor 10 Centro 32: 1º de Bachillerato
Profesor 11 Centro 32: 2º de Bachillerato
Profesor 12 Centro 32: 2º de Bachillerato
Profesor 01 Centro 33: 1º de ESO
Profesor 02 Centro 33: 1º de ESO
Profesor 03 Centro 33: 2º de ESO
Profesor 04 Centro 33: 2º de ESO
Profesor 05 Centro 33: 2º de ESO
Profesor 06 Centro 33: 3º de ESO
Profesor 07 Centro 33: 3º de ESO
Profesor 08 Centro 33: 3º de ESO
Profesor 09 Centro 33: 4º de ESO
Profesor 10 Centro 33: 4º de ESO
Profesor 11 Centro 33: 1º de Bachillerato
Profesor 12 Centro 33: 2º de Bachillerato
Profesor 01 Centro 34: 1º de ESO
Profesor 02 Centro 34: 1º de ESO
Profesor 03 Centro 34: 1º de ESO
Profesor 04 Centro 34: 2º de ESO, 1º de ESO
Profesor 05 Centro 34: 2º de ESO
Profesor 06 Centro 34: 3º de ESO
Profesor 07 Centro 34: 3º de ESO, 2º de ESO
Profesor 08 Centro 34: 4º de ESO
Profesor 09 Centro 34: 4º de ESO
Profesor 10 Centro 34: 1º de Bachillerato
Profesor 11 Centro 34: 1º de Bachillerato
Profesor 12 Centro 34: 2º de Bachillerato
Profesor 13 Centro 34: 2º de Bachillerato
Profesor 01 Centro 15: 1º de ESO
Profesor 02 Centro 15: 1º de ESO
Profesor 03 Centro 15: 2º de ESO
Profesor 04 Centro 15: 3º de ESO
Profesor 05 Centro 15: 3º de ESO
Profesor 06 Centro 15: 4º de ESO
Profesor 08 Centro 15: 4º de ESO
Profesor 09 Centro 15: 3º de ESO
Profesor 10 Centro 15: 2º de ESO
Profesor 11 Centro 15: 2º de ESO
Profesor 12 Centro 15: 1º de ESO
Profesor 01 Centro 16: 2º de Bachillerato
Profesor 02 Centro 16: 1º de Bachillerato, 0
Profesor 03 Centro 16: 4º de ESO
Profesor 04 Centro 16: 3º de ESO
Profesor 05 Centro 16: 2º de ESO
Profesor 06 Centro 16: 1º de ESO
Profesor 07 Centro 16: 1º de ESO
Profesor 08 Centro 16: 2º de ESO
Profesor 09 Centro 16: 3º de ESO
Profesor 10 Centro 16: 4º de ESO
Profesor 11 Centro 16: 1º de Bachillerato
Profesor 12 Centro 16: 2º de Bachillerato
Profesor 01 Centro 17: 2º de Bachillerato
Profesor 02 Centro 17: 1º de Bachillerato
Profesor 04 Centro 17: 3º de ESO
Profesor 06 Centro 17: 1º de ESO
Profesor 07 Centro 17: 1º de ESO
Profesor 08 Centro 17: 2º de ESO
Profesor 09 Centro 17: 3º de ESO
Profesor 10 Centro 17: 4º de ESO
Profesor 11 Centro 17: 1º de Bachillerato
Profesor 12 Centro 17: 2º de Bachillerato
Profesor 01 Centro 18: 2º de Bachillerato
Profesor 02 Centro 18: 1º de Bachillerato
Profesor 03 Centro 18: 4º de ESO
Profesor 04 Centro 18: 3º de ESO
Profesor 05 Centro 18: 2º de ESO
Profesor 06 Centro 18: 1º de ESO
Profesor 07 Centro 18: 1º de ESO
Profesor 08 Centro 18: 2º de ESO
Profesor 09 Centro 18: 3º de ESO
Profesor 10 Centro 18: 4º de ESO
Profesor 11 Centro 18: 1º de Bachillerato
Profesor 12 Centro 18: 2º de Bachillerato
Profesor 01 Centro 19: 2º de Bachillerato
Profesor 02 Centro 19: 1º de Bachillerato
Profesor 03 Centro 19: 4º de ESO
Profesor 04 Centro 19: 3º de ESO
Profesor 05 Centro 19: 2º de ESO
Profesor 06 Centro 19: 1º de ESO
Profesor 07 Centro 19: 1º de ESO
Profesor 08 Centro 19: 2º de ESO
Profesor 09 Centro 19: 3º de ESO
Profesor 11 Centro 19: 1º de Bachillerato
Profesor 12 Centro 19: 2º de Bachillerato
"""

# Parse text to dict
clases_por_profesor = {}
for line in clases_text.strip().split('\n'):
    if ':' in line:
        profesor, clases_str = line.split(':', 1)
        profesor = profesor.strip()
        clases = [c.strip() for c in clases_str.split(',') if c.strip() != '0']  # Ignore '0'
        clases_por_profesor[profesor] = clases

# Load the CSV to get emails (assuming prof_nombre is unique key)
df = pd.read_csv("./Datos_modificados_insercion_nombres_clases_corregidos_clase_curso.csv", sep=";", header=0, encoding="utf-8")

# mapeo profesor  -> email
prof_email_dict = df.groupby('prof_nombre')['prof_email'].first().to_dict()

# diccionario para guardar los códigos públicos

prof_class_to_code = {}

# Login y registro de clases
for profesor, clases in clases_por_profesor.items():
    email = prof_email_dict.get(profesor)
    if not email:
        print(f"No existe email para {profesor}")
        continue

    # Login to get token
    URL_LOGIN = "http://localhost:5000/soled/profesor/login"  
    headers_login = {
        "Content-Type": "application/json"
    }
    payload_login = {
        "email": email,
        "contrasenya": "Password@123"  # Corrected password
    }
    try:
        response_login = requests.post(URL_LOGIN, json=payload_login, headers=headers_login)
        response_login.raise_for_status()  # Raise error if not 200
        data_login = response_login.json()
        token_profesor = data_login.get("token")
        if not token_profesor:
            print(f"No no se recibe token para {profesor}")
            continue
    except Exception as e:
        print(f"Error al iniciar sesión para el profesor '{profesor}' con email '{email}': {str(e)}")
        continue

    # regiistrar clases sin duplicar
    registrar_clase_url = "http://localhost:5000/soled/clase"
    headers_clase = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token_profesor}"
    }

    for clase in set(clases):  # Unique classes
        payload_clase = {
            "curso": clase,
            "curso_escolar_id": 2024
        }
        try:
            response_clase = requests.post(registrar_clase_url, json=payload_clase, headers=headers_clase)
            response_clase.raise_for_status()
            data_clase = response_clase.json()
            # Assume the response has 'clase' with 'codigo_publico'
            codigo_publico = data_clase.get('codigo_publico')
            if codigo_publico:
                prof_class_to_code[(profesor, clase)] = codigo_publico
                print(f"Clase '{clase}' registrada para el {profesor} con código {codigo_publico}")
            else:
                print(f"No codigo_publico en la respuesta para la clase '{clase}' de {profesor}")
        except Exception as e:
            print(f"Error registrando la clase '{clase}' para {profesor}: {str(e)}")

# Actualizar el dataframe
df['codigo_clase'] = None
for index, row in df.iterrows():
    profesor = row['prof_nombre']
    clase = row['clase_curso']
    codigo = prof_class_to_code.get((profesor, clase))
    if codigo:
        df.at[index, 'codigo_clase'] = codigo

# REordenar las columnas para insertar la nueva
cols = list(df.columns)
pos_clase = cols.index('clase_curso') + 1
cols.insert(pos_clase, cols.pop(cols.index('codigo_clase')))
df = df[cols]

# Save the updated CSV
output_file = "Datos_modificados_insercion_clase_creacion_columna_codigo_publico_clase.csv"
df.to_csv(output_file, sep=";", index=False, encoding="utf-8-sig")
print(f"\n[LISTO] Archivo generado: {output_file}")
