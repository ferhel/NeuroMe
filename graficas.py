import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV
data = pd.read_csv(r'data/data_limpia.csv')

# 1. Estadísticas descriptivas generales
def descripciones_generales():
    print("Estadísticas descriptivas generales:")
    print(data.describe())

def estadisticas_columna_age():
    print("\nEstadísticas de la columna 'Age':")
    print(data['Age'].describe())

def frecuencia_etnicidad():
    print("\nFrecuencia de los valores en 'Ethnicity':")
    print(data['Ethnicity'].value_counts())

def graficar_histograma_age():
    plt.figure(figsize=(10, 6))
    data['Age'].hist(bins=20, edgecolor='black')
    plt.title('Distribución de la Edad')
    plt.xlabel('Edad')
    plt.ylabel('Frecuencia')
    plt.show()

def graficar_barras_etnicidad():
    plt.figure(figsize=(10, 6))
    data['Ethnicity'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Distribución de Etnicidad')
    plt.xlabel('Etnicidad')
    plt.ylabel('Frecuencia')
    plt.xticks(rotation=45)
    plt.show()

def graficar_dispersion_age_education():
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Age'], data['EducationLevel'], color='green', alpha=0.5)
    plt.title('Edad vs Nivel de Educación')
    plt.xlabel('Edad')
    plt.ylabel('Nivel de Educación')
    plt.show()

def graficar_boxplot_age():
    plt.figure(figsize=(10, 6))
    sns.boxplot(data['Age'])
    plt.title('Distribución de la Edad (Boxplot)')
    plt.show()

def graficar_boxplot_age_por_etnicidad_y_genero():
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Ethnicity', y='Age', hue='Gender', data=data)
    plt.title('Distribución de Edad por Etnicidad y Género')
    plt.show()

def graficar_mapa_calor_correlaciones():
    plt.figure(figsize=(12, 8))
    corr = data.corr()  # Correlación entre las columnas numéricas
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Mapa de Calor de Correlaciones')
    plt.show()