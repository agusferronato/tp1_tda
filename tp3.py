import sys
from backtracking import bt, VALUE_POSITION
from greedy import pakku, approximate, Master
import time


def algorithm(masters: list[Master], k: int) -> tuple[int, list[list[Master]]]:

    inicio = time.time()

    masters = sorted(masters, key=lambda master: master[VALUE_POSITION], reverse=True)

    approximation: list[list[Master]] = approximate(masters, k)

    best_sum: int = 0
    for group in approximation:
        best_sum += sum(master[VALUE_POSITION] for master in group) ** 2

    approximation = (best_sum, approximation)

    sum_of_each_set: list[int] = [0] * k
    current_list: list[list] = [[] for _ in range(k)]
    current_sum: int = 0
    remains: int = sum(master[VALUE_POSITION] for master in masters)

    current = (sum_of_each_set, current_list, current_sum, remains)
    res = bt(masters, k, 0, current, approximation)
    fin = time.time()
    print("tiempo: " + str(round(fin - inicio, 2)) + "s")
    return res


if __name__ == "__main__":
    try:
        path = sys.argv[1]
        algorithm([], int(sys.argv[2]))
    except (FileNotFoundError):
        print("Error: no se ha encontrado el archivo")
    except (IndexError):
        print("Error: Debe pasar como primer parametro el nombre del archivo y el segundo cantidad de subgrupos")
