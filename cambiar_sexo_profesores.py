import pandas as pd


dict_sexo = {
    "0": "Masculino",
    "1": "Femenino",
    "No declarado" : "Otro"
    }
data = "./Datos_modificados_insercion_profesor.csv"

df = pd.read_csv(data, sep=";", header=0, encoding="utf-8")

# Remplazar codigo de sexo por sexo
df["prof_sexo"] = df["prof_sexo"].astype(str).replace(dict_sexo)

# Guardar en csv
output_file = "./Datos_modificados_insercion_profesor_corregido_sexo.csv"
df.to_csv(output_file, sep=";", index=False, encoding="utf-8-sig")