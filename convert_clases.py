import pandas as pd
import numpy as np

df = pd.read_csv("./Datos_modificados_insercion_profesor_arreglado_sexo_asignatura.csv", sep=";", header=0, encoding="utf-8")


#df['clase_curso'] = df['clase_curso'].replace("#¡NULO!", np.nan)

dict_codigos_clases = {
    1: "Primero de ESO",
    2: "Segundo de ESO",    
    3: "Tercero de ESO",
    4: "Cuarto de ESO",
    5: "Primero de Bachillerato",
    6: "Segundo de Bachillerato",
}



df["clase_curso"] = df["clase_curso"].replace(dict_codigos_clases)

output_file = "Datos_modificados_insercion_nombres_clases_final.csv"
df.to_csv(output_file, sep=";", index=False, encoding="utf-8-sig")

df2 = pd.read_csv("./Datos_modificados_insercion_nombres_clases_final.csv", sep=";", header=0, encoding="utf-8-sig")

clases_por_profesor_dict = {}

for index, row in df2.iterrows():
    nombre_profesor = row["prof_nombre"]
    codigo_clase = str(row["clase_curso"])  # <-- convertir a str siempre

    if nombre_profesor not in clases_por_profesor_dict:
        clases_por_profesor_dict[nombre_profesor] = []

    if codigo_clase not in clases_por_profesor_dict[nombre_profesor]:
        clases_por_profesor_dict[nombre_profesor].append(codigo_clase)

print("\n=== Diccionario final de profesores y sus clases ===")
print(clases_por_profesor_dict)

output_file = "clases_por_profesor.txt"
with open(output_file, "w", encoding="utf-8-sig") as f:
    for profesor, clases in clases_por_profesor_dict.items():
        clases_str = ", ".join(clases)
        f.write(f"{profesor}: {clases_str}\n")
