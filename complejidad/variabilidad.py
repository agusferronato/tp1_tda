import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.generar_arreglos import obtener_arreglo
from complejidad.grafico import obtener_resultados
from matplotlib import pyplot as plt


TAMANIO = 1000

COLOR = ["red", "blue", "green", "black"]
MUESTRAS = 30

RANGES = (10, 1000), (100000, 10000000)


def nombres_rangos ():
    nombres = []
    for i in range(2):
        for j in range(2):
            nombres.append(f'({RANGES[i][0]}, {RANGES[i][1]}), ({RANGES[j][0]}, {RANGES[j][1]})')

    return nombres


def graficar(muestras):
    nombres = nombres_rangos()

    for resultados in muestras:
        for i in range(len(resultados)):
            plt.scatter(nombres[i], resultados[i], color=COLOR[i])
        
    plt.xlabel("Rangos b_i y t_i") 
    plt.ylabel("Tiempo (s)") 
    plt.show()



if __name__ == "__main__":
    muestras = []
    for k in range(MUESTRAS):
        resultados = []
        for i in range(0, 2):
            for j in range(0, 2):
                fn = obtener_arreglo(RANGES[i], RANGES[j])
                resultados.append(obtener_resultados([ TAMANIO ], fn))
        muestras.append([list(resultado.values())[0] for resultado in resultados])

    graficar(muestras)
