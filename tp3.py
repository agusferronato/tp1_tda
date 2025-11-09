import sys
from backtracking import bt, VALUE_POSITION
from pakku import pakku, SUM_POSITION, SET_POSITION
import time


def algorithm(masters, k):

    inicio = time.time()

    approximation = pakku(masters, k)

    best_sum = 0
    best_list = []
    for group in approximation:
        best_sum += group[SUM_POSITION] ** 2
        best_list.append(group[SET_POSITION])

    sum_of_each_set = [0] * k
    current_list = [[] for _ in range(k)]
    current_sum = 0 

    print(best_list)

    res =  bt(masters, k, 0, current=[sum_of_each_set, current_list, current_sum], best=(best_sum, best_list))
    fin = time.time()
    print("tiempo: " + str(fin - inicio))
    return res 






if __name__ == "__main__":
    try:
        path = sys.argv[1]
        algorithm([], int(sys.argv[2]))
    except (FileNotFoundError):
        print("Error: no se ha encontrado el archivo")
    except (IndexError):
        print("Error: Debe pasar como primer parametro el nombre del archivo y el segundo cantidad de subgrupos")