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

#Se elimino la columna: BMI.

data_limpia = data.drop(data.columns[[5]], axis=1)
data_limpia.info()



#Creando un nuevo archivo csv con la data limpia.

data_limpia.to_csv('data_limpia.csv', index=False)