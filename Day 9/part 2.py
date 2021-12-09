def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [list(map(int, list(line.rstrip()))) for line in file]
    return lines

data = get_data()

# PART 2 START
total = 0
basins = []

row_size = len(data[0])
checked = set()


def get_size(x, y, total=0):
    if data[y][x] == 9:
        return 0

    checked.add((x, y))
    total += 1
    
    if (x + 1, y) not in checked and x + 1 < row_size:
        total += get_size(x + 1, y)

    if (x - 1, y) not in checked and x - 1 >= 0:
        total += get_size(x - 1, y)

    if (x, y + 1) not in checked and y + 1 < len(data):
        total += get_size(x, y + 1)

    if (x, y - 1) not in checked and y - 1 >= 0:
        total += get_size(x, y - 1)

    return total

    

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

        # Point gained.
        checked = set()
        basins.append(get_size(x, y))

basins = sorted(basins, reverse = True)
print("Risk level:", basins[0] * basins[1] * basins[2])
