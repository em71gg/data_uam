import pandas as pd
#import matplotlib.pyplot as plt

profesor_ce = {
    "D1_LID1": 5,
    "D9_SO4": 4,
    "D2_GE1": 5,
    "D9_SO2": 1,
    "D2_GE3": 5,
    "D8_AP4": 2,
    "D6_APD1": 5,
    "D5_INT2": 1,
    "D7_TC1": 4,
    "D4_EE2": 1,
    "D8_AP1": 4,
    "D3_COM2": 1,
    "D8_AP3": 4,
    "D2_GE4": 1,
    "D9_SO1": 5,
    "D2_GE2": 1,
    "D9_SO3": 5,
    "D1_LID2": 4,
    "D3_COM1": 5,
    "D8_AP2": 2,
    "D4_EE1": 5,
    "D7_TC2": 2,
    "D5_INT1": 5,
    "D6_APD2": 1,
    "P1_EJP1": 4,
    "P3_ASO4": 3,
    "P1_EJP3": 4,
    "P2_AAP1": 4,
    "P2_AAP3": 4,
    "P3_ASO1": 1,
    "P3_ASO3": 5,
    "P1_EJP2": 2,
    "P1_EJP4": 1,
    "P2_AAP2": 4,
    "P3_ASO2": 3,
    "P2_AAP4": 2,
    "A1_CF1": 5,
    "A7_ASR2": 2,
    "A2_INT1": 5,
    "A6_DIS2": 4,
    "A3_ESF1": 4,
    "A5_COP2": 1,
    "A4_COA1": 4,
    "A1_CF2": 2,
    "A5_COP1": 5,
    "A4_COA2": 2,
    "A6_DIS1": 2,
    "A2_INT2": 2,
    "A7_ASR1": 3,
    "A3_ESF2": 4,
    "F1_COP1": 5,
    "F2_RES1": 5,
    "F4_INT2": 2,
    "F3_CON1": 5,
    "F1_COP2": 2,
    "F2_RES2": 1,
    "F4_INT1": 5,
    "F3_CON2": 1,
    "P4_CMA1": 4,
    "P4_CMA2": 4,
    "P4_CMR1": 3,
    "P4_CMR2": 3,
    "P4_CMR3": 4,
    "P4_CMA3": 4,
    "P4_CMA4": 4,
    "P4_CMR4": 2,
    "SEGVIOL1": 4,
    "SEGACOAL1": 4,
    "SEGPROF1": 4,
    "SEGPCON1": 1,
    "SEGVIOL2": 5,
    "SEGACOAL2": 1,
    "SEGPROF2": 4,
    "SEGPCON2": 1,
    "SEGVIOL3": 5,
    "SEGACOAL3": 5,
    "SEGPROF3": 5,
    "SEGPCON3": 1,
    "CFISICAS1": 5,
    "CFISICAS2": 5,
    "CFISICAS3": 5,
    "CRD1": 5,
    "CRSS1": 5,
    "CRP1": 4,
    "CRA1": 5,
    "CRR1": 4,
    "CRF1": 5,
    "CRCC1": 5,
    "CRD2": 5,
    "CRP2": 5,
    "CRA2": 5,
    "CRF2": 5,
    "CRCC2": 5,
    "CRR2": 5,
    "CRSS2": 5
}

alumno_cc = {
    "codigo_clase": "9HUKDMTF",
    "auton1": 6,
    "condeval1": 3,
    "conprevio1": 4,
    "pasoapaso1": 2,
    "particip1": 5,
    "dedica1": 7,
    "clarorg1": 5,
    "equidad1": 7,
    "conprevio2": 8,
    "errorpos1": 2,
    "elogio1": 4,
    "dedica2": 3,
    "conecta1": 5,
    "ejemplos1": 4,
    "elogio2": 7,
    "mensapren1": 5,
    "condeval2": 6,
    "clarobj1": 4,
    "clarorg2": 6,
    "ejemplos2": 6,
    "errorpos2": 7,
    "ritmorel1": 8,
    "mensapren2": 4,
    "equidad2": 5,
    "novedad1": 5,
    "conecta2": 3,
    "ritmorel2": 5,
    "clarobj2": 6,
    "auton2": 5,
    "particip2": 5,
    "pasoapaso2": 4,
    "novedad2": 3,
    "CDC1": 4,
    "CDC2": 7,
    "CDC3": 3,
    "CDC4": 5,
    "CDC5": 4,
    "CDC6": 7,
    "CDC7": 4,
    "CDC8": 5,
    "CDC9": 4,
    "CDC10": 6,
    "CDC11": 5,
    "CDC12": 3,
    "CDC13": 4,
    "CDC14": 3,
    "CDC15": 4,
    "CEM01": 6,
    "CEM02": 7,
    "CEM03": 4,
    "CEM04": 3,
    "CEM05": 3,
    "CEM06": 2,
    "CEM07": 4,
    "CEM08": 3,
    "CEM09": 6,
    "CEM10": 4,
    "CEM11": 3,
    "CEM12": 5,
    "CEM13": 3,
    "CEM14": 1,
    "CEM15": 5,
    "CEM16": 4,
    "CV01": 2,
    "CV02": 3,
    "CV03": 4,
    "CV04": 1,
    "CV05": 5,
    "CV06": 2,
    "CV07": 4,
    "CV08": 3,
    "CV09": 1,
    "CV10": 5,
    "CV11": 2,
    "CV12": 3,
    "CV13": 4,
    "CV14": 1,
    "CV15": 5,
    "CV16": 2,
    "CV17": 4,
    "CV18": 3,
    "CV19": 1,
    "CV20": 5,
    "CV21": 2,
    "CV22": 3,
    "CV23": 4,
    "CV24": 1,
    "CV25": 5,
    "CV26": 2,
    "CV27": 3,
    "CV28": 4,
    "CV29": 1,
    "CV30": 5,
    "CV31": 2,
    "CV32": 3,
    "CV33": 4,
    "CV34": 1,
    "CV35": 5,
    "CV36": 2,
    "CV37": 3,
    "CV38": 4,
    "CV39": 1,
    "CV40": 5,
    "CV41": 2,
    "CV42": 3,
    "CV43": 4,
    "CV44": 1,
    "CV45": 5,
    "CV46": 2,
    "CV47": 3,
    "CV48": 4,
    "P_COSTO1": 1,
    "C_COMPET1": 3,
    "P_COSTO2": 2,
    "C_COMPET2": 4,
    "P_COSTO3": 5,
    "C_COMPET3": 1,
    "MOT01APR": 3,
    "MOT02RES": 2,
    "MOT03EVIT": 5,
    "MOT04RES": 4,
    "MOT05EVIT": 1,
    "MOT06APR": 3,
    "MOT07EVIT": 2,
    "MOT08APR": 5,
    "MOT09RES": 4,
    "EXP01CG": 3,
    "EXP02CC": 4,
    "EXP03HM": 5,
    "EXP04CE": 1,
    "EXP05HS": 2,
    "EXP06HC": 3,
    "EXP07CM": 4,
    "EXP08HE": 5,
    "EXP09CS": 1,
    "EXP10HG": 2,
    "INTSOCN1": 3,
    "INTSOCP1": 4,
    "INTSOCN2": 5,
    "INTSOCP2": 1,
    "INTSOCN3": 2,
    "INTSOCP3": 3,
    "INTSOCN4": 4,
    "INTSOCP4": 5,
    "INTSOCN5": 1,
    "INTSOCP5": 2,
    "INTSOCN6": 3,
    "INTSOCP6": 4,
    "expresult1": 5,
    "interes1": 4,
    "habilper1": 3,
    "satisfapren1": 2,
    "esfuerzo1": 1,
    "expresult2": 2,
    "interes2": 3,
    "satisfapren2": 4,
    "habilper2": 5,
    "esfuerzo2": 1,
    "expresult3": 2,
    "satisfapren3": 3,
    "habilper3": 4,
    "interes3": 5,
    "esfuerzo3": 1,
    "satisfapren4": 2,
    "CRITCDC1": 3,
    "CRITCDC2": 4,
    "CRITCEM1": 5,
    "CRITCDC3": 1,
    "CRITCDC4": 2,
    "CRITCEM2": 3,
    "CRITCDC5": 4,
    "CRITCDC6": 5,
    "CRITCEM3": 1,
    "CRITCDC7": 2,
    "CRITCDC8": 3,
    "CRITCEM4": 4
}

# Lista con las claves de ambos diccionarios
proper_cols = list(profesor_ce) + list(alumno_cc)

data = "./Datos.csv"
df = pd.read_csv(data, sep=";", header=0, encoding="utf-8")

# columnas a convertir a int64
cols_to_convert = [col for col in proper_cols if col in df.columns]


# Columnas del dataframe no insertadas a través de la api
# cols_calculated = [col for col in df.columns if col not in proper_cols]

# Convertir las columnas a int64, manejando errores
# for col in cols_to_convert:
#     df[col] = df[col].astype(str).str.strip()  # Eliminar espacios en blanco
#     df[col] = df[col].replace(['', ' ', '.', '#¡NULO!'], pd.NA)
#     df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64')

# print('Contenido de proper_cols= list(profesor_ce) + list(alumno_cc): ', proper_cols)
# print(cols_to_convert)

print(df.dtypes.to_string())

# cols_con_nan = df[cols_to_convert].columns[df[cols_to_convert].isna().any()]
# print('Columnas con NAN entre las esperadas', cols_con_nan.tolist(), '\n')
# cols_con_nan_2 = [col for col in df.columns if df[col].isna().any()]
# print('Columnas con NAN', cols_con_nan_2)

# Mostrar estadísticas descriptivas de todas las columnas
print(df.describe(include='all'))

# ============================================================== #
# === TRANSFORMACIONES POR CADA REGISTRO SEGÚN centro_nombre === # 
# === para preparar datos insercion centro                   === #
# ============================================================== #

# Asegurar que centro_nombre es int (si no lo está)
df["centro_nombre"] = pd.to_numeric(df["centro_nombre"], errors="coerce").astype("Int64")

# Guardamos su valor original para poder usarlo como "n"
df["n"] = df["centro_nombre"]

# 1) centro_nombre → varchar(255) con valor "Centro Soled n"
df["centro_nombre"] = df["n"].apply(lambda x: f"Centro Soled {x}")

# 2) centro_tipo → varchar(100) = "Público"
df["centro_tipo"] = "Público"

# 3) centro_calle → varchar(255) = "Calle de centro Educativo n"
df["centro_calle"] = df["n"].apply(lambda x: f"Calle de centro Educativo {x}")

# 4) centro_numero → int64 = 1
df["centro_numero"] = 1

# 5) centro_poblacion → varchar(255) = "Población de centro Educativo n"
df["centro_poblacion"] = df["n"].apply(lambda x: f"Población de centro Educativo {x}")

# 6) centro_provincia → varchar(100) = "Provincia de centro Educativo n"
df["centro_provincia"] = df["n"].apply(lambda x: f"Provincia de centro Educativo {x}")

# 7) centro_pais → varchar(100)
#      - Si pais = 1 → "España"
#      - Si pais = 2 → "Argentina"
df["centro_pais"] = df["centro_pais"].replace({
    1: "Costa Rica",
    2: "España"
}).astype(str)

# 8) centro_cod_postal → varchar(255)
def generar_cp(p_codigo):
    try:
        codigo = str(int(p_codigo))  # manejar valores inesperados
    except:
        return None

    if len(codigo) == 3:
        x = "0"
        y = codigo[0]
    elif len(codigo) == 4:
        x = codigo[0]
        y = codigo[1]
    else:
        return None

    return f"280{x}{y}"

df["centro_cod_postal"] = df["P_Codigo"].apply(generar_cp)

# Eliminamos columna auxiliar
df.drop(columns=["n"], inplace=True)

# Mostrar resultado final
print(df[[
    "centro_nombre", "centro_tipo", "centro_calle", "centro_numero",
    "centro_poblacion", "centro_provincia", "centro_pais", "centro_cod_postal"
]].head())

# Guardar el DataFrame modificado en un nuevo archivo CSV
output_file = "./Datos_modificados_insercion_centro.csv"
df.to_csv(output_file, sep=";", index=False, encoding="utf-8-sig")