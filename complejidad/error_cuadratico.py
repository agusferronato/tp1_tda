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


# Siempre seteamos la seed de aleatoridad para que los
# resultados sean reproducibles
seed(12345)
np.random.seed(12345)

sns.set_theme()


def get_random_array(size: int):
    return np.random.randint(10, 1000, size=(size, 2), dtype=np.int64)


if __name__ == '__main__':
    # La variable x van a ser los valores del
    # eje x de los gráficos en todo el notebook
    # Tamaño mínimo=1000, tamaño máximo=100000, cantidad de puntos=20
    x: np.ndarray = np.linspace(1000, 100000, 20).astype(int)

    results = time_algorithm(orden_batallas, x, lambda s: [get_random_array(s)])
    ax: plt.Axes
    fig, ax = plt.subplots()


    c, pcov = sp.optimize.curve_fit(n_logn, x, [results[n] for n in x])

    errors = [np.abs(c[0] * n * np.log(n) + c[1] - results[n]) for n in x]


    ax.plot(x, errors)


    ax.set_title('Error de ajuste')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Error absoluto (s)')
    plt.show()

