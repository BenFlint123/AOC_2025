


def read_input(filepath):
    with open(filepath) as f:
        data = [string.strip() for string in f.readlines()]
    return data

def get_example_input():
    return [
        '987654321111111',
        '811111111111119',
        '234234234234278',
        '818181911112111'
    ]

def main():


    data = read_input(r"AOC_2025\Day_3\Day_3_input.txt")
    # data = get_example_input()


    total_joltage = 0

    for bank in data:
        joltages = [int(char) for char in list(bank)]
        max_joltage = max(joltages[:-1])  # can't select last battery first as it doesn't leave space for the 2nd battery
        bank_joltage = 0
        for i, val in enumerate(joltages):
            if val == max_joltage:
                bank_joltage += (joltages.pop(i) *10)
                max_remaining_joltage = max(joltages[i:])
                for j, val in enumerate(joltages[i:]):
                    if val == max_remaining_joltage:
                        bank_joltage += max_remaining_joltage
                        break
                total_joltage += bank_joltage
                break

    print(f"Total joltage: {total_joltage}")


if __name__ == "__main__":
    main()