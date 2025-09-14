import numpy as np
from random import seed
import csv
import os 

CARPETA = "sets"


def generar_set_aleatorio (tamanio):

    archivo = f'{CARPETA}/{tamanio}.txt'

    x = np.random.randint(10, 1000, size=(tamanio, 2), dtype=np.int64)

    with open(archivo, mode='w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerows(x)

    
if __name__ == "__main__":
    generar_set_aleatorio(12000)