import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tp1 import calculo_coeficiente


def coeficiente_bt (batallas, indice, solucion_actual : list, mejor_solucion):

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
            mejor_solucion = coeficiente_bt(batallas, indice + 1, solucion_actual, mejor_solucion)
            solucion_actual[i] = None
        
    return mejor_solucion


def coeficiente (info):
    return coeficiente_bt(info, 0, [None] * len(info), [info, calculo_coeficiente(info)])





