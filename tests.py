from pathlib import Path
import re 
from tp2 import algorithm


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


def tests():
    for file_name in ls(FILES_PATH):
        if re.match(r'^\d', file_name):
            xi, f = get_file_info(file_name)
            eliminated_troops, strategy = algorithm(xi, f)



if __name__ == "__main__":
    tests()