import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from random import seed
from tp1 import orden_batallas
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp
from complejidad.util import time_algorithm
from utils.generar_arreglos import obtener_arreglo


CANTIDAD_MUESTRAS = 35
N_MIN = 1000
N_MAX = 100000
EJECUCIONES_ERROR = 25



def n_logn(n, coeficiente_1, coeficiente_2):
    return coeficiente_1 * n * np.log(n) + coeficiente_2


def obtener_resultados(tamanios, fn):
    return time_algorithm(orden_batallas, tamanios, lambda s: [fn(s)])


def error_cuadratico_total(resultados, c, x):
    return np.sum((c[0] * x * np.log(x) + c[1] - [resultados[n] for n in x])**2)



def graficar(x, resultados, error=False):

    ax: plt.Axes
    fig, ax = plt.subplots()

    c, pcov = sp.optimize.curve_fit(n_logn, x, [resultados[n] for n in x])

    if error:
        errors = [np.abs(c[0] * n * np.log(n) + c[1] - resultados[n]) for n in x]

        ax.plot(x, errors)

        ax.set_title('Error de ajuste')
        ax.set_xlabel('Tamaño del array')
        ax.set_ylabel('Error absoluto (s)')

    else:

        ax.scatter(x, [resultados[i] for i in x], label="Medición")
        ax.set_title('Tiempo de ejecución del algoritmo')
        ax.set_xlabel('Tamaño del array')
        ax.set_ylabel('Tiempo de ejecución (s)')

        ax.plot(x, [c[0] * n * np.log(n) + c[1] for n in x], 'r--', label="Ajuste")
        ax.legend()
        fig


    r = error_cuadratico_total(resultados, c, x)

    print(f"c_1 = {c[0]}, c_2 = {c[1]}")
    print(f"Error cuadrático total: {r}")

    plt.show()


def graficar_tiempo_y_error(sizes, fn):

    resultados = obtener_resultados(sizes, fn)
    graficar(sizes, resultados)  # Grafico tiempo de ejecucion
    graficar(sizes, resultados, error=True)  # Grafico error


def error_cuadratico_para_varias_muestras(sizes, fn):
    max = None

    for i in range(EJECUCIONES_ERROR):

        resultados = obtener_resultados(sizes, fn)
        c, pcov = sp.optimize.curve_fit(n_logn, sizes, [resultados[n] for n in sizes])
        error = error_cuadratico_total(resultados, c, sizes)
        print(f'Error ejecucion {i + 1}: {error}')
        if max is None or error > max:
            max = error

    print(f'Error cuadratico maximo: {max}')





if __name__ == '__main__':
    
    sns.set_theme()

    tamanios: np.ndarray = np.linspace(N_MIN, N_MAX, CANTIDAD_MUESTRAS).astype(int)

    fn = obtener_arreglo((10, 1000), (10, 1000))
    graficar_tiempo_y_error(tamanios, fn)
