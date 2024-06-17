import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# 4.1. Estadísticas de ciencia de datos: estadísticas descriptivas simples
def estadisticas_descriptivas_simples(data):
    df = pd.DataFrame(data, columns=["Datos"])
    print("Estadísticas Descriptivas Simples")
    print("Media:", df["Datos"].mean())
    print("Mediana:", df["Datos"].median())
    print("Desviación Estándar:", df["Datos"].std())
    print("Varianza:", df["Datos"].var())
    print("Mínimo:", df["Datos"].min())
    print("Máximo:", df["Datos"].max())

# 4.2. Estadísticas de ciencia de datos: enfoques comunes para el muestreo de datos
def enfoques_comunes_muestreo(data, sample_size):
    print("Enfoques Comunes para el Muestreo de Datos")
    # Muestreo aleatorio simple
    sample = np.random.choice(data, size=sample_size, replace=False)
    print("Muestreo Aleatorio Simple:", sample)

# 4.3. Estadísticas de ciencia de datos: estadísticas inferenciales
def estadisticas_inferenciales(data):
    print("Estadísticas Inferenciales")
    # Prueba de hipótesis - t-test
    t_stat, p_value = stats.ttest_1samp(data, popmean=np.mean(data))
    print("t-stat:", t_stat, "p-value:", p_value)

# 4.4. Estadísticas de ciencia de datos: uso de Python para calcular y visualizar estadísticas
def calcular_visualizar_estadisticas(data):
    print("Uso de Python para Calcular y Visualizar Estadísticas")
    plt.hist(data, bins=10, alpha=0.7, color='blue')
    plt.title('Histograma de los Datos')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.show()

# 4.5. Estadísticas de ciencia de datos: estadística inferencial aplicada
def estadistica_inferencial_aplicada(data1, data2):
    print("Estadística Inferencial Aplicada")
    # Prueba de hipótesis - t-test para dos muestras
    t_stat, p_value = stats.ttest_ind(data1, data2)
    print("t-stat:", t_stat, "p-value:", p_value)

# Ejemplo de uso de las funciones
def main():
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    data1 = np.array([1, 2, 3, 4, 5])
    data2 = np.array([6, 7, 8, 9, 10])

    print("\n4.1. Estadísticas Descriptivas Simples")
    estadisticas_descriptivas_simples(data)

    print("\n4.2. Enfoques Comunes para el Muestreo de Datos")
    enfoques_comunes_muestreo(data, 5)

    print("\n4.3. Estadísticas Inferenciales")
    estadisticas_inferenciales(data)

    print("\n4.4. Uso de Python para Calcular y Visualizar Estadísticas")
    calcular_visualizar_estadisticas(data)

    print("\n4.5. Estadística Inferencial Aplicada")
    estadistica_inferencial_aplicada(data1, data2)

if __name__ == "__main__":
    main()
