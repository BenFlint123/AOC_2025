

def read_txt(filepath):
    with open(filepath) as f:
        data = f.readlines()
    return data


def main():
    data = read_txt(r"AOC_2025\Day_2\Day_2_input.txt")
    for string in data:
        data = string.split(',')
    
    running_total = 0
    for ID_range in data:
        lower, upper = ID_range.split('-')
        lower = int(lower)
        upper = int(upper)

        for id in range(lower, upper+1):
            string_id = str(id)
            if (len(string_id)) % 2 != 0:  # No way of having repeats if length is odd
                continue
            else:
                mid_point = int((len(string_id)) / 2)
                if string_id[:mid_point] == string_id[mid_point:]:
                    running_total += int(string_id)
    
    print(running_total)


            
    




if __name__ == "__main__":
    main()