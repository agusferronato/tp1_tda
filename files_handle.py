import csv


def obtener_coeficiente(archivo, archivo_resultados):
    archivo_resultados = open(archivo_resultados, "r")
    for linea in archivo_resultados:
        linea = linea.split(",")
        if linea[0] == archivo:
            archivo_resultados.close()
            return int(linea[1][:-1])
    archivo_resultados.close()


def obtener_info_batallas(archivo: str) -> list[tuple[int, int]]:
    info: list = []
    with open(archivo, "r") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltear encabezado
        for linea in lector:
            info.append((int(linea[0]), int(linea[1])))
    return info
