import sys
import numpy as np
import os
from files_handle import obtener_info_batallas
from generar_sets_datos import generar_set_aleatorio

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from tp1 import calculo_coeficiente, orden_batallas


CANTIDAD_MUESTRAS = 15
TAMANIO = 10


def coeficiente_fb (batallas, indice, solucion_actual : list, mejor_solucion):

    ultimo = solucion_actual.index(None) if None in solucion_actual else len(batallas)

    c_solucion_actual = calculo_coeficiente(solucion_actual[:ultimo])

    if indice == len(batallas):
        if c_solucion_actual < mejor_solucion[1]:
            return [solucion_actual.copy(), c_solucion_actual]
        else:
            return mejor_solucion.copy()

    if c_solucion_actual > mejor_solucion[1]:
        return mejor_solucion.copy()    
        
    batalla = batallas[indice]

    for i in range(len(batallas)):
        if solucion_actual[i] is None:
            solucion_actual[i] = batalla
            mejor_solucion = coeficiente_fb(batallas, indice + 1, solucion_actual, mejor_solucion)
            solucion_actual[i] = None
        
    return mejor_solucion



# info = [(bi, ti)]

def coeficiente (info):
    return coeficiente_fb(info, 0, [None] * len(info), [info, calculo_coeficiente(info)])



if __name__ == "__main__":
    for i in range(CANTIDAD_MUESTRAS):
        generar_set_aleatorio(TAMANIO)
        batallas = obtener_info_batallas("./sets/10.txt")
        print(f'Coeficiente BT: {coeficiente(batallas)[1]}')
        print(f'Coeficiente greedy: {orden_batallas(batallas)[1]}')
        print()




