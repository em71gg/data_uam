import pandas as pd

filepath = "datos_completos.csv"
df = pd.read_csv(filepath, sep=";", encoding="utf-8")



print([col for col in df.columns])