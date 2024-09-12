import numpy as np
import os

input_path = os.path.join('src', 'input')
output_path = os.path.join('src', 'output')


def verify_number(input_file, output_file):
    with open(input_file, 'r') as f:
        numbers = np.array([int(linha.strip()) for linha in f.readlines()])

    with open(output_file, 'w') as f_out:
        for number in numbers:
            if np.mod(number, 2) == 0:
                result = f"{number} is even\n"
            else:
                result = f"{number} is odd\n"
            f_out.write(result)


# Chame a função com o caminho do arquivo de entrada e saída
verify_number(os.path.join(input_path, 'input_numbers.txt'),
              os.path.join(output_path, 'output_numbers.txt'))
