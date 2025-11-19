import pandas as pd
import numpy as np

df = pd.read_csv("./Datos_modificados_insercion_profesor_final.csv", sep=";", header=0, encoding="utf-8")

# Asegurarse de que la columna 'prof_anyos_docencia' no tenga valores nulos

df['prof_anyos_docencia'] = df['prof_anyos_docencia'].replace("#¡NULO!", np.nan)

# sustituir todos los nan por la media de la columna pero en int
mean_edad = df['prof_anyos_docencia'].astype(float).mean()
df['prof_anyos_docencia'] = df['prof_anyos_docencia'].astype(float).fillna(mean_edad).round().astype(int)
print(df['prof_anyos_docencia'].head())


df['prof_anyos_antiguedad'] = df['prof_anyos_antiguedad'].replace("#¡NULO!", np.nan)

# sustituir todos los nan por la media de la columna pero en int
mean_edad = df['prof_anyos_antiguedad'].astype(float).mean()
df['prof_anyos_antiguedad'] = df['prof_anyos_antiguedad'].astype(float).fillna(mean_edad).round().astype(int)
print(df['prof_anyos_antiguedad'].head())


# Guardar en csv
output_file = "./Datos_modificados_insercion_profesor_definitiva.csv"
df.to_csv(output_file, sep=";", index=False, encoding="utf-8-sig")