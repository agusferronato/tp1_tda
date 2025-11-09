from pathlib import Path


EXPECTED_RESULTS_FILE = "Resultados Esperados.txt"
FILES_PATH = "./files"


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


def get_expected_results():

    optimal_value = {}

    with open(f'{FILES_PATH}/{EXPECTED_RESULTS_FILE}', "r+") as file:
        files_results = file.readlines()

        for i in range(1, len(files_results)):

            if files_results[i - 1] == "\n":

                file_name = files_results[i].strip("\n")
                optimal_value[file_name] = int(files_results[i + 1])

    return optimal_value
