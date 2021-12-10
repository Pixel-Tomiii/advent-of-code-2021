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
stack = []
syntax_map = {"(":")", "{":"}", "<":">", "[":"]"}
totals = []
total_map = {")":1, "]":2, "}":3, ">":4}

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
            break

    # Skip broken lines.
    else:
        for char in stack[::-1]:
            line_total = (5 * line_total) + total_map[syntax_map[char]]
        totals.append(line_total)

totals = sorted(totals)
print(f"Total: {totals[(len(totals)//2)]}")
