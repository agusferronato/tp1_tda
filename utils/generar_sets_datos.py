import numpy as np
from random import seed
import csv
import random
import os
from utils.files_handle import obtener_info_batallas

CARPETA = "sets"


MIN_VALUE = 10
MAX_VALUE = 1000


def get_random_array(size: int):
    return np.random.randint(MIN_VALUE, MAX_VALUE, size=(size, 2), dtype=np.int64)


def get_array_with_fixed_value(size: int):
    return np.column_stack((
        np.random.randint(10, 1000, size=size, dtype=np.int64),
        np.full(size, 10000, dtype=np.int64)
    ))


def generar_set_aleatorio (tamanio):

    nombre_archivo = f'{CARPETA}/{tamanio}.txt'

    x = get_random_array(tamanio)

    with open(nombre_archivo, mode='w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerows(x)

    return nombre_archivo
