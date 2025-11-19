import pandas as pd

input_file = "datos_finales_alumnos_preparados.csv"
df = pd.read_csv(input_file, sep=";", header=0, encoding="utf-8")

df = df.replace('#¡NULO!', 9)
df = df.apply(lambda col: pd.to_numeric(col, errors='ignore'))
output_file = "datos_finales_para_cuestionarios.csv"
df.to_csv(output_file, sep=";", index=False, encoding="utf-8-sig")
print(f"[LISTO] Archivo generado: {output_file}")   