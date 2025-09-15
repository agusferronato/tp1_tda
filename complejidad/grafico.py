import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from random import seed
from tp1 import orden_batallas
from matplotlib import pyplot as plt
from complejidad.math import n_logn
import seaborn as sns
import numpy as np
import scipy as sp
from complejidad.util import time_algorithm
from utils.generar_sets_datos import get_random_array, get_array_with_fixed_value


seed(12345)
np.random.seed(12345)

sns.set_theme()



def obtener_resultados(sizes, get_array_function):
    return time_algorithm(orden_batallas, sizes, lambda s: [get_array_function(s)])


def graficar (x, results, error = False):

    ax: plt.Axes
    fig, ax = plt.subplots()

    c, pcov = sp.optimize.curve_fit(n_logn, x, [results[n] for n in x])

    if error:
        errors = [np.abs(c[0] * n * np.log(n) + c[1] - results[n]) for n in x]

        ax.plot(x, errors)

        ax.set_title('Error de ajuste')
        ax.set_xlabel('Tamaño del array')
        ax.set_ylabel('Error absoluto (s)')

    else:

        ax.scatter(x, [results[i] for i in x], label="Medición")
        ax.set_title('Tiempo de ejecución del algoritmo')
        ax.set_xlabel('Tamaño del array')
        ax.set_ylabel('Tiempo de ejecución (s)')


        ax.plot(x, [c[0] * n * np.log(n) + c[1] for n in x], 'r--', label="Ajuste")
        ax.legend()
        fig


    r = np.sum((c[0] * x * np.log(x) + c[1] - [results[n] for n in x])**2)

    print(f"c_1 = {c[0]}, c_2 = {c[1]}")
    print(f"Error cuadrático total: {r}")
    

    plt.show()




if __name__ == '__main__':

    sizes: np.ndarray = np.linspace(1000, 100000, 20).astype(int)
    results = obtener_resultados(sizes, get_array_with_fixed_value)

    graficar(sizes, results)
    graficar(sizes, results, error=True)


