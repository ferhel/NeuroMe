import pandas as pd

# #Se asigna la ruta del archivo CSV que contiene los datos sobre la enfermedad de Alzheimer.
ruta = "alzheimers_disease_data.csv"

# Leer el archivo CSV.
data = pd.read_csv(ruta)

# Imprimir una tupla con el número de filas y columnas del DataFrame.
print(data.shape)

# Mostrar las primeras 5 filas para visualizar.
print(data.head())



# Comprobación de los tipos de datos.

# Busqueda de datos faltantes.

data.info()  # Obteniendo resumen conciso del DataFrame.

data.isnull().sum()  # No hay datos faltantes.


#Buscando filas repetidas.

print(f"Tamaño de la data sin filtrar: {data.shape}")

#Aplicando el método para eliminar duplicados.
print(f"Tamaño de la data verificando que no hay duplicados: {data.drop_duplicates().shape}")

#No se han encontrado filas duplicadas.
data.duplicated().sum()



#Eliminando columnas de datos que no utilizaremos.

#Se elimino esta columna de datos debido a que tomaremos informacion
#con relación al ambito mental de la salud.

print("Tamaño de la data sin filtrar:")
data.info()

print("Tamaño de la data filtrada:")

#Se elimino la columna: BMI,SystolicBP, DiastolicBP,CholesterolTotal, CholesterolLDL, CholesterolHDL,
#CholesterolTriglycerides.

data_limpia = data.drop(data.columns[[5, 17, 18, 19, 20, 21, 22]], axis=1)
data_limpia.info()

#Modificando el formato de la información de algunas columnas númericas a columnas de texto.
#La razon de esto es para una mejor visualización de la información mostrada al usuario, la base de datos presenta su información en base a números
#esto hace que el entendimiento de los datos se dificulte debido a:

#1: Solo se conoce el valor que representa el número en la columna gracias a la documentación de la base de datos.
#2: Se pierde a la vista el valor buscado porque se utilizan los mismo valores representativos en varias columnas.
#3: No es intuitivo ni práctico para el usuario.

#Mapeo de los valores númericos que cambiaremos.

#Columnas que obtienen valores diferentes a 0 = "No" y 1 = "Si".
mapeados = {
    "Gender" : {0: "Hombre", 1: "Mujer"},
    "Ethnicity" : {0: "Caucásico", 1: "Afroamericano", 2: "Asiatico", 3: "Otros"},
    "EducationLevel" : {0: "Nada", 1: "Escuela secundaria", 2: "Universidad", 3: "Superior"}
}

# Reemplazar los valores en cada columna usando un bucle.
for columna, mapeado in mapeados.items():
  data_limpia[columna] = data_limpia[columna].replace(mapeado)


# Columnas a excluir del reemplazo de 0 y 1.
excluir_columnas = ["Gender", "Ethnicity", "EducationLevel"]

# Reemplazo de 0 y 1 a "No" y "Si".
for columna in data_limpia.columns:
  if columna not in excluir_columnas:
    data_limpia[columna] = data_limpia[columna].replace({0: "No", 1: "Si"})

data_limpia.head()


#Creando un nuevo archivo csv con la data limpia.

data_limpia.to_csv('data_limpia.csv', index=False)