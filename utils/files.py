from pathlib import Path

EXPECTED_RESULTS_FILE = "Resultados Esperados.txt"
FILES_PATH = "./files"


def get_file_info(file_name):
    xi = []
    f = []
    
    with open(f'{FILES_PATH}/{file_name}', "r+") as file:
        info = file.readlines()
        n = int(info[1])
        xi = [int(info[i].strip()) for i in range(2, n + 2)]
        f = [int(info[i].strip()) for i in range(n + 2, 2 * (n + 1))]
    
    return xi, f


def ls(ruta = Path.cwd()):
    return [arch.name for arch in Path(ruta).iterdir() if arch.is_file()]


def get_expected_results():
    sequence = {}
    eliminated_troops = {}

    with open(f'{FILES_PATH}/{EXPECTED_RESULTS_FILE}', "r+") as file:
        files_results = file.readlines()

        for i in range(0, len(files_results), 3):
            file_name = files_results[i].strip("\n")
            sequence[file_name] = (files_results[i + 1].strip("\n").replace(" ", "")).split(",")
            eliminated_troops[file_name] = int(files_results[i + 2])

    return sequence, eliminated_troops
