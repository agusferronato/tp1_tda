from utils.archivos import obtener_info_batallas, obtener_coeficiente
from utils.verificar_resultado_bt import coeficiente
from tp1 import orden_batallas
import sys
import random

RUTA_CATEDRA = "./files"

OPCION_CATEDRA = "-c"

ARCHIVOS_CATEDRA = ["10.txt", "50.txt", "100.txt", "1000.txt", "5000.txt", "10000.txt", "100000.txt"]
ARCHIVO_RESULTADOS = "Resultados Esperados.txt"

# Pruebas aleatorias

OPCION_ALEATORIA = "-a"
CANTIDAD_MUESTRAS = 10
TAMANIO = 10


MIN_VALUE = 10
MAX_VALUE = 1000


def arreglo_aleatorio (size: int):
    return [(random.randint(MIN_VALUE, MAX_VALUE), random.randint(MIN_VALUE, MAX_VALUE)) for _ in range(size)]


def comparar_coeficientes(esperado, obtenido, nombre_archivo = ""):
    
    if esperado == obtenido:
        print(f'\033[92m✅ Test {nombre_archivo} paso\033[0m')
    else:
        print(f'\033[91m❌ Test {nombre_archivo} no paso\033[0m')
        print(f'Resultado esperado: {nombre_archivo}')
        print(f'Resultado obtenido: {nombre_archivo}')



def test_catedra(archivo):
    info = obtener_info_batallas(f'{RUTA_CATEDRA}/{archivo}')

    _, coeficiente = orden_batallas(info)
    coeficiente_esperado = obtener_coeficiente(archivo,f'{RUTA_CATEDRA}/{ARCHIVO_RESULTADOS}')

    comparar_coeficientes(coeficiente_esperado, coeficiente, archivo)


def test_bt (info):
    print()
    print(f'Batallas: {info}')

    orden_greedy, coeficiente_greedy = orden_batallas(info)
    orden_bt, coeficiente_bt = coeficiente(info)

    print(f'Resultado greedy: {orden_greedy}')
    print(f'Resultado BT: {orden_bt}')

    comparar_coeficientes(coeficiente_greedy, coeficiente_bt)



if __name__ == "__main__":
    try:
        opcion: str = sys.argv[1]
        
    except (IndexError):
        opcion = None

    # Prueba con los archivos de la catedra
    if opcion == OPCION_CATEDRA or opcion is None:
        for archivo in ARCHIVOS_CATEDRA:
            test_catedra(archivo)

    # Prueba aleatoria
    elif opcion == OPCION_ALEATORIA:
        for i in range(CANTIDAD_MUESTRAS):
            test_bt(arreglo_aleatorio(TAMANIO))

            
        




    