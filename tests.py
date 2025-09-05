from files_handle import obtener_bi_ti, obtener_coeficiente
from tp1 import orden_batallas


RUTA = "./files"

# ARCHIVOS = ["10.txt", "50.txt"]

ARCHIVOS = ["10.txt", "50.txt", "100.txt", "1000.txt", "5000.txt", "10000.txt", "100000.txt"]
ARCHIVO_RESULTADOS = "Resultados Esperados.txt"


def test(archivo):
    bi, ti = obtener_bi_ti(f'{RUTA}/{archivo}')

    orden, coeficiente = orden_batallas(ti, bi)
    coeficiente_esperado = obtener_coeficiente(archivo,f'{RUTA}/{ARCHIVO_RESULTADOS}')

    if coeficiente == coeficiente_esperado:
        print(f'\033[92m✅ Test {archivo} paso\033[0m')
    else:
        print(f'\033[91m❌ Test {archivo} no paso\033[0m')
        print()
        print(f'Resultado esperado: {coeficiente_esperado}')
        print(f'Resultado obtenido: {coeficiente}')
    print()


if __name__ == "__main__":
    for archivo in ARCHIVOS:
        test(archivo)