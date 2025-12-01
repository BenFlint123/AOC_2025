
import csv

def read_csv_to_list(file_path: str):
    with open(file_path) as f:
        csv_reader = csv.reader(f)
        data_as_list = list(csv_reader)
        return data_as_list

def concatenate_list_of_lists(list_of_lists: list):
    return_list = []
    for list in list_of_lists:
        for element in list:
            return_list.append(element)
    return return_list
        

def main():
    dial_value = 50
    dial_values = list(range(100))
    instructions = read_csv_to_list(r"Day_1\day_1_input.csv")
    instructions = concatenate_list_of_lists(instructions)
    zero_counter = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        net_distance = distance % 100 # all values > 100 involve spinning the dial back to current value and adding remainder


        if direction == 'R':
            dial_value += net_distance
            if dial_value > 99:
                dial_value -= 100
        elif direction == 'L':
            dial_value -= net_distance
            if dial_value < 0:
                dial_value += 100
        else:
            print(f"Invalid instruction does not begin with 'L' or 'R': {instruction}")


        if dial_value == 0:
            zero_counter += 1

    print(f"Final number of zeros: {zero_counter}")



if __name__ == "__main__":
    main()