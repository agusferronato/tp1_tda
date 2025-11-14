import sys
import os
import time
import random
# esto es feo deberia no estar
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tp3 import algorithm as bt
from algorithms.greedy import pakku, approximate
from algorithms.lineal_programming import approximate_linear_programming as alp, linear_programming as lp
from tabulate import tabulate
from utils.generate_data_sets import generate_data_setsS, generate_data_sets_worst_pakku
from utils.files import get_file_info, get_expected_results


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(SCRIPT_DIR, "../sets")
os.makedirs(FOLDER, exist_ok=True)

EXPECTED_RESULTS_FILE = "Resultados Esperados.txt"
EXPECTED_RESULTS_PATH = os.path.join(FOLDER, EXPECTED_RESULTS_FILE)


def compare_algorithms():

    results = {}
    name = {
        alp: "Approximate Lineal Programming",
        lp: "Lineal Programming",
        bt: "Backtracking",
        pakku: "Pakku",
    }

    for algorithm in [alp, lp, bt, pakku]:
        results[algorithm] = {}

    for size in range(5, 14):

        for k in range(2, size - 1):
            generate_data_setsS(size, k)

    optimal_value = get_expected_results(EXPECTED_RESULTS_PATH)

    for size in range(5, 14):

        for k in range(2, size - 1):

            file = f"{size}_{k}.txt"
            masters, _ = get_file_info(f"{FOLDER}/{file}")

            for algorithm in [alp, lp, bt, pakku]:

                print(f"a: {name[algorithm]}, size: {size}, k: {k}")

                if size not in results[algorithm]:
                    results[algorithm][size] = {}

                results[algorithm][size][k] = []

                start = time.time()

                value = algorithm(masters, k)
                if isinstance(value, tuple):
                    value = value[0]

                results[algorithm][size][k].append([value, round(time.time() - start, 2), value / optimal_value[file]])

    values_data = {}
    times_data = {}
    ratio_data = {}

    for algorithm, sizes in results.items():
        for size, ks in sizes.items():        
            for k, records in ks.items():     

                key = f"n={size}, k={k}"

                if key not in values_data:
                    values_data[key] = []
                if key not in times_data:
                    times_data[key] = []
                if key not in ratio_data:
                    ratio_data[key] = []

                for record in records:                    
                    value, total_time, ratio = record
                    values_data[key].append(value)
                    times_data[key].append(total_time)
                    ratio_data[key].append(ratio)


    headers = [name[algorithm] for algorithm in [alp, lp, bt, pakku]]

    values_data = [[k, *v] for k, v in values_data.items()]
    times_data = [[k, *v] for k, v in times_data.items()]
    ratio_data = [[k, *v] for k, v in ratio_data.items()]


    print(tabulate(values_data, headers=headers, tablefmt="grid"))
    print(tabulate(times_data, headers=headers, tablefmt="grid"))
    print(tabulate(ratio_data, headers=headers, tablefmt="grid"))


def compare_pakku_vs_approximate():

    # usamos una lista de tuplas (filas) para imprimir con tabulate
    results = []
    ks = [2 * x for x in range(1, 10)]

    for k in ks:
        # generar el set worst-case para este k
        generate_data_sets_worst_pakku(k)

        file = f"worst_pakku_{k}.txt"
        path = os.path.join(FOLDER, file)

        # leer masters desde el archivo generado
        masters, k_from_file = get_file_info(path)
        size = len(masters)

        # Pakku (raw)
        start = time.time()
        pakku_res = pakku(masters, k)
        pakku_time = round(time.time() - start, 3)
        if isinstance(pakku_res, tuple):
            pakku_raw = pakku_res[0]
        else:
            pakku_raw = pakku_res if isinstance(pakku_res, (int, float)) else 0

        # Approximate (raw)
        start = time.time()
        approx_res = approximate(masters, k)
        approx_time = round(time.time() - start, 3)
        if isinstance(approx_res, tuple):
            approx_raw = approx_res[0]
        else:
            approx_raw = approx_res if isinstance(approx_res, (int, float)) else 0

        # normalizar valores por (9 * k**3)
        denom = 9 * (k ** 3) if k > 0 else 1
        pakku_norm = round(pakku_raw / denom, 6) if denom != 0 else None
        approx_norm = round(approx_raw / denom, 6) if denom != 0 else None

        # delta = (pakku_raw - approx_raw) / pakku_raw (si pakku_raw == 0 -> None)
        delta = None
        try:
            delta = round((pakku_raw - approx_raw) / pakku_raw, 6) if pakku_raw != 0 else None
        except Exception:
            delta = None

        results.append((size, k, pakku_norm, approx_norm, delta, pakku_time, approx_time))

    headers = ["Size", "k", "Pakku", "Approx", "Delta", "Time Pakku (s)", "Time Approx (s)"]
    print(tabulate(results, headers=headers, tablefmt="grid"))


if __name__ == "__main__":
    compare_pakku_vs_approximate()
