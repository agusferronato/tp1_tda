from files import get_expected_results, get_file_info, ls, FILES_PATH
import re
from utils.problem import score
from tp3 import algorithm
from lineal_programming import linear_programming
import time


def tests():
    optimal_value = get_expected_results()

    for file_name in ls(FILES_PATH):

        if re.match(r"^\d", file_name) and file_name == "18_6.txt":
            start = time.time()
            masters, k = get_file_info(f"{FILES_PATH}/{file_name}")

            best_sum = linear_programming(masters, k)
            # best_sum = score(best, k)

            if best_sum == optimal_value[file_name]:
                print(f"👌 Paso. Archivo {file_name}. Valor obtenido {best_sum}")
            else:
                print(
                    f"⚠️ No paso. Archivo {file_name}. Valor esperado: {optimal_value[file_name]}. Valor obtenido: {best_sum}"
                )
                print(
                    f"Coeficiente entre la solucion optima y la no exacta: {round(optimal_value[file_name] / best_sum, 2)}"
                )

            print(
                f"time: {round(time.time() - start, 2)}s, {round((time.time() - start) / 60, 2)}m"
            )


if __name__ == "__main__":
    tests()
