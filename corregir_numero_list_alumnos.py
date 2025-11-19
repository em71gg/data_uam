import pandas as pd

input_file = "Datos_modificados_insercion_alumnos_preparada.csv"
df = pd.read_csv(input_file, sep=";", header=0, encoding="utf-8")

df['alumno_numero_lista'] = df['alumno_numero_lista'].astype(int)   

output_file = "./Datos_modificados_insercion_alumnos_numero_lista_corregido.csv"
df.to_csv(output_file, sep=";", index=False, encoding="utf-8-sig")
print(f"\n[LISTO] Archivo generado: {output_file}")