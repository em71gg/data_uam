import pandas as pd
import requests
import time
import logging

# Configura logging para debug
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ========================= CONFIGURACIÓN =========================
URL_LOGIN = "http://localhost:5000/soled/alumno/login"
URL_CC    = "http://localhost:5000/soled/alumno/cuestionario/cc"
CSV       = "datos_completos.csv"

# ========================= CARGA Y LIMPIEZA DEL CSV =========================
df = pd.read_csv(CSV, sep=";", encoding="utf-8", low_memory=False)

# Reemplazo de valores NaN en celdas
df = df.replace({"nan": pd.NA, "NaN": pd.NA})

# Limpieza de nombres de columnas
df.columns = df.columns.astype(str)
df.columns = df.columns.str.replace("\ufeff", "")     # eliminar BOM
df.columns = df.columns.str.strip()

# Eliminar columnas cuyo nombre sea NaN, vacío, "Unnamed", etc.
df = df.loc[:, ~df.columns.isna()]
df = df.loc[:, df.columns != ""]
df = df.loc[:, ~df.columns.str.contains("^Unnamed", na=False)]
df = df.loc[:, df.columns.str.lower() != "nan"]

# Leer cabecera original para depuración
with open(CSV, "r", encoding="utf-8") as f:
    header = f.readline().strip().split(";")
print("\n=== CABECERA ORIGINAL DEL CSV ===")
print(header)
print("=================================\n")

# Asegurar alumno_id numérico
df["alumno_id"] = pd.to_numeric(df["alumno_id"], errors="coerce").astype("Int64")

# Fuerza conversión a int en columnas permitidas (ignora errores)
for col in df.columns:
    if col not in ["alumno_id", "codigo_clase"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

# ========================= CAMPOS PERMITIDOS PARA CC =========================
cols_permitidos = [
    "auton1","condeval1","conprevio1","pasoapaso1","particip1","dedica1","clarorg1","equidad1",
    "conprevio2","errorpos1","elogio1","dedica2","conecta1","ejemplos1","elogio2","mensapren1",
    "condeval2","clarobj1","clarorg2","ejemplos2","errorpos2","ritmorel1","mensapren2","equidad2",
    "novedad1","conecta2","ritmorel2","clarobj2","auton2","particip2","pasoapaso2","novedad2",
    *[f"CDC{i}" for i in range(1, 16)],
    *[f"CEM{str(i).zfill(2)}" for i in range(1, 17)],  # Fix: hasta 16 para incluir CEM16
    *[f"CV{str(i).zfill(2)}" for i in range(1, 49)],   # Fix: hasta 48 para incluir CV48
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

# ========================= FILTRAR COLUMNAS DEL CSV =========================
columnas_validas = set(cols_permitidos) | {"alumno_id", "codigo_clase"}

df = df[[col for col in df.columns if col in columnas_validas]]

print("\n=== COLUMNAS FINALES UTILIZADAS ===")
print(list(df.columns))
print("====================================\n")

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

    logging.info(f"Procesando alumno {alumno_id} - código clase: {codigo_publico}")

    # ---------- LOGIN ----------
    payload_login = {
        "id_alumno": alumno_id,
        "codigo_publico_clase": codigo_publico
    }

    max_retries = 5
    for attempt in range(max_retries):
        try:
            r = requests.post(URL_LOGIN, json=payload_login, timeout=5)
            if r.status_code == 429:
                time.sleep(2 ** attempt)
                continue
            if r.status_code != 200:
                raise ValueError(f"Status code {r.status_code}")
            data = r.json()
            if "token" not in data or "codigo_clase" not in data:
                raise KeyError("Faltan keys en respuesta JSON")
            token = data["token"]
            codigo_clase = data["codigo_clase"]
            df.at[idx, "login_status"] = "OK"
            df.at[idx, "token"] = token
            login_ok += 1
            logging.info("LOGIN OK")
            break
        except Exception as e:
            if attempt == max_retries - 1:
                df.at[idx, "login_status"] = f"ERROR {e}"
                login_error += 1
                logging.error(f"LOGIN ERROR: {e}")

    if df.at[idx, "login_status"] != "OK":
        continue

    # ---------- ENVÍO CC ----------
    headers = {"Authorization": f"Bearer {token}"}
    payload_cc = {"codigo_clase": codigo_clase}

    for col in cols_permitidos:
        value = row.get(col)
        if pd.isna(value):
            payload_cc[col] = 0  # Enviar 0 para NaN/missing
        else:
            try:
                v = int(value)
                if v == 9:
                    payload_cc[col] = None  # Enviar null para 9
                else:
                    payload_cc[col] = v
            except:
                continue  # Skip si no convertible

    try:
        r = requests.post(URL_CC, json=payload_cc, headers=headers, timeout=5)
        if r.status_code in [200, 201]:
            df.at[idx, "envio_status"] = "OK"
            cc_ok += 1
            logging.info("CC OK")
        else:
            raise ValueError(f"Status code {r.status_code} - {r.text}")
    except Exception as e:
        df.at[idx, "envio_status"] = f"ERROR {e}"
        cc_error += 1
        logging.error(f"CC ERROR: {e}")

    time.sleep(1)  # Aumentado para evitar rate limits

# ========================= GUARDAR RESULTADOS =========================
df.to_csv("resultados_envio.csv", sep=";", encoding="utf-8", index=False)

# ========================= RESUMEN =========================
print("\n================= RESUMEN FINAL =================")
print(f"Logins OK: {login_ok}")
print(f"Logins ERROR: {login_error}")
print(f"CC enviados OK: {cc_ok}")
print(f"CC enviados ERROR: {cc_error}")
print("=================================================\n")