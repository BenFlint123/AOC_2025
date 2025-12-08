import copy

def read_input(filepath):
    with open(filepath) as f:
        data = [string.strip() for string in f.readlines()]
    return data

def get_example_input():
    data = [
    ".......S.......",
    "...............",
    ".......^.......",
    "...............",
    "......^.^......",
    "...............",
    ".....^.^.^.....",
    "...............",
    "....^.^...^....",
    "...............",
    "...^.^...^.^...",
    "...............",
    "..^...^.....^..",
    "...............",
    ".^.^.^.^.^...^.",
    "..............."
    ]
    return data


def main():
    data = read_input(r"AOC_2025\Day_7\day_7_input.txt")
    # data = get_example_input()

    formatted_data = []
    for strng in data:
        strng = strng.replace('S', '1')
        strng = strng.replace('^', '2')
        strng = strng.replace('.', '0')
        formatted_data.append([int(char) for char in list(strng)])

    split_counter = 0
    for i, row in enumerate(formatted_data):
        if i == len(formatted_data) - 1:
            break
        else:
            # formatted_data[i-1] = data_to_edit[i-1]
            for j, element in enumerate(row):
                if formatted_data[i][j] == 0:
                    continue
                elif formatted_data[i][j] == 1 and formatted_data[i+1][j] == 0:
                    formatted_data[i+1][j] = 1
                elif formatted_data[i][j] == 1 and formatted_data[i+1][j] == 1:
                    continue
                elif formatted_data[i][j] == 1 and formatted_data[i+1][j] == 2:
                    if j != 0:
                        formatted_data[i+1][j-1] = 1
                    if j != len(row):
                        formatted_data[i+1][j+1] = 1
                    split_counter += 1
                elif formatted_data[i][j] == 2:
                    formatted_data[i+1][j] = 0
    
    print(split_counter)



        

if __name__ == "__main__":
    main()

