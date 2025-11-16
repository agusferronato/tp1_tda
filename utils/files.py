from pathlib import Path
import os
from utils.problem import NAME_POSITION
import sys


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(SCRIPT_DIR, "../files")
OUTPUT_FOLDER = os.path.join(SCRIPT_DIR, "../output")
os.makedirs(FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


EXPECTED_RESULTS_FILE = "Resultados Esperados.txt"
EXPECTED_RESULTS_PATH = os.path.join(FOLDER, EXPECTED_RESULTS_FILE)


def ls(ruta=Path.cwd()):
    return [arch.name for arch in Path(ruta).iterdir() if arch.is_file()]


def get_file_info(file):
    k = 0
    masters = []

    with open(file, "r+") as file:
        info = file.readlines()
        k = int(info[1])

        for i in range(2, len(info)):

            name, power = info[i].split(", ")
            masters.append((name, int(power)))

    return masters, k


def get_expected_results(path=EXPECTED_RESULTS_PATH):

    optimal_value = {}

    with open(path, "r+") as file:
        files_results = file.readlines()

        for i in range(1, len(files_results)):

            if files_results[i - 1] == "\n":

                file_name = files_results[i].strip("\n")
                optimal_value[file_name] = int(files_results[i + 1])

    return optimal_value



def print_result (result, size, k):

    with open(f"{OUTPUT_FOLDER}/{size}_{k}.txt", "w+") as file:

        best_sum, best_list = result

        file.write(f"Algoritmo de BT. Tamaño: {size}, k = {k}\n\n")
        file.write(f"Suma obtenida: {best_sum}\n\n")
        file.write(f"Asignación de maestros\n\n")

        for j in range(1, k + 1):
            file.write(f"Conjunto {j}. Cantidad de maestros asignados: {len(best_list[j - 1])}\n")
            for i in range(len(best_list[j - 1])):
                
                master = best_list[j - 1][i]
                file.write(master[NAME_POSITION])
                if i != len(best_list[j - 1]) - 1:
                    file.write(", ")

            file.write(f"\n\n")

        print(f"El resultado se encuentra en: output/{size}_{k}.txt")

