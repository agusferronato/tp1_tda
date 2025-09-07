import sys
from files_handle import obtener_info_batallas


# Algoritmo
# info es una lista de tuplas de la forma (bi, ti)

def orden_batallas (info):
    return [], 0


if __name__ == "__main__":
    try:
        ruta = sys.argv[1]
        info = obtener_info_batallas(ruta)
        print(orden_batallas(info))
    except (FileNotFoundError):
        print("Error: no se ha encontrado el archivo")
    except (IndexError):
        print("Error: Debe pasar como primer parametro el nombre del archivo")