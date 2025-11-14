import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from tp3 import algorithm


MIN_POWER = 50
MAX_POWER = 1750

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(SCRIPT_DIR, "../sets")
os.makedirs(FOLDER, exist_ok=True)

EXPECTED_RESULTS_FILE = "Resultados Esperados.txt"
EXPECTED_RESULTS_PATH = os.path.join(FOLDER, EXPECTED_RESULTS_FILE)


def generate_data_setsS(size, k):

    masters = []
    lines = []

    with open(f"{FOLDER}/{size}_{k}.txt", "w") as file:
        file.write(f"\n{k}\n")
        for i in range(size):
            master_power = random.randint(MIN_POWER, MAX_POWER)
            masters.append(("", master_power))
            file.write(f", {master_power}\n")

    if not os.path.exists(EXPECTED_RESULTS_PATH):
        open(EXPECTED_RESULTS_PATH, "w").close()

    with open(EXPECTED_RESULTS_PATH, "r") as file:
        lines = file.readlines()
        file_found = False
        optimal_value, _ = algorithm(masters, k)

        for i in range(len(lines)):
            if lines[i].startswith(f"{size}_{k}.txt"):
                lines[i + 1] = f"{optimal_value}\n"
                file_found = True
                break

        if not file_found:
            lines.append("\n")
            lines.append(f"{size}_{k}.txt\n")
            lines.append(f"{optimal_value}\n")


    with open(EXPECTED_RESULTS_PATH, "w+") as file:
        file.writelines(lines)


def generate_data_sets_worst_pakku(k: int):
    with open(f"{FOLDER}/worst_pakku_{k}.txt", "w") as file:
        file.write(f"\n{k}\n")
        for i in range(1, k + 1):
            file.write(f", {2 * k - i}\n")
            file.write(f", {2 * k - i}\n")
        file.write(f", {k}\n")

    expected_result: int = 9 * (k ** 3)
    with open(EXPECTED_RESULTS_PATH, "a") as file:
        file.write("\n")
        file.write(f"worst_pakku_{k}.txt\n")
        file.write(f"{expected_result}\n")
