import pandas as pd

# ============================= CONFIGURACIÓN =============================
archivo_original = "datos_finales_para_cuestionarios.csv"
salida_todo      = "datos_con_todas_l, las_columnas.csv"        # 1. Con TODAS (las originales + las 43 que faltan)
salida_solo_faltantes = "solo_las_columnas_que_faltan.csv"        # 2. Solo las 43 que no existen
# =========================================================================

# 1. Cargar el CSV original
print("Cargando el archivo...")
df = pd.read_csv(archivo_original, sep=';', dtype=str, low_memory=False)

print(f"Columnas originales: {len(df.columns)}")
print(f"Filas: {len(df)}")

# 2. Diccionario con todas las claves que deberían existir
campos_permitidos = {
    "alumno_id": 1, "codigo_clase": "9HUKDMTF", "auton1": 6, "condeval1": 3,  # ... (todo el que pegaste)
    # (no hace falta volver a escribirlo entero, solo necesitamos las claves)
}

columnas_deseadas = list(campos_permitidos.keys())

# 3. Detectar cuáles faltan
faltantes = [col for col in columnas_deseadas if col not in df.columns]
print(f"\nColumnas que faltan en el CSV: {len(faltantes)}")
print(faltantes)

# 4. Crear CSV 1: el original + columnas faltantes (rellenas con NaN o vacío)
for col in faltantes:
    df[col] = ""   # o pd.NA si prefieres

# Reordenar exactamente como en el diccionario (opcional pero bonito)
df = df.reindex(columns=columnas_deseadas)  # ¡solo las del dict, en ese orden!
# Si quieres TODAS (originales + nuevas), comenta la línea anterior y descomenta la de abajo:
# df = df[sorted(df.columns)]

df.to_csv(salida_todo, sep=';', index=False, encoding='utf-8-sig')
print(f"\n→ Archivo completo guardado: {salida_todo}")

# 5. Crear CSV 2: solo las 43 columnas que NO existían
df_faltantes = pd.DataFrame(columns=faltantes)
df_faltantes.to_csv(salida_solo_faltantes, sep=';', index=False, encoding='utf-8-sig')
print(f"→ Archivo con solo las columnas faltantes: {salida_solo_faltantes}")