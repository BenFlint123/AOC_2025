
def read_input_file(file_path):
    with open(file_path) as f:
        data = [string.strip() for string in f.readlines()]
        split_index = data.index('')
        range_data, id_data = data[:split_index], data[split_index+1:]
        return range_data, id_data
    

def get_example_input():
    range_data = [
        "3-5",
        "10-14",
        "16-20",
        "12-18"
    ]
    id_data = [
        ""
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]
    return range_data, id_data
    

def main():
    range_data, id_data = read_input_file(r"AOC_2025\Day_5\day_5_input.txt")
    # range_data, id_data = get_example_input()

    # condense ranges into non-overlapping intervals
    range_data = [string.split('-') for string in range_data]
    range_data = [[int(i), int(j)] for [i, j] in range_data]
    sorted_range_data = sorted(range_data, key=lambda x: x[0])
    non_overlapping_ranges = []
    print('combine overlapping ranges...')
    for i, lst in enumerate(sorted_range_data):
        if i == 0:
            non_overlapping_ranges.append([int(id) for id in lst])
        else:
            if int(lst[0]) <= int(non_overlapping_ranges[-1][1]):
                non_overlapping_ranges[-1][1] = max(int(lst[1]), non_overlapping_ranges[-1][1])
            else:
                non_overlapping_ranges.append([int(id) for id in lst])

    id_data = [int(id) for id in id_data]
    id_data.sort()

    fresh_count = 0
    for id in id_data:
        for lst in non_overlapping_ranges:
            if id >= lst[0] and id <= lst[1]:
                fresh_count += 1
            else:
                continue
    print(fresh_count)

if __name__ == "__main__":
    main()
