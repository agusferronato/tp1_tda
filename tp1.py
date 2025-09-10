import sys
from files_handle import obtener_info_batallas
from format import imprimir_batallas


def calculo_coeficiente(batallas: list[tuple[int, int]]) -> int:
    suma_total: int = 0
    felicidad_i: int = 0

    for batalla in batallas:
        suma_total += batalla[0] * (batalla[1] + felicidad_i)
        felicidad_i += batalla[1]

    return suma_total


# info[i] == (bi, ti)

def orden_batallas(info: list[tuple[int, int]]):
    batallas: list = sorted(info, key=lambda x: x[0] / x[1], reverse=True)
    return batallas, calculo_coeficiente(batallas)


if __name__ == "__main__":
    try:
        ruta: str = sys.argv[1]
        info: list = obtener_info_batallas(ruta)
        batallas, coeficiente = orden_batallas(info)
        imprimir_batallas(batallas, coeficiente, file=None)
    except (FileNotFoundError):
        print("Error: no se ha encontrado el archivo")
    except (IndexError):
        print("Error: Debe pasar como primer parametro el nombre del archivo")
