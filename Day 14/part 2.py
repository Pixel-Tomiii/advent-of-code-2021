import copy
def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file if line.rstrip() != ""]
    return lines

data = get_data()

# PART 2 START
    
pairs = dict()
chars = dict()

# initialise
for i in range(len(data[0]) - 1):
    pairs[data[0][i] + data[0][i+1]] = 1

for char in data[0]:
    if char not in chars:
        chars[char] = 0
    chars[char] += 1
    
maps = dict()
data = data[1:]

for row in data:
    pat, insert = row.split(" -> ")
    maps[pat] = insert

for step in range(40):
    new_pairs = dict()
    
    for pair in pairs.keys():
        if pair in maps:
            amount = pairs[pair]
            
            pair1 = pair[0] + maps[pair]
            pair2 = maps[pair] + pair[1]

            if maps[pair] not in chars:
                chars[maps[pair]] = 0
            chars[maps[pair]] += amount
                
                
            if pair1 not in new_pairs:
                new_pairs[pair1] = 0
            if pair2 not in new_pairs:
                new_pairs[pair2] = 0

            new_pairs[pair1] += amount
            new_pairs[pair2] += amount
    pairs = new_pairs


most = max(chars.values())
least = min(chars.values())

print("Result:", most - least)

