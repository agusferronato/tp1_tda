def obtener_coeficiente(archivo, archivo_resultados):
    archivo_resultados = open(archivo_resultados, "r")
    for linea in archivo_resultados:
        linea = linea.split(",")
        if linea[0] == archivo:
            archivo_resultados.close()
            return int(linea[1][:-1])
    archivo_resultados.close()


def obtener_bi_ti (archivo, ruta = ""):
    bi = []
    ti = []
    with open(archivo, "r") as archivo:
        lineas = archivo.readlines()
        lineas.pop(0)
        for linea in lineas:
            linea = linea.split(",")
            ti.append(int(linea[0]))
            bi.append(int(linea[1][:-1]))
    return bi, ti
            

