TEXTO_BATALLAS = "Batallas en orden"
TEXTO_COEFICIENTE = "Coeficiente obtenido"


def imprimir_batallas (batallas : list, coeficiente : int, archivo = None):
    if archivo is None:
        print()
        print(f'\033[92m{TEXTO_BATALLAS} (bi, ti) \033[0m')
        print(batallas)
        print()
        print(f'\033[92m{TEXTO_COEFICIENTE}\033[0m')
        print(coeficiente)
        print()
    else:
        with open(archivo, "w") as archivo:
            archivo.writelines([
                TEXTO_BATALLAS + "\n",
                f'{batallas}\n',
                TEXTO_COEFICIENTE + "\n",
                f'{coeficiente}\n',
            ])
