import copy
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
graph = dict()

for row in data:
    start, end = row.split("-")

    if end not in graph:
        graph[end] = set()

    if start not in graph:
        graph[start] = set()

    graph[start].add(end)
    graph[end].add(start)

# Find all paths.
def get_path(node, graph, path):
    total = 0
    
    if node == "end":
        return 1

    for child in graph[node]:
        if child.islower():
            if child not in path:
                new_path = path.copy()
                new_path.append(child)
                total += get_path(child, graph, new_path)
        else:
            new_path = path.copy()
            new_path.append(child)
            total += get_path(child, graph, new_path)
        
    return total

print("total paths:", get_path("start", graph, ["start"]))

    
