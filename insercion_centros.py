import pandas as pd
import requests

df = pd.read_csv("./Datos_modificados_insercion_centro.csv", sep=";", header=0, encoding="utf-8")

# Endpoint y token
URL = "http://localhost:5000/soled/centro/registro"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlBFSDIyNjQ5IiwiZW1haWwiOiJlbWlsaW9AZW1haWwuY29tIiwicm9sIjoiYWRtaW4iLCJpYXQiOjE3NjMzOTkyNzUsImV4cCI6MTc2MzQwMjg3NX0.GsxWLB_jO4vfhvMrjFiK58kB53F384lnxPKfUYlX7fU"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

# Diccionario resultado
dict_codigos_centros = {}


list_centros = []

for index, row in df.iterrows():

    nombre_centro = row['centro_nombre']

    if nombre_centro in list_centros:
        continue
    list_centros.append(nombre_centro)

    # realizar la el montaje del post para el centro
    payload = {
        "nombre": row['centro_nombre'],
        "tipo_centro": row['centro_tipo'],
        "calle": row['centro_calle'],
        "numero": 1,
        "poblacion": row['centro_poblacion'],
        "provincia": row['centro_provincia'],
        "pais": row['centro_pais'],
        "cod_postal": str(row['centro_cod_postal']).strip()
    }
    
    #realizar el post y recoger de la respuesta el codigo_publico del centro 
    try:
        response = requests.post(URL, json=payload, headers=headers)
        data = response.json()
        
        if response.status_code == 200 or response.status_code == 201:
            
            codigo_publico = data.get("centro", {}).get('codigo_publico')


            dict_codigos_centros[nombre_centro] = codigo_publico
            print(f"Centro '{nombre_centro}' registrado con código público: {codigo_publico}")

        else:
            print(f"Error al registrar el centro '{nombre_centro}': {response.status_code} - {response.text}")  
            print(response.text)
    except Exception as e:
        print(f"Excepción al registrar el centro '{nombre_centro}': {str(e)}")
    
print("\n=== Diccionario final de centros registrados ===")
print(dict_codigos_centros)

# guardar diccionario en .txt
output_file = "codigos_centros.txt"
try:
    with open("codigos_centros.txt", "w", encoding="utf-8") as f:
        for centro, codigo in dict_codigos_centros.items():
            f.write(f"{centro}: {codigo}\n")  
    print(f"Archivo '{output_file}' guardado correctamente.")  
except Exception as e:
    print(f"Error al guardar el archivo '{output_file}': {str(e)}")
                

