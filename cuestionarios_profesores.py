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

# === Depuración: mostrar la cabecera real del CSV ===
with open(CSV, "r", encoding="utf-8") as f:
    header = f.readline().strip().split(";")
    print("\n=== CABECERA ORIGINAL DEL CSV ===")
    print(header)
    print("=================================\n")

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