def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines

data = get_data()

# PART 2 START
graph = dict()

for row in data:
    start, end = row.split("-")

    if end not in graph:
        graph[end] = set()

    if start not in graph:
        graph[start] = set()

    graph[start].add(end)
    graph[end].add(start)

def count_small_caves(path):
    """Returns true if there is at least 2 of a small cave"""
    small_caves = set()
    for cave in path:
        # Small caves only.
        if cave.islower():
            if cave not in small_caves:
                small_caves.add(cave)
            # If cave is already in set it must be there twice.    
            else:
                return True
            
    return False
        
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
                if not count_small_caves(path) and child not in ["start", "end"]:
                    new_path = path.copy()
                    new_path.append(child)
                    total += get_path(child, graph, new_path)
        else:
            new_path = path.copy()
            new_path.append(child)
            total += get_path(child, graph, new_path)
    
    return total

print("total paths:", get_path("start", graph, ["start"]))

    
