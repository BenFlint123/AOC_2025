

def read_txt(filepath):
    with open(filepath) as f:
        data = f.readlines()
    return data


def main():
    data = read_txt(r"AOC_2025\Day_2\Day_2_input.txt")
    print(data)


if __name__ == "__main__":
    main()