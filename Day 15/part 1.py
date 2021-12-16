import copy
import math

def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [list(map(int, list(line.rstrip()))) for line in file if line.rstrip() != ""]
    return lines

data = get_data()

def distance(x, y):
    return ((WIDTH - x) + (HEIGHT - y))

WIDTH = len(data[0])
HEIGHT = len(data)

new = set([(0, 0)])
visited = dict()
visited[(0, 0)] = 0, data[0][0] + distance(0, 0)

def get_min(new, visited):
    smallest = math.inf
    node = None

    for pos in new:
        if visited[pos][1] < smallest:
            node = pos
            smallest = visited[pos][1]

    return pos

while new:
    x, y = get_min(new, visited)
    new.remove((x, y))

    left = None
    right = None
    
    # if right exists.
    if x + 1 < WIDTH:
        absolute = visited[(x, y)][0] + data[y][x+1]
        if (x + 1, y) in visited:
            if absolute < visited[(x + 1, y)][0]:
                visited[(x + 1, y)] =  absolute, absolute + distance(x + 1, y)
                new.add((x + 1, y))
        else:
            visited[(x + 1, y)] =  absolute, absolute + distance(x + 1, y)
            new.add((x + 1, y))

    # if down exists.
    if y + 1 < HEIGHT:
        absolute = visited[(x, y)][0] + data[y+1][x]
        if (x, y + 1) in visited:
            if absolute < visited[(x, y + 1)][0]:
                visited[(x, y + 1)] = absolute, absolute + distance(x, y + 1)
                new.add((x, y + 1))
        else:
            visited[(x, y + 1)] = absolute, absolute + distance(x, y + 1)
            new.add((x, y + 1))

    # if left exists.
    if x - 1 >= 0:
        absolute = visited[(x, y)][0] + data[y][x-1]
        if (x - 1, y) in visited:
            if absolute < visited[(x - 1, y)][0]:
                visited[(x - 1, y)] =  absolute, absolute + distance(x - 1, y)
                new.add((x - 1, y))
        else:
            visited[(x - 1, y)] =  absolute, absolute + distance(x - 1, y)
            new.add((x - 1, y))

    # if up exists.
    if y - 1 >= 0:
        absolute = visited[(x, y)][0] + data[y-1][x]
        if (x, y - 1) in visited:
            if absolute < visited[(x, y - 1)][0]:
                visited[(x, y - 1)] = absolute, absolute + distance(x, y - 1)
                new.add((x, y - 1))
        else:
            visited[(x, y - 1)] = absolute, absolute + distance(x, y - 1)
            new.add((x, y - 1))


print("Shortest:", visited[(WIDTH-1, HEIGHT-1)][0])
                


    

