import sys


def polynomial_verifier(result: list[list[tuple[str, int]]], B: int) -> bool:
    total: int = 0
    for group in result:
        group_sum: int = sum(master[1] for master in group)
        total += group_sum ** 2
    return total <= B


def backtracking():
    return


def linear_programming():
    return


def greedy(x: list[tuple[str, int]], k: int) -> list[list[tuple[str, int]]]:
    result: list[list] = [[] for _ in range(k)]
    x.sort(key=lambda master: master[1], reverse=True)
    for master in x:
        min_index = min(range(k), key=lambda i: sum(x_i[1] for x_i in result[i]) ** 2)
        result[min_index].append(master)
    return result


def dinamic_programming():
    return


def algorithm(x: list[tuple[str, int]], k: int) -> list[list[tuple[str, int]]]:
    aproximation: list[list] = greedy(x, k)
    # llamar a BT con la aproximacion como mejor solucion actual


if __name__ == "__main__":
    try:
        path = sys.argv[1]
        x: list[tuple[str, int]] = []
        k: int = int(sys.argv[2])
        algorithm(x, k)
    except (FileNotFoundError):
        print("Error: no se ha encontrado el archivo")
    except (IndexError):
        print("Error: Debe pasar como primer parametro el nombre del archivo y el segundo cantidad de subgrupos")