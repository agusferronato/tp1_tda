from files import get_expected_results, get_file_info, ls, FILES_PATH
import re
from utils.problem import score
from algorithms.greedy import pakku


def tests():
    optimal_value = get_expected_results()

    for file_name in ls(FILES_PATH):

        if re.match(r"^\d", file_name):
            masters, k = get_file_info(f"{FILES_PATH}/{file_name}")
            corte = 1 + (1/(9*k)) - 1/(9*(k**2))

            best = pakku(masters, k)
            best_sum = score(best, k)

            if best_sum/optimal_value[file_name] <= corte:
                print(f"👌 Paso. Archivo {file_name}. ")
            else:
                print(
                    f"⚠️ No paso. Archivo {file_name}. Valor esperado: {corte}. Valor obtenido: {best_sum}"
                )


if __name__ == "__main__":
    tests()
