
def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file if line.rstrip() != ""]
    return lines

data = get_data()

# PART 1 START

class Node():
    def __init__(value, next_value=None, previous_value=None):
        self.value = value
        self.next = next_value
        self.prev = previous_value
        

char_count = dict()
chars = data[0]
data = data[1:]

# Map inputs to outputs.
maps = dict()
for row in data:
    pat, insert = row.split(" -> ")
    maps[pat] = insert

for step in range(40):
    print(step)
    new_chars = ""
    for i in range(0, len(chars) - 1):
        pair = chars[i] + chars[i + 1]
        new_chars += chars[i]
        if pair in maps:
             new_chars += maps[pair]
    chars = new_chars + chars[i + 1]
        
for char in chars:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1

least = min(char_count.values())
most = max(char_count.values())
print(most - least)
##with open("out.txt", "w") as out:
##    print(chars, file=out)
