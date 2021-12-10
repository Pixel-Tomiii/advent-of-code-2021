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
stack = []
syntax_map = {"(":")", "{":"}", "<":">", "[":"]"}
total = 0
total_map = {")":3, "]":57, "}":1197, ">":25137}

for line in data:
    stack = []
    line_total = 0
    for char in line:
        # if opener.
        if char in syntax_map.keys():
            stack.append(char)
            continue
            
        # Peek last item.
        if len(stack) > 0 and syntax_map[stack.pop(-1)] != char:
            line_total += total_map[char]

    total += line_total

print(f"Total: {total}")
