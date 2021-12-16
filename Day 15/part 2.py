import numpy
import math
import time

def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [list(map(int, list(line.rstrip()))) for line in file if line.rstrip() != ""]
    return lines

class Node():
    def __init__(self, distance, h, previous, pos):
        self.distance = distance
        self.h = h
        self.previous = previous
        self.x, self.y = pos

    def __repr__(self):
        return f"Pos: ({self.x}, {self.y}) with distance {self.distance}, {self.h}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

class Heap():
    def __init__(self):
        self.nodes = [None]
        self.size = 0

    def add(self, node):
        self.nodes[self.size] = node

        index = self.size
        self.size += 1

        if len(self.nodes) <= self.size:
            new = [None for _ in range(self.size * 2)]
            for i, node in enumerate(self.nodes):
                new[i] = node
            self.nodes = new.copy()

        while index > 0:
            parent = (index - 1) // 2

            if self.nodes[parent].h > self.nodes[index].h:
                self.nodes[parent], self.nodes[index] = self.nodes[index], self.nodes[parent]
                index = parent
            else:
                break

    def pop(self):
        self.size -= 1
        ret = self.nodes[0]
        self.nodes[0] = self.nodes[self.size]

        index = 0
        while index < self.size:
            left = (index * 2) + 1
            right = (index * 2) + 2

            if left >= self.size:
                break

            if right >= self.size:
                point = left
            
            elif self.nodes[left].h < self.nodes[right].h:
                point = left
            else:
                point = right

            

            if self.nodes[point].h < self.nodes[index].h:
                self.nodes[point], self.nodes[index] = self.nodes[index], self.nodes[point]
                index = point
            else:
                break
        return ret
        

    def output(self):
        for node in self.nodes:
            print(node)

    def contains(self, node):
        for check in self.nodes:
            if check and check == node:
                return check

        return False

def get_node_distance(x, y, grid):
    """Fetch a node from the grid."""
    absolute_x = x % len(grid[0])
    absolute_y = y % len(grid)

    xDiff = x // len(grid[0])
    yDiff = y // len(grid)
    diff = xDiff + yDiff

    value = grid[absolute_y][absolute_x]

    if diff:
        value += diff

    if value > 9:
        value -= 9

    return value

def distance(x, y, dest_x, dest_y):
    return abs(dest_x - x) + abs(dest_y - y)
    
grid = get_data()
WIDTH = len(grid[0]) * 5
HEIGHT = len(grid) * 5

start = Node(0, distance(0, 0, WIDTH-1, HEIGHT-1), None, (0, 0))
heap = Heap()
current = start
checked = set([start])

while (current.x, current.y) != (WIDTH-1, HEIGHT-1):
    if len(checked) % 5000 == 0:
        print(len(checked), "CURRENT:", current)
    
    x, y = current.x, current.y
    checked.add(current)
    if x + 1 < WIDTH:
        right = Node(current.distance + get_node_distance(x+1, y, grid),
                     current.distance + get_node_distance(x+1, y, grid) + distance(x+1, y, WIDTH-1, HEIGHT-1),
                     current,
                     (x+1, y))
        in_heap = heap.contains(right)
        if not in_heap and right not in checked:
            heap.add(right)

        else:
            if in_heap:
                if in_heap.distance >= right.distance:
                    in_heap.distance = right.distance
                    in_heap.previous = current
                    in_heap.h = right.h
                    
    if y > 0:
        down = Node(current.distance + get_node_distance(x, y-1, grid),
                    current.distance + get_node_distance(x, y-1, grid) + distance(x, y-1, WIDTH-1, HEIGHT-1),
                    current,
                    (x, y-1))
        in_heap = heap.contains(down)
        if not in_heap and down not in checked:
            heap.add(down)
        else:
            if in_heap:
                if in_heap.distance >= down.distance:
                    in_heap.distance = down.distance
                    in_heap.previous = current
                    in_heap.h = down.h
                    
    if x > 0:
        left = Node(current.distance + get_node_distance(x-1, y, grid),
                    current.distance + get_node_distance(x-1, y, grid) + distance(x-1, y, WIDTH-1, HEIGHT-1),
                    current,
                    (x-1, y))
        in_heap = heap.contains(left)
        if not in_heap and left not in checked:
            heap.add(left)

        else:
            if in_heap:
                if in_heap.distance >= left.distance:
                    in_heap.distance = left.distance
                    in_heap.previous = current
                    in_heap.h = left.h
                    
    if y + 1 < HEIGHT:
        up = Node(current.distance + get_node_distance(x, y+1, grid),
                  current.distance + get_node_distance(x, y+1, grid) + distance(x, y+1, WIDTH-1, HEIGHT-1),
                  current,
                  (x, y+1))
        in_heap = heap.contains(up)
        if not in_heap and up not in checked:
            heap.add(up)

        else:
            if in_heap:
                if in_heap.distance >= up.distance:
                    in_heap.distance = up.distance
                    in_heap.previous = current
                    in_heap.h = up.h

##    heap.output()
    current = heap.pop()
##    print("CURRENT:", current)
##    input()

print(f"Distance: {current.distance}")
out = [[" " for _ in range(WIDTH)] for __ in range(HEIGHT)]

while current.previous:
    out[current.y][current.x] = str(int(get_node_distance(current.x, current.y, grid)))
    current = current.previous

log = open("out.txt", "w")
for row in out:
    print("".join(row), file=log)
log.close()



    

