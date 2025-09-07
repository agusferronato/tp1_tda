import sys
from files_handle import obtener_bi_ti

# Algoritmo

def orden_batallas (ti, bi):
    return [], 0


if __name__ == "__main__":
    try:
        ruta = sys.argv[1]
        bi, ti = obtener_bi_ti(ruta)
        print(orden_batallas(ti, bi))
    except (FileNotFoundError):
        print("Error: no se ha encontrado el archivo")
    except (IndexError):
        print("Error: Debe pasar como primer parametro el nombre del archivo")