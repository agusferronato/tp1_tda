from files import get_expected_results, get_file_info, ls, FILES_PATH
import re
from tp3 import algorithm



def tests():
    optimal_value = get_expected_results()

    for file_name in ls(FILES_PATH):
        
        if re.match(r'^\d', file_name) and file_name == "20_4.txt":
            
            masters, k = get_file_info(f'{FILES_PATH}/{file_name}')
            
            best_sum, _ = algorithm(masters, k)

            if best_sum == optimal_value[file_name]:
                print(f"👌 Paso. Archivo {file_name}. Valor obtenido {best_sum}")
            else: 
                print(f"⚠️ No paso. Archivo {file_name}. Valor esperado: {optimal_value[file_name]}. Valor obtenido: {best_sum}")



if __name__ == "__main__":
    tests()