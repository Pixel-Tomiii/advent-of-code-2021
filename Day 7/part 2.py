import math

def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines

data = get_data()

def fuel_to_pos(crabs, pos):
    fuel = 0
    for crab in crabs:
        fuel += sum([x for x in range(1, abs(crab - pos) + 1)])

    return fuel

# PART 1 START
crabs = list(map(int, data[0].split(",")))

fuel, pos = math.inf, 0

for new_pos in range(min(crabs), max(crabs) + 1):
    new_fuel = fuel_to_pos(crabs, new_pos)
    if new_fuel < fuel:
        fuel = new_fuel
        pos = new_pos

print(fuel, pos)
        
