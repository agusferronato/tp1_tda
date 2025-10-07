from pathlib import Path

EXPECTED_RESULTS_FILE = "Resultados Esperados.txt"
FILES_PATH = "./files"
OUTPUT_PATH = "./output"

STRATEGIES_BY_LINE = 4


def get_file_info(file):
    xi = []
    f = []
    
    with open(file, "r+") as file:
        info = file.readlines()
        n = int(info[1])
        xi = [int(info[i].strip()) for i in range(2, n + 2)]
        f = [int(info[i].strip()) for i in range(n + 2, 2 * (n + 1))]
    
    return xi, f



def ls(ruta = Path.cwd()):
    return [arch.name for arch in Path(ruta).iterdir() if arch.is_file()]



def print_format(eliminated_troops, strategy):

    with open(f'{OUTPUT_PATH}/{len(strategy)}.txt', "w") as file:
        file.write("Eliminated troops:\n")
        file.write(str(eliminated_troops) + "\n")
        file.write("\n")

        file.write("Strategy:\n")
        counter = 0
        for i in range(0, len(strategy)):
            if counter == STRATEGIES_BY_LINE:
                file.write("\n")
                file.write(f"{strategy[i]}, ")
                counter = 1
            else:
                file.write(f"{strategy[i]}, ")
                counter += 1

        file.write("\n")






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
