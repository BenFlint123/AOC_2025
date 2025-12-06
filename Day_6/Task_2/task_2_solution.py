import numpy as np
import math


def read_input_data(filepath):

    with open(filepath) as f:
        data = f.read().splitlines()
        return data


def get_example_input():
    data = ["123 328  51 64 ",
            " 45 64  387 23 ", 
            "  6 98  215 314",
            "*   +   *   +  "]
    return data


def split_data(data):
    result = []
    current_group = []

    for sublist in data:
        if sublist == [' ', ' ', ' ', ' ']:
            if current_group:
                result.append(current_group)
                current_group = []
        else:
            current_group.append(sublist)
    if current_group:
        result.append(current_group)
    return result

def main():
    data = read_input_data(r"AOC_2025\Day_6\day_6_input.txt")
    # data = get_example_input()

    operators = data.pop(-1)
    operators = [strng.strip() for strng in list(operators) if strng != ' ']
    data = [list(strng) for strng in data]

    data = np.array(data)
    data = data.T.tolist()
    data = split_data(data)

    updated_data = []
    for lst in data:
        result = []
        for sublist in lst:
            number_str = ''.join(sublist).replace(' ', '')
            result.append(int(number_str))
        updated_data.append(result)

    results = []
    for i, operator in enumerate(operators):
        if operator == '+':
            results.append(sum(updated_data[i]))
        elif operator == '*':
            results.append(math.prod(updated_data[i]))
    
    total_sum = sum(results)

if __name__ == '__main__':
    main()

