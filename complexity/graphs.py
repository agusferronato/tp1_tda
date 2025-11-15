import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from random import seed
from tp3 import algorithm
from matplotlib import pyplot as plt 
import seaborn as sns
import numpy as np
import scipy as sp
from complexity.utils_complexity import time_algorithm
from utils.generate_data_sets import get_file_info_by_size, generate_random_data_sets

SAMPLES = 15
N_MIN = 15
N_MAX = 30

def exponential(n, c1, c2):
    return c1 * pow(c2, n)


def n_three_means(n, c1, c2):
    return c1 * pow(n, 1.5) + c2


def square(n, c1, c2):
    return c1 * n ** 2 + c2


def cubed(n, c1, c2):
    return c1 * n ** 3 + c2


def nlogn(n, c1, c2):
    return c1 * n * np.log(n) + c2


def linear(n, c1, c2):
    return c1 * n + c2



def get_results(sizes, fn):
    return time_algorithm(algorithm, sizes, lambda s: fn(s))


def quadratic_error(results, c, x, function):
    return np.sum((function(x, c[0], c[1]) - [results[n] for n in x])**2)



def graph_time(x, function, results, function_name):

    ax: plt.Axes
    fig, ax = plt.subplots()

    #c, pcov = sp.optimize.curve_fit(function, x, [results[n] for n in x])

    
    ax.scatter(x, [results[i] for i in x], label="Medición")
    ax.set_title('Tiempo de ejecución del algoritmo')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Tiempo de ejecución (s)')

    # ax.plot(x, [function(n, c[0], c[1]) for n in x], 'r--', label=f"Ajuste {function_name}")
    ax.legend()
    fig


    #r = quadratic_error(results, c, x, function)

    #print(f"c_1 = {c[0]}, c_2 = {c[1]}")

    plt.show()




def graph_error(x, functions, results):

    ax: plt.Axes
    fig, ax = plt.subplots()
    

    for function_name, function in functions.items():

        c, _ = sp.optimize.curve_fit(function, x, [results[n] for n in x])

        errors_function = [np.abs(function(n, c[0], c[1]) - results[n]) for n in x]

        ax.plot(x, errors_function, label=f"Ajuste ${function_name}$")

        print(f"Error cuadrático total para {function_name}: {np.sum(np.power(errors_function, 2))}")

    ax.set_title('Error de ajuste')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Error absoluto (s)')
    ax.legend()

    plt.show()



if __name__ == '__main__':

    # functions = {
    #     "n^2": square,
    #     "n^3": cubed,
    #     "nlogn": nlogn
    # }

    functions = {
        "2^n": exponential,
    }

    sns.set_theme()

    sizes: np.ndarray = np.linspace(N_MIN, N_MAX, SAMPLES).astype(int)

    for size in sizes:
        generate_random_data_sets(size, size // 2, False)

    fn = get_file_info_by_size

    results = get_results(sizes, fn)

    for function_name, function in functions.items():
        graph_time(sizes, function, results, function_name)

    # graph_error(sizes, functions, results)