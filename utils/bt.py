import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from utils.files import ls, FILES_PATH, EXPECTED_RESULTS_FILE, get_file_info
import re
from data_sets import generate_data_set


NUM_FILES = 10
FILE_SIZE = 5
PARENTHESIS_POSITION = 1


def algorithm_by_bf (xi, f, index, last_attack, current_solution, best_solution):

    if index == len(xi):
        if sum(current_solution) > sum(best_solution):
            return current_solution[:]
        return best_solution


    current_xi = xi[index]
    current_f = f[index - last_attack]

    current_solution.append(min(current_xi, current_f))

    best_solution = algorithm_by_bf(xi, f, index + 1, index + 1, current_solution, best_solution) 

    current_solution.pop()

    return algorithm_by_bf(xi, f, index + 1, last_attack, current_solution, best_solution) 


def bf (xi, f):
    return sum(algorithm_by_bf(xi, f, 0, 0, [], []))





if __name__ == "__main__":

    max_index = 0

    for file_name in ls(FILES_PATH):
        if re.match(rf'^{FILE_SIZE}\D', file_name):
            if file_name[PARENTHESIS_POSITION] != ".":
                current_index = int(file_name[PARENTHESIS_POSITION + 1:file_name.index(")")])
                if current_index > max_index:
                    max_index = current_index
    
    index = max_index + 1

    # Generate 10 example files

    for i in range(index, index + NUM_FILES):
        generate_data_set(FILE_SIZE, FILES_PATH, f'({i})')

        with open(f'{FILES_PATH}/{EXPECTED_RESULTS_FILE}', "a") as file:
            
            xi, f = get_file_info(f'{FILES_PATH}/{FILE_SIZE}({i}).txt')

            file.write(f'{FILE_SIZE}({i}).txt\n')
            file.write("\n")
            file.write(str(bf(xi, f)) + "\n")

