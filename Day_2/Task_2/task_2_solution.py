
def get_example_input():
    data = [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
        "565653-565659",
        "824824821-824824827",
        "2121212118-2121212124"
    ]
    return data

def read_txt(filepath):
    with open(filepath) as f:
        data = f.readlines()
    return data

def is_only_repeats(string):
    cutoff = len(string) // 2

    for element_size in range(1, cutoff+1):
        if len(string) % element_size != 0:
            continue
        chunks = [string[i:i+element_size] for i in range(0, len(string), element_size)]
        if len(set(chunks)) == 1:
            return True
    return False

def main():
    data = read_txt(r"AOC_2025\Day_2\Day_2_input.txt")
    for string in data:
        data = string.split(',')

    #data = get_example_input()
    running_total = 0
    for ID_range in data:
        lower, upper = ID_range.split('-')

        lower = int(lower)
        upper = int(upper)

        for id in range(lower, upper+1):
            string_id = str(id)
            
            if is_only_repeats(string_id):
                running_total += int(string_id)

    print(running_total)


if __name__ == "__main__":
    main()