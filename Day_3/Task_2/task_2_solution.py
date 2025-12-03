

# plan for task 2 - put code in the first part into a function. 
# recursively call the function counting down from 12 with the max joltage being set to that far from the end of the string





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

def calculate_largest_joltage(joltages, num_digits, bank_joltage):
    if num_digits == 1:
        max_joltage = max(joltages)
    else:
        max_joltage = max(joltages[:-num_digits+1])  # need to leave room for remaining joltages
    bank_joltage = str(bank_joltage)
    for i, val in enumerate(joltages):
        if val == max_joltage:
            bank_joltage += str(joltages.pop(i))
            remaining_joltages = joltages[i:]
            if num_digits - 1 == 0:
                return bank_joltage
            else:
                return calculate_largest_joltage(remaining_joltages, num_digits-1, bank_joltage)

def main():


    data = read_input(r"AOC_2025\Day_3\Day_3_input.txt")
    # data = get_example_input()


    total_joltage = 0

    for bank in data:
        joltages = [int(char) for char in list(bank)]
        bank_joltage = int(calculate_largest_joltage(joltages, 12, ''))
        total_joltage += bank_joltage


    print(f"Total joltage: {total_joltage}")


if __name__ == "__main__":
    main()