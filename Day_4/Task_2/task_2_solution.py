import numpy as np

def get_input():
    with open(r"AOC_2025\Day_4\Day_4_input.txt") as f:
        data = [string.strip() for string in f.readlines()]
    return data

def get_example_input():
    data = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@."
    ]
    return data

def find_accessible_rolls(data):
    padded_data = np.pad(data, pad_width=1, constant_values=0) # pad outside with zeros to make room to shift into
    
    # take slices of the data so that each element now holds the neighbouring element in the given direction
    shift_up = padded_data[:-2, 1:-1]
    shift_down = padded_data[2:, 1:-1]
    shift_left = padded_data[1:-1, :-2]
    shift_right = padded_data[1:-1, 2:]
    shift_UL = padded_data[:-2, :-2]
    shift_UR = padded_data[:-2, 2:]
    shift_DL = padded_data[2:, :-2]
    shift_DR = padded_data[2:, 2:]

    # sum all 8 neighbours for each element
    neighbors = (shift_up + shift_down + shift_left + shift_right + shift_UL + shift_UR + shift_DL + shift_DR)
    
    # Check where there's a roll of paper and fewer than 4 neighbors
    accessible = (data == 1) & (neighbors < 4)
    return accessible


def main():
    data = get_input()
    # data = get_example_input()
    data = [list(string) for string in data]
    converted_data = []
    for lst in data:
        converted_data.append([1 if string == '@' else 0 for string in lst])

    data = np.array(converted_data)
    total_rolls = 0

    while(True):
        accessible_rolls = find_accessible_rolls(data)
        if np.sum(accessible_rolls) != 0:
            total_rolls += np.sum(accessible_rolls)
            data = data - accessible_rolls
        else:
            break
    
    
    print(total_rolls)

if __name__ == "__main__":
    main()