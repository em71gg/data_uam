import pandas as pd


input_file = "Datos_modificados_insercion_clase_creacion_columna_codigo_publico_clase.csv"
df = pd.read_csv(input_file, sep=";", header=0, encoding="utf-8")    

dict_sexo = {
    "0": "Femenino",
    "1": "Masculino",
    "#¡NULO!": "Otro"
}

# Reemplazar código sexo
df["alumno_sexo"] = df["alumno_sexo"].astype(str).replace(dict_sexo)

# Generar alumno_numero_lista reiniciado por clave
df["alumno_numero_lista"] = df.groupby("codigo_clase").cumcount() + 1

# dar valor a resto de los campos de los alumnos

df['alumno_nacionalidad'] = df['prof_nacionalidad']

df['alumno_ciudad'] = df['centro_poblacion']


# Guardar en csv
output_file = "./Datos_modificados_insercion_alumnos_preparada.csv"
df.to_csv(output_file, sep=";", index=False, encoding="utf-8-sig")
print(f"\n[LISTO] Archivo generado: {output_file}")