
def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [line.rstrip().split(",") for line in file if line.rstrip() != ""]
    return lines

data = get_data()

# PART 2 START

coords = set()
max_y = 0
max_x = 0

for row in data:
    if len(row) == 2:
        x = int(row[0])
        y = int(row[1])

        coords.add((x, y))

        if x > max_x:
            max_x = x

        if y > max_y:
            max_y = y

    # Fold
    else:
        row = row[0].removeprefix("fold along ")
        axis, amount = row.split("=")
        amount=int(amount)

        if axis == "x":
            for x in range(amount + 1, max_x + 1):
                for y in range(0, max_y + 1):
                    if (x, y) in coords:
                        coords.remove((x, y))
                        coords.add((amount - (x - amount), y))

            max_x = amount - 1

        elif axis == "y":
            for y in range(amount + 1, max_y + 1):
                for x in range(0, max_x + 1):
                    if (x, y) in coords:
                        coords.remove((x, y))
                        coords.add((x, amount - (y - amount)))
            max_y = amount - 1
        
for y in range(max_y + 1):
    line = ""
    for x in range(max_x + 1):
        if (x, y) in coords:
            line += "#"
        else:
            line += " "
    print(line)
