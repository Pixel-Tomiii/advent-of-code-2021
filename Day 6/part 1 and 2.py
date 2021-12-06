def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines

data = get_data()

# PART 1 START
fishes = list(map(int, data[0].split(",")))
# Create mapping.
ages = dict()
for timer in range(9):
    ages[timer] = 0
    for fish in fishes:
        if timer == fish:
            ages[timer] += 1

for day in range(256):
    fishes_at_0 = ages[0]

    # move all fishes down a key.
    for timer in range(1, 9):
        ages[timer - 1] = ages[timer]
    ages[8] = 0

    # Reset.
    ages[6] += fishes_at_0
    ages[8] += fishes_at_0

print("Total fishes:", sum(ages.values()))
