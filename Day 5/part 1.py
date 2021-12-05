def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines

data = get_data()
lines = []
# PART 1 START
for row in data:
    row = row.split(" -> ")
    p1 = tuple(map(int, row[0].split(",")))
    p2 = tuple(map(int, row[1].split(",")))
    lines.append((p1, p2))

coords = dict()

for vent in lines:
    # Get x and y difference.
    xDiff = vent[0][0] - vent[1][0]
    yDiff = vent[0][1] - vent[1][1]

    if xDiff != 0 and yDiff != 0:
        continue
    
    # going along x
    if yDiff == 0:
        y = vent[0][1]
        small = min(vent[0][0], vent[1][0])
        big = max(vent[0][0], vent[1][0])
        for x in range(small, big + 1):
            if (x, y) not in coords:
                coords[(x, y)] = 0
            coords[(x, y)] += 1

    # going along y
    if xDiff == 0:
        x = vent[0][0]
        small = min(vent[0][1], vent[1][1])
        big = max(vent[0][1], vent[1][1])
        for y in range(small, big + 1):
            if (x, y) not in coords:
                coords[(x, y)] = 0
            coords[(x, y)] += 1



# Get results.
total = 0
for value in coords.values():
    if value >= 2:
        total += 1

print("DANGER ZONES:", total)
