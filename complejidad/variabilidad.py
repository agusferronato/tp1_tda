import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from complejidad.grafico import obtener_resultados
from tp1 import orden_batallas
from matplotlib import pyplot as plt


SIZE = 1000

NORMAL = 1
TIEMPO_LARGO = 2
PESO_GRANDE = 3
AMBOS_GRANDES = 4
PATRON = [NORMAL, TIEMPO_LARGO, PESO_GRANDE, AMBOS_GRANDES]
ETIQUETAS = ["Normal", "Tiempo largo", "Peso grande", "Ambos largo" ]

RANGES = (10, 1000), (100000, 10000000)


def get_array_with_fixed_value(range_t: tuple[int, int], range_b: tuple[int, int]):
    def fn (size: int):
        return np.column_stack((
            np.random.randint(range_b[0], range_b[1], size, dtype=np.int64),
            np.random.randint(range_t[0], range_t[1], size, dtype=np.int64)
        ))
    return fn


def graficar(resultados):
    plt.scatter(PATRON, resultados)
    for i in range(len(resultados)):
        plt.text(PATRON[i] + 0.1, resultados[i] + 0.1, ETIQUETAS[i], fontsize=12)
    
    plt.ylabel("Tiempo (s)") 
    plt.show()





if __name__ == "__main__":
    resultados = []
    
    for i in range(0, 2):
        for j in range(0, 2):
            fn = get_array_with_fixed_value(RANGES[i], RANGES[j])
            resultados.append(obtener_resultados([ SIZE ], fn))

    graficar([list(resultado.values())[0] for resultado in resultados])
