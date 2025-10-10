import sys
from utils.files import get_file_info, print_format


def reconstruction(xi: list[int], f: list[int], OPT: list[int]) -> list[str]:
    index: int = len(xi)
    solution: list[str] = []

    while index > 0:
        for j in range(1, index + 1):
            if OPT[index] == OPT[index - j] + min(f[j - 1], xi[index - 1]):
                solution.append("Atacar")
                solution.extend(["Cargar"] * (j - 1))
                index -= j
                break

    solution.reverse()
    return solution


def algorithm(xi: list[int], f: list[int]) -> tuple[int, list[str]]:

    n: int = len(xi)
    OPT: list[int] = [0] * (n + 1)

    for i in range(1, n + 1):
        max_value: int = -1
        for j in range(1, i + 1):
            current_value = OPT[i - j] + min(f[j - 1], xi[i - 1])
            if max_value < current_value:
                max_value = current_value
        OPT[i] = max_value

    return OPT[n], reconstruction(xi, f, OPT)


if __name__ == "__main__":
    try:
        path = sys.argv[1]
        xi, f = get_file_info(path)
        eliminated_troops, strategy = algorithm(xi, f)
        print_format(eliminated_troops, strategy)

    except (FileNotFoundError):
        print("Error: no se ha encontrado el archivo")
    except (IndexError):
        print("Error: Debe pasar como primer parametro el nombre del archivo")
