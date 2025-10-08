import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from random import seed
from tp2 import algorithm
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp
from complexity.utils_complexity import time_algorithm
from utils.data_sets import generate_data_set
from utils.files import get_file_info_by_size


SAMPLES = 25
N_MIN = 1000
N_MAX = 12500


def square(n, c1, c2):
    return c1 * n * n + c2


def get_results(sizes, fn):
    return time_algorithm(algorithm, sizes, lambda s: fn(s))


def quadratic_error(results, c, x):
    return np.sum((c[0] * x * x + c[1] - [results[n] for n in x])**2)


def graph(x, results, error=False):

    ax: plt.Axes
    fig, ax = plt.subplots()

    c, pcov = sp.optimize.curve_fit(square, x, [results[n] for n in x])

    if error:
        errors = [np.abs(c[0] * n * n + c[1] - results[n]) for n in x]

        ax.plot(x, errors)

        ax.set_title('Error de ajuste')
        ax.set_xlabel('Tamaño del array')
        ax.set_ylabel('Error absoluto (s)')

    else:

        ax.scatter(x, [results[i] for i in x], label="Medición")
        ax.set_title('Tiempo de ejecución del algoritmo')
        ax.set_xlabel('Tamaño del array')
        ax.set_ylabel('Tiempo de ejecución (s)')

        ax.plot(x, [c[0] * n * n + c[1] for n in x], 'r--', label="Ajuste")
        ax.legend()
        fig


    r = quadratic_error(results, c, x)

    print(f"c_1 = {c[0]}, c_2 = {c[1]}")
    print(f"Error cuadrático total: {r}")

    plt.show()



def graph_time(sizes, fn):

    results = get_results(sizes, fn)
    graph(sizes, results)  
    graph(sizes, results, error=True)  



if __name__ == '__main__':

    sns.set_theme()

    sizes: np.ndarray = np.linspace(N_MIN, N_MAX, SAMPLES).astype(int)

    for size in sizes:
        generate_data_set(size)

    graph_time(sizes, get_file_info_by_size)