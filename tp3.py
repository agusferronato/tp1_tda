import sys
from utils.problem import VALUE_POSITION
from utils.files import get_file_info, print_result
from algorithms.backtracking import bt
from algorithms.greedy import pakku


def algorithm(masters, k: int):

    masters = sorted(masters, key=lambda master: master[VALUE_POSITION], reverse=True)

    approximation = pakku(masters, k)

    sum_of_each_set: list[int] = [0] * k
    current_list: list[list] = [[] for _ in range(k)]
    current_sum: int = 0
    remains: int = sum(master[VALUE_POSITION] for master in masters)

    current = (sum_of_each_set, current_list, current_sum, remains)
    res = bt(masters, k, 0, current, approximation)
    return res


if __name__ == "__main__":
    try:
        path = sys.argv[1]

        masters, k = get_file_info(path)

        print_result(algorithm(masters, k), len(masters), k)

    except FileNotFoundError:
        print("Error: no se ha encontrado el archivo")
    except IndexError:
        print(
            "Error: Debe pasar como primer parametro el nombre del archivo"
        )
