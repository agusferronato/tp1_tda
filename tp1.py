import sys
from files_handle import obtener_bi_ti

# Algoritmo

def orden_batallas (ti, bi):
    return [], 0


if __name__ == "__main__":
    ruta = sys.argv[1]
    bi, ti = obtener_bi_ti(ruta)
    print(orden_batallas(ti, bi))