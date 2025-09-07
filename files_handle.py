def obtener_coeficiente(archivo, archivo_resultados):
    archivo_resultados = open(archivo_resultados, "r")
    for linea in archivo_resultados:
        linea = linea.split(",")
        if linea[0] == archivo:
            archivo_resultados.close()
            return int(linea[1][:-1])
    archivo_resultados.close()


def obtener_info_batallas (archivo):
    info = [] # (bi, ti)
    with open(archivo, "r") as archivo:
        lineas = archivo.readlines()
        lineas.pop(0)
        for linea in lineas:
            linea = linea.split(",")
            info.append((int(linea[1][:-1]), int(linea[0])))
    return info
            

