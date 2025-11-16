from utils.files import get_expected_results, get_file_info, ls, FOLDER
import re
from tp3 import algorithm
# from algorithms.lineal_programming import linear_programming
import time


def tests():
    optimal_value = get_expected_results()

    for file_name in ls(FOLDER):

        if re.match(r"^\d", file_name):
            start = time.time()
            masters, k = get_file_info(f"{FOLDER}/{file_name}")

            best_sum, _ = algorithm(masters, k)

            if best_sum == optimal_value[file_name]:
                print(f"✅ Paso. Archivo {file_name}. Valor obtenido {best_sum}")
            else:
                print(
                    f"❌ No paso. Archivo {file_name}. Valor esperado: {optimal_value[file_name]}. Valor obtenido: {best_sum}"
                )
                print(
                    f"Coeficiente entre la solucion optima y la no exacta: {round(optimal_value[file_name] / best_sum, 2)}"
                )


if __name__ == "__main__":
    tests()
