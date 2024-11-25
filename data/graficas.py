import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV
data = pd.read_csv(r'data\data_limpia.csv')


# 1. Estadísticas descriptivas generales
print("Estadísticas descriptivas generales:")
print(data.describe())

# 2. Estadísticas de una columna específica, por ejemplo, 'Age'
print("\nEstadísticas de la columna 'Age':")
print(data['Age'].describe())

# 3. Distribución de valores (frecuencia de los valores únicos en 'Ethnicity')
print("\nFrecuencia de los valores en 'Ethnicity':")
print(data['Ethnicity'].value_counts())

# 4. Graficar histogramas y otros gráficos:

# 4.1 Histograma de la columna 'Age'
plt.figure(figsize=(10, 6))
data['Age'].hist(bins=20, edgecolor='black')
plt.title('Distribución de la Edad')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

# 4.2 Gráfico de barras para la columna 'Ethnicity'
plt.figure(figsize=(10, 6))
data['Ethnicity'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Distribución de Etnicidad')
plt.xlabel('Etnicidad')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.show()

# 4.3 Gráfico de dispersión entre 'Age' y 'EducationLevel'
plt.figure(figsize=(10, 6))
plt.scatter(data['Age'], data['EducationLevel'], color='green', alpha=0.5)
plt.title('Edad vs Nivel de Educación')
plt.xlabel('Edad')
plt.ylabel('Nivel de Educación')
plt.show()

# 4.4 Boxplot de la columna 'Age'
plt.figure(figsize=(10, 6))
sns.boxplot(data['Age'])
plt.title('Distribución de la Edad (Boxplot)')
plt.show()

# 4.5 Boxplot de 'Age' por 'Ethnicity' y 'Gender'
plt.figure(figsize=(10, 6))
sns.boxplot(x='Ethnicity', y='Age', hue='Gender', data=data)
plt.title('Distribución de Edad por Etnicidad y Género')
plt.show()

# 4.6 Mapa de calor de correlaciones entre las variables numéricas
plt.figure(figsize=(12, 8))
corr = data.corr()  # Correlación entre las columnas numéricas
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Mapa de Calor de Correlaciones')
plt.show()