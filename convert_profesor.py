import pandas as pd
import numpy as np

data = "./Datos_modificados_insercion_centro.csv"

df = pd.read_csv(data, sep=";", header=0, encoding="utf-8")

profesor_list = ['curso_escolar_id','prof_nombre', 'prof_apellidos', 'prof_edad' , 'prof_sexo', 'prof_nacionalidad','prof_titulación','prof_anyos_docencia', 'prof_anyos_antiguedad','prof_asignatura','prof_email', 'prof_contrasenya']

print(df[profesor_list].dtypes)

dict_asignaturas = {
    "Matemáticas": 1,    
    "Física": 2,          
    "Química": 3,  
    "Biología": 4,        
    "Historia": 5,
    "Geografía": 6,      
    "Lengua y Literatura": 7,
    "Inglés": 8,
    "Educación Física": 9,
    "Arte": 10,
    "Música": 11,
    "Tecnología": 12,
    "Informática": 13,
    "Economía": 14,
    "Filosofía": 15,
    "Ciencias Sociales": 16,
    "Educación Cívica": 17
}

dict_sexo = {
    "0": "Femenino",
    "1": "Masculino",
    "#¡NULO!" : "Otro"
    }

centro_codes = {
    
"Centro Soled 1": "LZM3D62T",
"Centro Soled 2": "P945SHYJ",
"Centro Soled 3": "AQ3NFQ8R",
"Centro Soled 4": "M68DAQ87",
"Centro Soled 5": "N84SVRAF",
"Centro Soled 6": "C8C2G3NY",
"Centro Soled 7": "9CAU8H4G",
"Centro Soled 8": "288VJYNR",
"Centro Soled 9": "U6WRAWBC",
"Centro Soled 10": "L5GQB7N6",
"Centro Soled 11": "2KMU9ZMH",
"Centro Soled 12": "Y5BYUH79",
"Centro Soled 13": "F8TQEQET",
"Centro Soled 14": "H2GJJ6M7",
"Centro Soled 27": "EJYVQ3KW",
"Centro Soled 28": "L53VA88T",
"Centro Soled 29": "GGWKJXAM",
"Centro Soled 30": "WT28XK9C",
"Centro Soled 31": "3LZTWRNS",
"Centro Soled 32": "WQS39LNE",
"Centro Soled 33": "GFK4KHQU",
"Centro Soled 34": "8DM9MN72",
"Centro Soled 15": "YX9C6W8V",
"Centro Soled 16": "F2L5ATM3",
"Centro Soled 17": "H43756NP",
"Centro Soled 18": "S33CUJX4",
"Centro Soled 19": "YU3WT2MR",
}

# Generar profesor nombre
def generar_prof_nombre(codigo):
    codigo_str = str(codigo).strip()
    if len(codigo_str) == 4:
        return f"Profesor {codigo_str[2]}{codigo_str[3]} Centro {codigo_str[0]}{codigo_str[1]}"
    elif len(codigo_str) == 3:
        return f"Profesor {codigo_str[1]}{codigo_str[2]} Centro {codigo_str[0]}"  
    else:
        return ''

df['prof_nombre'] = df['P_Codigo'].apply(generar_prof_nombre)

# Generar apellido profesor

df["prof_apellidos"] = df["P_Codigo"].astype(str).str[-2:].apply(lambda x: f"Apellidos {x}")

# Remplazar codigo de sexo por sexo
df["prof_sexo"] = df["prof_sexo"].astype(str).replace(dict_sexo)

# Remplazar id asignatura por nombre asignatura
df['prof_asignatura'] = df['prof_asignatura'].replace('#¡NULO!', np.nan)
df['prof_asignatura'] = pd.to_numeric(df['prof_asignatura'], errors='coerce')
inverse_asignaturas = {v: k for k, v in dict_asignaturas.items()}
df['prof_asignatura'] = df['prof_asignatura'].map(inverse_asignaturas)

# Generar email profesor
df["prof_email"] = df["P_Codigo"].astype(str) + "@email.com"

# Generar nacionalidad profesor
df["prof_nacionalidad"] = df["centro_pais"].replace({
    "España": "Española",
    "Costa Rica": "Costarricense"
})

df['codigo_publico'] = df['centro_nombre'].map(centro_codes)

# Reordenar columnas para insertar codigo_publico entre centro_nombre y centro_tipo
cols = list(df.columns)
centro_nombre_idx = cols.index('centro_nombre')
cols.insert(centro_nombre_idx + 1, cols.pop(cols.index('codigo_publico')))
df = df[cols]

print(df[profesor_list + ['codigo_publico']].head())

# Guardar en csv
output_file = "./Datos_modificados_insercion_profesor.csv"
df.to_csv(output_file, sep=";", index=False, encoding="utf-8-sig")