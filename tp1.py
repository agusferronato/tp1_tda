import sys
from files_handle import obtener_info_batallas


def calculo_coeficiente (info):
    suma = 0
    fi = 0

    for batalla in info:
        suma += batalla[0] * (batalla[1] + fi)
        fi += batalla[1]

    return suma


# Algoritmo
# info es una lista de tuplas de la forma (bi, ti)

def orden_batallas (info):
    info = sorted(info, key=lambda x: x[0] / x[1], reverse=True)

    return [], calculo_coeficiente(info)


if __name__ == "__main__":
    try:
        ruta = sys.argv[1]
        info = obtener_info_batallas(ruta)
        print(orden_batallas(info))
    except (FileNotFoundError):
        print("Error: no se ha encontrado el archivo")
    except (IndexError):
        print("Error: Debe pasar como primer parametro el nombre del archivo")
