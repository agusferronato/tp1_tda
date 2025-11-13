from pathlib import Path
import os
import sys 


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(SCRIPT_DIR, "../files")
os.makedirs(FOLDER, exist_ok=True)


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
