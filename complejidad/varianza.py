import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from utils.generar_sets_datos import get_random_array
from complejidad.grafico import graficar
from tp1 import orden_batallas

MUESTRAS: int = 5
ESCALAR: int = 10e10
SIZE: int = 1000


def contrucion_del_set(escalar_t, escalar_b):
    t = [t_i * escalar_t for t_i in get_random_array(SIZE)]
    b = [t_i * escalar_t for t_i in get_random_array(SIZE)]
    return np.column_stack((t, b))


def ambos_normales():
    return contrucion_del_set(1, 1)


def t_grande():
    return contrucion_del_set(ESCALAR, 1)


def b_grande():
    return contrucion_del_set(1, ESCALAR)


def ambos_grande():
    return contrucion_del_set(ESCALAR, ESCALAR)


plt.title("Comparacion de tiempos de ejecucion segun los numeros")
plt.xlabel("")
plt.ylabel("tiempo de ejecucion (s)")
plt.legend()
plt.grid(true)
plt.tight_layout()
plt.show()