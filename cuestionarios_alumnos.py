import pandas as pd
import requests

input_file = "datos_finales_alumnos_preparados.csv"
df = pd.read_csv(input_file, sep=";", header=0, encoding="utf-8")


# URL_LOGIN_ALUMNO = "http://localhost:5000/soled/alumno/login"
# URL_INSERTAR_CUESTIONARIO = "http://localhost:5000/soled/cuestionario"

# headers = {
#     "Content-Type": "application/json",
# }

# for index, row in df.iterrows():
#     # Login del alumno para obtener token
#     payload_login = {
#         "id_alumno": row['alumno_id'],
#         "codigo_publico_clase": row['codigo_clase'],
#     }
#     try:
#         response_login = requests.post(URL_LOGIN_ALUMNO, json=payload_login, headers=headers)
#         data_login = response_login.json()
        
#         if response_login.status_code in (200, 201):
#             token_alumno = data_login.get("token")
#             print(f"Alumno '{row['alumno_id']}' logueado correctamente.")
#         else:
#             print(f"Error al loguear el alumno nº de lista '{row['alumno_numero_lista']}' de la clase '{row['codigo_clase']}': {response_login.status_code} - {response_login.text}")
#             continue

#     except requests.exceptions.RequestException as e:
#         print(f"Error de conexión al loguear el alumno nº de lista '{row['alumno_numero_lista']}' de la clase '{row['codigo_clase']}': {e}")
#         continue

#     # Insertar cuestionario
#     headers_cuestionario = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {token_alumno}"
#     }

    # payload_cuestionario = {
    #     "codigo_clase": row['codigo_clase'],
    #     "auton1": row["auton1"],
    #     "condeval1": row["condeval1"],
    #     "conprevio1": row["conprevio1"],
    #     "pasoapaso1": row["pasoapaso1"],
    #     "particip1": row["particip1"],
    #     "dedica1": row["dedica1"],  
    #     "clarorg1": row["clarorg1"],
    #     "equidad1": row["equidad1"],
    #     "conprevio2": row["conprevio2"],
    #     "errorpos1": row["errorpos1"],
    #     "elogio1": row["elogio1"],
    #     "dedica2": row["dedica2"],
    #     "conecta1": row["conecta1"],
    #     "ejemplos1": row["ejemplos1"],
    #     "elogio2": row["elogio2"],
    #     "mensapren1": row["mensapren1"],
    #     "condeval2": row["condeval2"],
    #     "clarobj1": row["clarobj1"],
    #     "clarorg2": row["clarorg2"],
    #     "ejemplos2": row["ejemplos2"],
    #     "errorpos2": row["errorpos2"],
    #     "ritmorel1": row["ritmorel1"],
    #     "mensapren2": row["mensapren2"],
    #     "equidad2": row["equidad2"],
    #     "novedad1": row["novedad1"],
    #     "conecta2": row["conecta2"],
    #     "ritmorel2": row["ritmorel2"],
    #     "clarobj2": row["clarobj2"],
    #     "auton2": row["auton2"],
    #     "particip2": row["particip2"],
    #     "pasoapaso2": row["pasoapaso2"],
    #     "novedad2": row["novedad2"],
    #     "CDC1": row["CDC1"],
    #     "CDC2": row["CDC2"],
    #     "CDC3": row["CDC3"],
    #     "CDC4": row["CDC4"],
    #     "CDC5": row["CDC5"],
    #     "CDC6": row["CDC6"],
    #     "CDC7": row["CDC7"],
    #     "CDC8": row["CDC8"],
    #     "CDC9": row["CDC9"],
    #     "CDC10": row["CDC10"],
    #     "CDC11": row["CDC11"],
    #     "CDC12": row["CDC12"],
    #     "CDC13": row["CDC13"],
    #     "CDC14": row["CDC14"],
    #     "CDC15": row["CDC15"],
    #     "CEM01": row["CEM01"],
    #     "CEM02": row["CEM02"],
    #     "CEM03": row["CEM03"],
    #     "CEM04": row["CEM04"],
    #     "CEM05": row["CEM05"],
    #     "CEM06": row["CEM06"],
    #     "CEM07": row["CEM07"],
    #     "CEM08": row["CEM08"],
    #     "CEM09": row["CEM09"]   ,
    #     "CEM10": row["CEM10"],
    #     "CEM11": row["CEM11"],
    #     "CEM12": row["CEM12"],
    #     "CEM13": row["CEM13"],
    #     "CEM14": row["CEM14"],
    #     "CEM15": row["CEM15"],
    #     "CEM16": row["CEM16"],
    #     "CV01": row["CV01"],
    #     "CV02": row["CV02"],
    #     "CV03": row["CV03"],
    #     "CV04": row["CV04"],
    #     "CV05": row["CV05"],
    #     "CV06": row["CV06"],
    #     "CV07": row["CV07"],
    #     "CV08": row["CV08"],
    #     "CV09": row["CV09"],
    #     "CV10": row["CV10"],
    #     "CV11": row["CV11"],
    #     "CV12": row["CV12"],
    #     "CV13": row["CV13"],
    #     "CV14": row["CV14"],
    #     "CV15": row["CV15"],
    #     "CV16": row["CV16"],
    #     "CV17": row["CV17"],
    #     "CV18": row["CV18"],
    #     "CV19": row["CV19"],
    #     "CV20": row["CV20"],
    #     "CV21": row["CV21"],
    #     "CV22": row["CV22"],
    #     "CV23": row["CV23"],
    #     "CV24": row["CV24"],
    #     "CV25": row["CV25"],
    #     "CV26": row["CV26"],
    #     "CV27": row["CV27"],
    #     "CV28": row["CV28"],
    #     "CV29": row["CV29"],
    #     "CV30": row["CV30"],
    #     "CV31": row["CV31"],
    #     "CV32": row["CV32"],
    #     "CV33": row["CV33"],
    #     "CV34": row["CV34"],
    #     "CV35": row["CV35"],
    #     "CV36": row["CV36"],
    #     "CV37": row["CV37"],
    #     "CV38": row["CV38"] ,
    #     "CV39": row["CV39"],
    #     "CV40": row["CV40"],
    #     "CV41": row["CV41"],
    #     "CV42": row["CV42"],
    #     "CV43": row["CV43"],
    #     "CV44": row["CV44"],
    #     "CV45": row["CV45"],
    #     "CV46": row["CV46"],
    #     "CV47": row["CV47"],
    #     "CV48": row["CV48"],
    #     "P_COSTO1": 1,
    #     "C_COMPET1": 3,
    #     "P_COSTO2": 2,
    #     "C_COMPET2": 4,
    #     "P_COSTO3": 5,
    #     "C_COMPET3": 1,
    #     "MOT01APR": 3,
    #     "MOT02RES": 2,
    #     "MOT03EVIT": 5,
    #     "MOT04RES": 4,
    #     "MOT05EVIT": 1,
    #     "MOT06APR": 3,
    #     "MOT07EVIT": 2,
    #     "MOT08APR": 5,
    #     "MOT09RES": 4,
    #     "EXP01CG": 3,
    #     "EXP02CC": 4,
    #     "EXP03HM": 5,
    #     "EXP04CE": 1,
    #     "EXP05HS": 2,
    #     "EXP06HC": 3,
    #     "EXP07CM": 4,
    #     "EXP08HE": 5,
    #     "EXP09CS": 1,
    #     "EXP10HG": 2,
    #     "INTSOCN1": 3,
    #     "INTSOCP1": 4,
    #     "INTSOCN2": 5,
    #     "INTSOCP2": 1,
    #     "INTSOCN3": 2,
    #     "INTSOCP3": 3,
    #     "INTSOCN4": 4,
    #     "INTSOCP4": 5,
    #     "INTSOCN5": 1,
    #     "INTSOCP5": 2,
    #     "INTSOCN6": 3,
    #     "INTSOCP6": 4,
    #     "expresult1": 5,
    #     "interes1": 4,
    #     "habilper1": 3,
    #     "satisfapren1": 2,
    #     "esfuerzo1": 1,
    #     "expresult2": 2,
    #     "interes2": 3,
    #     "satisfapren2": 4,
    #     "habilper2": 5,
    #     "esfuerzo2": 1,
    #     "expresult3": 2,
    #     "satisfapren3": 3,
    #     "habilper3": 4,
    #     "interes3": 5,
    #     "esfuerzo3": 1,
    #     "satisfapren4": 2,
    #     "CRITCDC1": 3,
    #     "CRITCDC2": 4,
    #     "CRITCEM1": 5,
    #     "CRITCDC3": 1,
    #     "CRITCDC4": 2,
    #     "CRITCEM2": 3,
    #     "CRITCDC5": 4,
    #     "CRITCDC6": 5,
    #     "CRITCEM3": 1,
    #     "CRITCDC7": 2,
    #     "CRITCDC8": 3,
    #     "CRITCEM4": 4
    # }

nombre_columna_cuestionario = "CRITCEM4"  # Cambia esto por el nombre real de la columna que deseas verificar
if nombre_columna_cuestionario in df.columns:
    print("La columna existe")
else:
    print("La columna NO existe")
    # try:
    #     response_cuestionario = requests.post(URL_INSERTAR_CUESTIONARIO, json=payload_cuestionario, headers=headers_cuestionario)
    #     data_cuestionario = response_cuestionario.json()
        
    #     if response_cuestionario.status_code == 200 or response_cuestionario.status_code == 201:
    #         print(f"Cuestionario para el alumno '{row['alumno_id']}' insertado correctamente.")
    #     else:
    #         print(f"Error al insertar el cuestionario para el alumno nº de lista '{row['alumno_numero_lista']}' de la clase '{row['codigo_clase']}': {response_cuestionario.status_code} - {response_cuestionario.text}")

    # except requests.exceptions.RequestException as e:
    #     print(f"Error de conexión al insertar el cuestionario para el alumno nº de lista '{row['alumno_numero_lista']}') de la clase '{row['codigo_clase']}': {e}")