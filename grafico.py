# Imports necesarios para el notebook
from random import seed
from tp1 import orden_batallas
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp
from util import time_algorithm


# Siempre seteamos la seed de aleatoridad para que los
# resultados sean reproducibles
seed(12345)
np.random.seed(12345)

sns.set_theme()


def get_random_array(size: int) -> list[tuple[int, int]]:
    return np.random.randint(10, 1000, size=(size, 2), dtype=np.int64)


if __name__ == '__main__':
    # La variable x van a ser los valores del
    # eje x de los gráficos en todo el notebook
    # Tamaño mínimo=1000, tamaño máximo=100000, cantidad de puntos=20
    x: np.ndarray = np.linspace(1000, 100000, 20).astype(int)

    results = time_algorithm(orden_batallas, x, lambda s: [get_random_array(s)])
    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, [results[i] for i in x], label="Medición")
    ax.set_title('Tiempo de ejecución del algoritmo')
    ax.set_xlabel('Tamaño del array')
    ax.set_ylabel('Tiempo de ejecución (s)')

    def n_logn(n, coeficiente_1, coeficiente_2):
        return coeficiente_1 * n * np.log(n) + coeficiente_2

    c, pcov = sp.optimize.curve_fit(n_logn, x, [results[n] for n in x])
    print(f"c_1 = {c[0]}, c_2 = {c[1]}")
    r = np.sum((c[0] * x * np.log(x) + c[1] - [results[n] for n in x])**2)
    print(f"Error cuadrático total: {r}")

    ax.plot(x, [c[0] * n * np.log(n) + c[1] for n in x], 'r--', label="Ajuste")
    ax.legend()
    fig
    plt.show()
