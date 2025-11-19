import pandas as pd
#import matplotlib.pyplot as plt
data = "./Datos_modificados_insercion_centro.csv"

df = pd.read_csv(data, sep=";", header=0, encoding="utf-8")

df["centro_cod_postal"] = df["centro_cod_postal"].astype(str)

df.to_csv("Datos_modificados_insercion_centro.csv", sep=";", index=False, encoding="utf-8-sig")

print(df['centro_cod_postal'].dtype)