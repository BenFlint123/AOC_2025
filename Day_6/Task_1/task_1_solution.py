import numpy as np


def read_input_data(filepath):

    with open(filepath) as f:
        data = [string.split() for string in f]
        return data


def get_example_input():
    data = ["123 328  51 64",
            "45 64  387 23", 
            "6 98  215 314",
            "*   +   *   +"]
    data = [string.split() for string in data]
    return data

def main():
    data = read_input_data(r"AOC_2025\Day_6\day_6_input.txt")
    #data = get_example_input()

    multiply_arrays = [[], [], [], []]
    add_arrays = [[], [], [], []]

    for i, operator in enumerate(data[4]):
        if operator == '+':
            add_arrays[0].append(data[0][i])
            add_arrays[1].append(data[1][i])
            add_arrays[2].append(data[2][i])
            add_arrays[3].append(data[3][i])
        elif operator == '*':
            multiply_arrays[0].append(data[0][i])
            multiply_arrays[1].append(data[1][i])
            multiply_arrays[2].append(data[2][i])
            multiply_arrays[3].append(data[3][i])
    
    add_arrays = np.array(add_arrays, dtype=int)
    multiply_arrays = np.array(multiply_arrays, dtype=int)

    sum_array = add_arrays[0] + add_arrays[1] + add_arrays[2] + add_arrays[3]
    product_array = multiply_arrays[0] * multiply_arrays[1] * multiply_arrays[2] * multiply_arrays[3]
    total_sum = sum_array.sum() + product_array.sum()
    print(total_sum)

if __name__ == '__main__':
    main()

