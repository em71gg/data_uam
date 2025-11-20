# import pandas as pd
# import requests
# import time

# URL_LOGIN = "http://localhost:5000/soled/profesor/login"
# URL_CE = "http://localhost:5000/soled/profesor/cuestionario/ce"
# CSV = "datos_finales_para_cuestionarios.csv"

# df = pd.read_csv(CSV, sep=";", encoding="utf-8")
# df.columns = df.columns.str.strip()

# # 1. Login único por profesor
# tokens_dict = {}
# headers = {
#     "Content-Type": "application/json",
# }
# for email in df["prof_email"].unique():
#     try:
#         payload_login = {
#             "email": email, 
#             "contrasenya": "Password@123"
#         }
#         response_login = requests.post(URL_LOGIN, json=payload_login, headers=headers)
#         token = response_login.json().get("token")
#         if token:
#             tokens_dict[email] = token
#             print(f"Login OK → {email}")
#         else:
#             print(f"Token no recibido → {email}")
#     except Exception as e:
#         print(f"Error login {email}: {e}")
#     # time.sleep(0.1)

# print(f"\nSubiendo 1 CE por profesor ({len(tokens_dict)} profesores)...\n")

# # UN SOLO POST por profesor 

# for email, token in tokens_dict.items():
#     headers["Authorization"] = f"Bearer {token}"
    
#     # Tomamos cualquier fila del profesor (todas sus clases tienen las mismas respuestas)
#     fila = df[df["prof_email"] == email].iloc[0]
    
#     payload = {
#         "D1_LID1": df['D1_LID1'],
#         "D9_SO4": df['D9_SO4'],
#         "D2_GE1": df["D2_GE1"],
#         "D9_SO2": df["D9_SO2"],
#         "D2_GE3": df["D2_GE3"],
#         "D8_AP4": df["D8_AP4"],
#         "D6_APD1": df["D6_APD1"],
#         "D5_INT2": df["D5_INT2"],
#         "D7_TC1": df['D7_TC1'],
#         "D4_EE2": df['D4_EE2'],
#         "D8_AP1": df['D8_AP1'], 
#         "D3_COM2": df['D3_COM2'],
#         "D8_AP3": df['D8_AP3'],
#         "D2_GE4": df['D2_GE4'],
#         "D9_SO1": df['D9_SO1'],
#         "D2_GE2": df['D2_GE2'],
#         "D9_SO3": df['D9_SO3'],
#         "D1_LID2": df['D1_LID2'],
#         "D3_COM1": df['D3_COM1'],
#         "D8_AP2": df['D8_AP2'],
#         "D4_EE1": df['D4_EE1'],
#         "D7_TC2": df['D7_TC2'],
#         "D5_INT1": df['D5_INT1'],
#         "D6_APD2": df['D6_APD2'],
#         "P1_EJP1": df['P1_EJP1'],
#         "P3_ASO4": df['P3_ASO4'],
#         "P1_EJP3": df['P1_EJP3'],
#         "P2_AAP1": df['P2_AAP1'],
#         "P2_AAP3": df['P2_AAP3'],
#         "P3_ASO1": df['P3_ASO1'],
#         "P3_ASO3": df['P3_ASO3'],
#         "P1_EJP2": df['P1_EJP2'],
#         "P1_EJP4": df['P1_EJP4'],
#         "P2_AAP2": df['P2_AAP2'],
#         "P3_ASO2": df['P3_ASO2'],
#         "P2_AAP4": df['P2_AAP4'],
#         "A1_CF1": df['A1_CF1'],
#         "A7_ASR2": df['A7_ASR2'],
#         "A2_INT1": df['A2_INT1'],
#         "A6_DIS2": df['A6_DIS2'],
#         "A3_ESF1": df['A3_ESF1'],
#         "A5_COP2": df['A5_COP2'],
#         "A4_COA1": df['A4_COA1'],
#         "A1_CF2": df['A1_CF2'],
#         "A5_COP1": df['A5_COP1'],
#         "A4_COA2": df['A4_COA2'],
#         "A6_DIS1": df['A6_DIS1'],
#         "A2_INT2": df['A2_INT2'],
#         "A7_ASR1": df['A7_ASR1'],
#         "A3_ESF2": df['A3_ESF2'],
#         "F1_COP1": df['F1_COP1'],
#         "F2_RES1": df['F2_RES1'],
#         "F4_INT2": df['F4_INT2'],
#         "F3_CON1": df['F3_CON1'],
#         "F1_COP2": df['F1_COP2'],
#         "F2_RES2": df['F2_RES2'],
#         "F4_INT1": df['F4_INT1'],
#         "F3_CON2": df['F3_CON2'],
#         "P4_CMA1": df['P4_CMA1'],
#         "P4_CMA2": df['P4_CMA2'],
#         "P4_CMR1": df['P4_CMR1'],
#         "P4_CMR2": df['P4_CMR2'],
#         "P4_CMR3": df['P4_CMR3'],
#         "P4_CMA3": df['P4_CMA3'],
#         "P4_CMA4": df['P4_CMA4'],
#         "P4_CMR4": df['P4_CMR4'],
#         "SEGVIOL1": df['SEGVIOL1'],
#         "SEGACOAL1": df['SEGACOAL1'],
#         "SEGPROF1": df['SEGPROF1'],
#         "SEGPCON1": df['SEGPCON1'],
#         "SEGVIOL2": df['SEGVIOL2'],
#         "SEGACOAL2": df['SEGACOAL2'],
#         "SEGPROF2": df['SEGPROF2'],
#         "SEGPCON2": df['SEGPCON2'],
#         "SEGVIOL3": df['SEGVIOL3'],
#         "SEGACOAL3": df['SEGACOAL3'],
#         "SEGPROF3": df['SEGPROF3'],
#         "SEGPCON3": df['SEGPCON3'],
#         "CFISICAS1": df['CFISICAS1'],
#         "CFISICAS2": df['CFISICAS2'],
#         "CFISICAS3": df['CFISICAS3'],
#         "CRD1": df['CRD1'],
#         "CRSS1": df['CRSS1'],
#         "CRP1": df['CRP1'],
#         "CRA1": df['CRA1'],
#         "CRR1": df['CRR1'],
#         "CRF1": df['CRF1'],
#         "CRCC1": df['CRCC1'],
#         "CRD2": df['CRD2'],
#         "CRP2": df['CRP2'],
#         "CRA2": df['CRA2'],
#         "CRF2": df['CRF2'],
#         "CRCC2": df['CRCC2'],
#         "CRR2": df['CRR2'],
#         "CRSS2": df['CRSS2']
#     }
#     try:
#         response_ce = requests.post(URL_CE, json=payload, headers=headers)
#         if response_ce.status_code in (200, 201):
#             exitos += 1
#             clases = df[df["prof_email"] == email]["codigo_clase"].unique()
#             print(f"CE subido → {fila['prof_nombre']} {fila['prof_apellidos']} (clases: {', '.join(clases)})")
#         else:
#             fallos += 1
#             print(f"Error {email}: {response_ce.status_code} → {response_ce.text[:120]}")
#     except Exception as e:
#         fallos += 1
#         print(f"Error conexión {email}: {e}")

# print(f"\nFINALIZADO → {exitos} éxitos | {fallos} fallos")

import pandas as pd
import requests
import time

# ========================= CONFIGURACIÓN =========================
URL_LOGIN = "http://localhost:5000/soled/profesor/login"
URL_CE    = "http://localhost:5000/soled/profesor/cuestionario/ce"
CSV       = "datos_finales_para_cuestionarios.csv"

# ========================= CARGA DE DATOS =========================
df = pd.read_csv(CSV, sep=";", encoding="utf-8")
df.columns = df.columns.str.strip()

# ========================= LOGIN ÚNICO POR PROFESOR =========================
print("Iniciando login de profesores...\n")
tokens = {}

for email in df["prof_email"].unique():
    payload_login = {
        "email": email,
        "contrasenya": "Password@123"
    }
    try:
        r = requests.post(URL_LOGIN, json=payload_login, timeout=10)
        if r.status_code == 200:
            token = r.json().get("token")
            if token:
                tokens[email] = token
                print(f"Login OK → {email}")
            else:
                print(f"No se recibió token → {email}")
        else:
            print(f"Login falló ({r.status_code}) → {email} | {r.text[:100]}")
    except Exception as e:
        print(f"Error de conexión en login → {email}: {e}")
    time.sleep(0.1)

print(f"\n{len(tokens)} profesores autenticados. Subiendo CE...\n")
print("=" * 80)

# ========================= COLUMNAS DEL CUESTIONARIO CE =========================
columnas_ce = [col for col in df.columns if col[0] in "DPAF" or col.startswith(
    ("SEG", "CR", "auton", "condeval", "pasoapaso", "particip", "dedica", "clarorg",
     "equidad", "errorpos", "elogio", "conecta", "ejemplos", "mensapren", "clarobj",
     "ritmorel", "novedad", "CDC", "CEM", "CV", "CFISICAS"))]

# ========================= ENVÍO: 1 CE POR PROFESOR =========================
headers = {"Content-Type": "application/json"}
exitos = fallos = 0

for email, token in tokens.items():
    headers["Authorization"] = f"Bearer {token}"
    
    # Cualquier fila del profesor vale (todas sus clases tienen respuestas idénticas)
    fila = df[df["prof_email"] == email].iloc[0]
    
    # Construcción limpia del payload
    payload = {}
    for col in columnas_ce:
        valor = fila[col]
        if pd.notna(valor) and str(valor).strip() not in ("", "9"):
            payload[col] = int(valor)
        # Si es 9 o NaN → se omite (el backend lo interpreta como "no responde")

    try:
        r = requests.post(URL_CE, json=payload, headers=headers, timeout=20)
        if r.status_code in (200, 201):
            exitos += 1
            clases = ", ".join(df[df["prof_email"] == email]["codigo_clase"].unique())
            print(f"CE subido → {fila['prof_nombre']} {fila['prof_apellidos']} (clases: {clases})")
        else:
            fallos += 1
            print(f"Error {email} → {r.status_code} | {r.text[:150]}")
    except Exception as e:
        fallos += 1
        print(f"Error de conexión {email} → {e}")
    
    time.sleep(0.2)  # Ser amable con el servidor

# ========================= RESUMEN FINAL =========================
print("\n")
print(f"PROCESO COMPLETADO")
print(f"CE subidos correctamente : {exitos}")
print(f"Errores                  : {fallos}")
print(f"Total profesores          : {len(tokens)}")
print("\n")