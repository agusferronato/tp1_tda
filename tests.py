from files_handle import obtener_info_batallas, obtener_coeficiente
from tp1 import orden_batallas


RUTA = "./files"

# ARCHIVOS = ["10.txt", "50.txt"]

ARCHIVOS = ["10.txt", "50.txt", "100.txt", "1000.txt", "5000.txt", "10000.txt", "100000.txt"]
ARCHIVO_RESULTADOS = "Resultados Esperados.txt"


def test(archivo):
    info = obtener_info_batallas(f'{RUTA}/{archivo}')

    orden, coeficiente = orden_batallas(info)
    coeficiente_esperado = obtener_coeficiente(archivo,f'{RUTA}/{ARCHIVO_RESULTADOS}')


    if coeficiente == coeficiente_esperado:
        print(f'\033[92m✅ Test {archivo} paso\033[0m')
    else:
        print(f'\033[91m❌ Test {archivo} no paso\033[0m')
        print(f'Resultado esperado: {coeficiente_esperado}')
        print(f'Resultado obtenido: {coeficiente}')


if __name__ == "__main__":
    for archivo in ARCHIVOS:
        test(archivo)