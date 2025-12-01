
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
        

def brute_force_solution():
    current_dial_idx = 50
    instructions = read_csv_to_list(r"Day_1\day_1_input.csv")
    instructions = concatenate_list_of_lists(instructions)
    dial_values = list(range(100))
    zero_counter = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])

        while distance > 0:
            if direction == 'R':
                if current_dial_idx == 99:
                    current_dial_idx = 0
                    zero_counter += 1
                else:
                    current_dial_idx += 1
            elif direction == 'L':
                if current_dial_idx == 0:
                    current_dial_idx = 99
                elif current_dial_idx == 1:
                    current_dial_idx -= 1
                    zero_counter += 1
                else:
                    current_dial_idx -= 1

            distance -= 1
    
    print(f"Final number of zeros from brute force: {zero_counter}")

                    
def better_solution():
    """Come back to this - is there a way of doing this without doing the steps 
    1-by-1. Feels very inefficient.
    """

    dial_value = 50
    dial_values = list(range(100))
    instructions = read_csv_to_list(r"Day_1\day_1_input.csv")
    instructions = concatenate_list_of_lists(instructions)
    zero_counter = 0

    for instruction in instructions:
        direction = instruction[0]
        distance = int(instruction[1:])
        net_distance = distance % 100 # all values > 100 involve spinning the dial back to current value and adding remainder
        total_rotations = distance // 100 # Now count the number of spins here
        zero_counter += total_rotations

        # I am double counting when I land on a zero and there's a change in direction
        # when I move right to zero I go past 99 and increment 1 to zero
        # If I then move left, I go below zero and increment 1 again 
        # But I've actually only pointed at zero once.
        if net_distance == 0:
            continue
        if direction == 'R':
            new_value = (dial_value + net_distance) % 100
            # Count zero if we pass through it OR end on it
            # We pass through/reach zero if dial_value + net_distance >= 100
            if dial_value + net_distance >= 100:
                zero_counter += 1
            dial_value = new_value
            
        elif direction == 'L':
            new_value = (dial_value - net_distance) % 100
            # Count zero if we pass through it OR end on it
            # Exception: don't count if we START on zero (dial_value == 0)
            if dial_value > 0 and dial_value - net_distance <= 0:
                zero_counter += 1
            dial_value = new_value

        else:
            print(f"Invalid instruction does not begin with 'L' or 'R': {instruction}")

    print(f"Final number of zeros from better solution: {zero_counter}")




if __name__ == "__main__":
    brute_force_solution()
    better_solution()