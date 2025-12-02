import pandas as pd
import requests
import time

# ========================= CONFIGURACIÓN =========================
URL_LOGIN = "http://localhost:5000/soled/alumno/login"
URL_CC    = "http://localhost:5000/soled/alumno/cuestionario/cc"
CSV       = "datos_completos.csv"

# ========================= CARGA Y LIMPIEZA DEL CSV =========================
df = pd.read_csv(CSV, sep=";", encoding="utf-8")

# df = df.applymap(lambda x: pd.NA if str(x).strip().lower() == "nan" else x)
# df.columns = df.columns.str.strip().str.replace(r'\s+', '', regex=True)

df = df.replace({"nan": pd.NA, "NaN": pd.NA})
df.columns = df.columns.str.replace("\ufeff", "")  # quitar BOM si existe


# Depuración: mostrar la cabecera real del CSV

with open(CSV, "r", encoding="utf-8") as f:
    header = f.readline().strip().split(";")
print("\n=== CABECERA ORIGINAL DEL CSV ===")
print(header)
print("=================================\n")

# Eliminar columnas cuyo nombre sea NaN (float)
df = df.loc[:, ~df.columns.isna()]
df = df.loc[:, ~df.columns.str.contains("^Unnamed", na=False)]
df = df.loc[:, df.columns != ""]

if "" in df.columns:
    df = df.drop(columns=[""])

df["alumno_id"] = pd.to_numeric(df["alumno_id"], errors="coerce").astype("Int64")

# ========================= CAMPOS PERMITIDOS PARA CC =========================
# Removed "codigo_clase" to avoid overwriting the internal code
cols_permitidos = [
    "auton1","condeval1","conprevio1","pasoapaso1","particip1","dedica1","clarorg1","equidad1",
    "conprevio2","errorpos1","elogio1","dedica2","conecta1","ejemplos1","elogio2","mensapren1",
    "condeval2","clarobj1","clarorg2","ejemplos2","errorpos2","ritmorel1","mensapren2","equidad2",
    "novedad1","conecta2","ritmorel2","clarobj2","auton2","particip2","pasoapaso2","novedad2",
    *[f"CDC{i}" for i in range(1, 15+1)],
    *[f"CEM{str(i).zfill(2)}" for i in range(1, 16+1)],
    *[f"CV{str(i).zfill(2)}" for i in range(1, 48+1)],
    "P_COSTO1","C_COMPET1","P_COSTO2","C_COMPET2","P_COSTO3","C_COMPET3",
    "MOT01APR","MOT02RES","MOT03EVIT","MOT04RES","MOT05EVIT","MOT06APR",
    "MOT07EVIT","MOT08APR","MOT09RES",
    "EXP01CG","EXP02CC","EXP03HM","EXP04CE","EXP05HS","EXP06HC","EXP07CM","EXP08HE",
    "EXP09CS","EXP10HG",
    "INTSOCN1","INTSOCP1","INTSOCN2","INTSOCP2","INTSOCN3","INTSOCP3",
    "INTSOCN4","INTSOCP4","INTSOCN5","INTSOCP5","INTSOCN6","INTSOCP6",
    "expresult1","interes1","habilper1","satisfapren1","esfuerzo1",
    "expresult2","interes2","satisfapren2","habilper2","esfuerzo2",
    "expresult3","satisfapren3","habilper3","interes3","esfuerzo3","satisfapren4",
    "CRITCDC1","CRITCDC2","CRITCEM1","CRITCDC3","CRITCDC4","CRITCEM2",
    "CRITCDC5","CRITCDC6","CRITCEM3","CRITCDC7","CRITCDC8","CRITCEM4"
]

# ========================= RESULTADOS =========================
df["login_status"] = ""
df["token"] = ""
df["envio_status"] = ""

login_ok = 0
login_error = 0
cc_ok = 0
cc_error = 0

print("\n================= INICIO DEL PROCESO =================\n")

# ========================= BUCLE PRINCIPAL =========================
for idx, row in df.iterrows():

    alumno_id = str(int(row["alumno_id"]))
    codigo_publico = row["codigo_clase"]

    print(f"\n---- Alumno {alumno_id} ---- codigo clase: {codigo_publico}")

    # ---------- LOGIN ----------
    payload_login = {
        "id_alumno": alumno_id,
        "codigo_publico_clase": codigo_publico
    }
    print("Payload login:", payload_login)
    try:
        print("Payload login:", payload_login)
        r = requests.post(URL_LOGIN, json=payload_login)
        if r.status_code != 200:
            df.at[idx, "login_status"] = f"ERROR {r.status_code}"
            login_error += 1
            print(f"LOGIN ERROR {r.status_code}")
            continue

        data = r.json()
        token = data["token"]
        codigo_clase = data["codigo_clase"]

        df.at[idx, "login_status"] = "OK"
        df.at[idx, "token"] = token
        login_ok += 1
        print(f"LOGIN OK — token obtenido")

    except Exception as e:
        df.at[idx, "login_status"] = f"EXCEPTION {e}"
        login_error += 1
        print(f"LOGIN EXCEPTION {e}")
        continue

    # ---------- ENVÍO CC ----------
    headers = {"Authorization": f"Bearer {token}"}
    payload_cc = {"codigo_clase": codigo_clase}

    for col in cols_permitidos:
        if col in df.columns:
            value = row[col]

            if pd.isna(value):
                continue  # no enviar nada

            try:
                v = int(value)
            except:
                continue  # ignora textos extraños

            if v == 9:
                continue  # 9 = vacío → no enviar este campo
            
            payload_cc[col] = v

            # No else: skip setting to None, so missing fields default to NULL in DB

    print("Payload CC:", payload_cc)  # For debugging

    try:
        r = requests.post(URL_CC, json=payload_cc, headers=headers)

        if r.status_code == 200:
            df.at[idx, "envio_status"] = "OK"
            cc_ok += 1
            print("✔ CC enviado correctamente")
        else:
            df.at[idx, "envio_status"] = f"ERROR {r.status_code}"
            cc_error += 1
            print(f"ERROR enviando CC — status {r.status_code}")
            print(f"Response body: {r.text}")  # Add for more error details

    except Exception as e:
        df.at[idx, "envio_status"] = f"EXCEPTION {e}"
        cc_error += 1
        print(f"ERROR EXCEPTION enviando CC — {e}")

    time.sleep(0.2)

# ========================= GUARDAR RESULTADOS =========================
df.to_csv("resultados_envio.csv", sep=";", encoding="utf-8", index=False)

# ========================= RESUMEN =========================
print("\n================= RESUMEN FINAL =================")
print(f"Logins OK: {login_ok}")
print(f"Logins ERROR: {login_error}")
print(f"CC enviados OK: {cc_ok}")
print(f"CC enviados ERROR: {cc_error}")
print("=================================================\n")
print("Archivo generado: resultados_envio.csv\n")
print("Proceso finalizado.\n")