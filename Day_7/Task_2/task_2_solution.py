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


def harry_part_2(content: list):
    start = [(x.index("S"), y) for y, x in enumerate(content) if "S" in x]  # doesn't unnecessarily convert from characters to integers or from strings to lists

    @cache  # uses @cache decorator to keep the inputs and outputs of this function in a dictionary of k, v pairs (x, y) -> result
    def tachyon_beam(x: int, y: int):
        if y == len(content[0]):
            return 1
        elif content[y][x] == "^":
            return tachyon_beam(x - 1, y + 1) + tachyon_beam(x + 1, y + 1)  # writes same algorithm in cleaner way
        else:
            return tachyon_beam(x, y + 1)

    print("The hits on the cached dictionary is:", tachyon_beam.cache_info().hits)

    return tachyon_beam(start[0][0], start[0][1])

def count_paths(data, node_row_index, node_column_index, memo=None):
    if memo is None:
        memo = {}
    
    # Check if we've already calculated this position
    if (node_row_index, node_column_index) in memo:
        return memo[(node_row_index, node_column_index)]
    
    # Base case: reached the bottom row
    if node_row_index == len(data) - 1:
        result = 1 if data[node_row_index][node_column_index] == 1 else 0
        memo[(node_row_index, node_column_index)] = result
        return result
    
    # Current position must be a 1 to be a valid path
    if data[node_row_index][node_column_index] != 1:
        memo[(node_row_index, node_column_index)] = 0
        return 0
    
    path_count = 0
    next_row = node_row_index + 1
    next_val = data[next_row][node_column_index]
    
    if next_val == 1:
        # Continue straight down
        path_count += count_paths(data, next_row, node_column_index, memo)
    elif next_val == 2:
        # Split: go left and right
        if node_column_index > 0:
            path_count += count_paths(data, next_row, node_column_index - 1, memo)
        if node_column_index < len(data[0]) - 1:
            path_count += count_paths(data, next_row, node_column_index + 1, memo)
    # If next_val == 0, this path is blocked, return 0
    
    memo[(node_row_index, node_column_index)] = path_count
    return path_count


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

    timelines = count_paths(formatted_data, 0, formatted_data[0].index(1))

    print(timelines)

        

if __name__ == "__main__":
    main()

