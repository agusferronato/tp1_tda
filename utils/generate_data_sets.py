import sys
import os
import random
from tp3 import algorithm


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from tp3 import algorithm
from utils.files import get_file_info


MIN_POWER = 50
MAX_POWER = 1750

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(SCRIPT_DIR, "../sets")
PAKKU_DATA_SETS = os.path.join(SCRIPT_DIR, "../pakku_sets")
os.makedirs(FOLDER, exist_ok=True)
os.makedirs(PAKKU_DATA_SETS, exist_ok=True)


EXPECTED_RESULTS_PATH = os.path.join(FOLDER, "Resultados Esperados.txt")
EXPECTED_RESULTS_PAKKU_PATH = os.path.join(PAKKU_DATA_SETS, "Resultados Esperados.txt")


def write_pakku_strategy(file, k, size, masters=None):
    file.write(f"\n{k}\n")

    for i in range(2*k - 1, k, -1):     
        file.write(f', {i}\n')
        file.write(f', {i}\n')

    file.write(f', {k}\n')
    file.write(f', {k}\n')
    file.write(f', {k}\n')


def optimal_value_pakku_strategy(k, masters=None):
    return 9 * (k**3), []


def write_random_strategy(file, k, size, masters):
    file.write(f"\n{k}\n")
    for i in range(size):
        master_power = random.randint(MIN_POWER, MAX_POWER)
        masters.append(("", master_power))
        file.write(f", {master_power}\n")


def optimal_value_random_strategy(k, masters=None):
    return algorithm(masters, k)


def generate_data_sets(
    folder, results_path, write_strategy, optimal_strategy, k, masters=None, size=None
):

    with open(f"{folder}/{size}_{k}.txt", "w") as file:
        write_strategy(file, k, size, masters)

    if not os.path.exists(results_path):
        open(results_path, "w").close()

    with open(results_path, "r") as file:
        lines = file.readlines()
        file_found = False
        optimal_value, _ = optimal_strategy(k, masters)

        for i in range(len(lines)):
            if lines[i].startswith(f"{size}_{k}.txt"):
                lines[i + 1] = f"{optimal_value}\n"
                file_found = True
                break

        if not file_found:
            lines.append("\n")
            lines.append(f"{size}_{k}.txt\n")
            lines.append(f"{optimal_value}\n")

    with open(results_path, "w+") as file:
        file.writelines(lines)


def generate_worst_pakku(k):
    generate_data_sets(
        PAKKU_DATA_SETS,
        EXPECTED_RESULTS_PAKKU_PATH,
        write_pakku_strategy,
        optimal_value_pakku_strategy,
        k,
        None,
        2*k + 1
    )


def generate_random_data_sets(size, k):
    generate_data_sets(
        FOLDER,
        EXPECTED_RESULTS_PATH,
        write_random_strategy,
        optimal_value_random_strategy,
        k,
        [],
        size,
    )


def get_file_info_by_size(size):
    return get_file_info(f"{FOLDER}/{size}_{size // 2}.txt")
