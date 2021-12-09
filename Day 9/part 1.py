def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [list(map(int, list(line.rstrip()))) for line in file]
    return lines

data = get_data()

# PART 1 START
print(data)

total = 0

for y, row in enumerate(data):
    for x, point in enumerate(row):
        if x + 1 < len(row):
            if point >= data[y][x+1]:
                continue

        if x - 1 >= 0:
            if point >= data[y][x-1]:
                continue

        if y + 1 < len(data):
            if point >= data[y+1][x]:
                continue

        if y - 1 >= 0:
            if point >= data[y-1][x]:
                continue

        total += point + 1

print("Risk level:", total)
