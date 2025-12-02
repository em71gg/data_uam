# import pandas as pd

# filepath = "datos_completos.csv"
# df = pd.read_csv(filepath, sep=";", encoding="utf-8")



# print([col for col in df.columns])

import pandas as pd

df = pd.read_csv("datos_completos.csv", sep=";", encoding="utf-8", low_memory=False)

# Mostrar columnas problemáticas
problematic = [col for col in df.columns if pd.isna(col) or str(col).strip() == ""]
print("Columnas sospechosas:", problematic)

# Mostrar todas las columnas crudas con repr
print("Columnas exactas:")
for col in df.columns:
    print(repr(col))

print(df['codigo_clase'].dtype)