import sys
import csv


def parser(ruta: str) -> list[tuple[int, int]]:
    datos: list = []
    with open(ruta, "r") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltear el encabezado
        for fila in lector:
            datos.append((int(fila[0]), int(fila[1])))
    return datos


if __name__ == "__main__":
    datos: list = parser(sys.argv[1])
    if not datos:
        print("No se encontraron los datos.")
