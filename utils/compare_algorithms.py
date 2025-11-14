import sys
import os
import time

from tp3 import algorithm as bt
from algorithms.greedy import pakku, approximate
from algorithms.lineal_programming import approximate_linear_programming as alp, linear_programming as lp
from tabulate import tabulate
from utils.generate_data_sets import generate_data_setsS, generate_data_sets_worst_pakku
from utils.files import get_file_info, get_expected_results

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


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


if __name__ == "__main__":
    compare_algorithms()
