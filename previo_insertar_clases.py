import pandas as pd

dict_codigos_clases = {
    "Primero de ESO": '1º de ESO',
    "Segundo de ESO": '2º de ESO',
    "Tercero de ESO": '3º de ESO',
    "Cuarto de ESO": '4º de ESO',
    "Primero de Bachillerato": '1º de Bachillerato',
    "Segundo de Bachillerato": '2º de Bachillerato',
}

input_file_path = './Datos_modificados_insercion_nombres_clases_final.csv'
df = pd.read_csv(input_file_path, sep=';', header=0, encoding='utf-8')

df['clase_curso'] = df['clase_curso'].map(dict_codigos_clases).fillna(df['clase_curso'])

output_file_path = './Datos_modificados_insercion_nombres_clases_corregidos_clase_curso.csv'
df.to_csv(output_file_path, sep=';', index=False, encoding='utf-8-sig')


