import pandas as pd


origen_datos = "./Datos_modificados_insercion_profesor_definitiva.csv"
df = pd.read_csv(origen_datos, sep=";", header=0, encoding="utf-8")

# En valores tengo las clases originales en values las objetivos
dict_asignaturas = {
    "Matemáticas": "Lengua y Literatura" ,    
    "Física": "Matemáticas",          
    "Química": "Sociales",  
    "Biología": "Idiomas",        
    "Historia": "Física",
    "Geografía": "Química",      
    "Lengua y Literatura": "Biología",
    "Inglés": "Tecnología",
    "Educación Física": "Religión",
    "Arte": "Educación Cívica",
    "Música": "Artes Plásticas",
    "Tecnología": "Educación Física",
    "Informática": "Educación Hogar",
    "Economía": "Artes Industriales",
    "Filosofía": "Educación Musical",
    "Ciencias Sociales": "Filosofía",
    "Educación Cívica": "Psicología"
}

dict_sexo = {
    "Femenino": "Masculino",
    "Masculino": "Femenino",
    }

df["prof_sexo"] = df["prof_sexo"].replace(dict_sexo)

df["prof_asignatura"] = df["prof_asignatura"].replace(dict_asignaturas)

before = pd.read_csv(origen_datos, sep=";", encoding="utf-8", dtype=str)
after = df

print((before["prof_asignatura"] != after["prof_asignatura"]).sum())
print((before["prof_sexo"] != after["prof_sexo"]).sum())

output_file = "Datos_modificados_insercion_profesor_arreglado_sexo_asignatura.csv"
df.to_csv(output_file, sep=";", index=False, encoding="utf-8-sig")
