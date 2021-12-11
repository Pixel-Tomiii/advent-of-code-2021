import copy
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

def output(grid):
    print("\n".join([str(row) for row in grid]))
    print()
        
def get_neighbours(grid, x, y):
    neighbours = []

    for offset_y in range(-1, 2):
        for offset_x in range(-1, 2):
            if offset_x == 0 and offset_y == 0:
                continue
            if (x + offset_x >= 0 and x + offset_x < len(grid[0]) and
                    y + offset_y >= 0 and y + offset_y < len(grid)):
                neighbours.append((x + offset_x, y + offset_y))
    return neighbours

def update(grid):
    for y, row in enumerate(grid):
        for x, octo in enumerate(row):
            grid[y][x] += 1

def flash_all(grid, flashed):
    flash = False
    total = 0
    for y, row in enumerate(grid):
        for x, octo in enumerate(row):
            if grid[y][x] > 9:
                flash = True
                total += 1
                flashed.add((x, y))
                grid[y][x] = 0
                neighbours = get_neighbours(grid, x, y)
                for x, y in neighbours:
                    if ((x, y)) not in flashed:
                        grid[y][x] += 1

                    
    return flash, total

total_flashes = 0
size = len(data) * len(data[0])
step = 0
while True:
    step += 1
    flashed = set()
    
    update(data)
    
    while True:
        flash, total = flash_all(data, flashed)
        if not flash:
            break
    if len(flashed) == size:
        break


print("Step:", step)
