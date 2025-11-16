import sys
import os
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tp3 import algorithm
from algorithms.greedy import pakku
from utils.files import get_file_info
from utils.problem import NAME_POSITION, VALUE_POSITION


MIN_POWER = 50
MAX_POWER = 1750

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FOLDER = os.path.join(SCRIPT_DIR, "../sets")
PAKKU_DATA_SETS = os.path.join(SCRIPT_DIR, "../pakku_sets")
os.makedirs(FOLDER, exist_ok=True)
os.makedirs(PAKKU_DATA_SETS, exist_ok=True)


EXPECTED_RESULTS_PATH = os.path.join(FOLDER, "Resultados Esperados.txt")
EXPECTED_RESULTS_PAKKU_PATH = os.path.join(PAKKU_DATA_SETS, "Resultados Esperados.txt")


MIN_SIZE = 5
MAX_SIZE = 20


# PAKKU

def write_pakku_strategy(file, k, size, masters=None):
    file.write(f"\n{k}\n")

    for i in range(2*k - 1, k, -1):     
        file.write(f', {i}\n')
        file.write(f', {i}\n')

    file.write(f', {k}\n')
    file.write(f', {k}\n')
    file.write(f', {k}\n')


def optimal_value_pakku_strategy(k, masters=None, optimal=None):
    return 9 * (k**3), []



# RANDOM


def write_random_strategy(file, k, size, masters):
    file.write(f"\n{k}\n")
    for i in range(size):
        master_power = random.randint(MIN_POWER, MAX_POWER)
        masters.append(("", master_power))
        file.write(f", {master_power}\n")


def optimal_value_random_strategy(k, masters=None, optimal=None):
    return algorithm(masters, k)




# ALTERNATIVE

def generate_optimal_solution (size, k):

    min = 10
    max = 300

    min += size // k + size % k 

    sum_for_each_set = (random.randint(min, min + max)) 

    masters = []
    optimal_value = k * (sum_for_each_set ** 2)
    
    masters_for_each_set = size // k 
    sets = []

    for j in range(k):
        
        remains = sum_for_each_set
        masters_for_set_j = []

        if j == k - 1 and size % k != 0:
            masters_for_each_set += size % k 

        for i in range(masters_for_each_set - 1):

            master_value = random.randint(1, remains - (masters_for_each_set - len(masters_for_set_j)))
            masters_for_set_j.append(("", master_value))
            remains -= master_value

        master_value = remains
        
        masters_for_set_j.append(("", master_value))
        masters.extend(masters_for_set_j)
        sets.append(masters_for_set_j)


    return masters, optimal_value


def write_alternative_strategy(file, k, size, masters):

    file.write(f"\n{k}\n")
    for master in masters:
        file.write(f"{master[NAME_POSITION]}, {master[VALUE_POSITION]}\n")


def optimal_value_alternative_strategy (k, masters=None, optimal=None):
    return optimal, []




def print_expected_results (masters, size, k, results_path, optimal_strategy, optimal = None):
    if not os.path.exists(results_path):
        open(results_path, "w").close()
    
    with open(results_path, "r") as file:
        lines = file.readlines()
        file_found = False
        optimal_value, _ = optimal_strategy(k, masters, optimal)

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



def generate_data_sets(
    folder, results_path, write_strategy, optimal_strategy, k, masters=None, size=None, optimal=None
):

    with open(f"{folder}/{size}_{k}.txt", "w") as file:
        write_strategy(file, k, size, masters)

    if results_path is None:
        return 

    print_expected_results(masters, size, k, results_path, optimal_strategy, optimal)






def generate_alternative_ds(size, k):

    masters, optimal = generate_optimal_solution(size, k)

    generate_data_sets(
        FOLDER,
        EXPECTED_RESULTS_PATH,
        write_alternative_strategy,
        optimal_value_alternative_strategy,
        k,
        masters,
        size,
        optimal
    )
        

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


def generate_random_data_sets(size, k, with_expected_results):
    results_path = EXPECTED_RESULTS_PATH
    if not with_expected_results:
        results_path = None

    generate_data_sets(
        FOLDER,
        results_path,
        write_random_strategy,
        optimal_value_random_strategy,
        k,
        [],
        size,
    )



def get_file_info_by_size(size):
    return get_file_info(f"{FOLDER}/{size}_{size // 2}.txt")



if __name__ == "__main__":
    
    for i in range(MIN_SIZE, MAX_SIZE):
        for k in range(2, i - 1):

            masters, optimal = generate_optimal_solution(i, k)
            p_sum, _ = pakku(masters, k)
            bt_sum, _ = algorithm(masters, k)
            print(f"ratio: {p_sum / bt_sum}. k = {k}. size = {i}")
            print(f"optimal value: {bt_sum}. generated_value: {optimal}")
            print(optimal == bt_sum)