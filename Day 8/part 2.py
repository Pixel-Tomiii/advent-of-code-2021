import math

def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines

data = get_data()

display = list("abcdefg")

# PART 1 START

zero = set(list("abcefg"))
one = set(list("cf"))
two = set(list("acdeg"))
three = set(list("acdfg"))
four = set(list("bcdf"))
five = set(list("abdfg"))
six = set(list("abdefg"))
seven = set(list("acf"))
eight = set(list("abcdefg"))
nine = set(list("abcdfg"))

delim = "|"

numbers = [zero, one, two, three, four, five, six, seven, eight, nine]
unique = [len(one), len(four), len(seven), len(eight)]

map_to_segment = dict()
for value in display:
    map_to_segment[value] = []
    
total = 0
# Fetch all unique values.
for line in data:
    data_inputs, data_outputs = line.split(delim)
    data_inputs = data_inputs.rstrip().split(" ")
    data_outputs = data_outputs.lstrip().split(" ")

    # Check if each output is unique.
    if all([len(output) in unique for output in data_outputs]):
        output = ""
        for value in data_outputs:
            if len(value) == 2:
                output += "1"
            elif len(value) == 3:
                output += "7"
            elif len(value) == 4:
                output += "4"
            else:
                output += "8"
        total += int(output)
        continue

    absolute_mapping = ["", "", "", "", "", "", ""]
    unique_mapping = [0, 0, 0, 0, 0, 0, 0]

    for inp in data_inputs:
        if len(inp) not in unique:
            continue
        for digit in inp:
            unique_mapping[display.index(digit)] += 1

    for inp in data_outputs:
        if len(inp) not in unique:
            continue
        for digit in inp:
            unique_mapping[display.index(digit)] += 1

    cfpair = ""
    highest = max(unique_mapping)
    # Find out which map to c and f.
    for index, value in enumerate(unique_mapping):
        if value == highest:
            cfpair += display[index]
    
    # find which of the cf pair maps to f.
    for inp in data_inputs:
        if len(inp) == len(six):
            for digit in cfpair:
                if digit not in inp:
                    absolute_mapping[display.index("c")] = digit
                    break
            else:
                continue
            break
    else:
        for inp in data_outputs:
            if len(inp) == len(six):
                for digit in cfpair:
                    if digit not in inp:
                        absolute_mapping[display.index("c")] = digit
                        break
                else:
                    continue
                break

    # find which of the cf pair maps to c.
    if cfpair[0] in absolute_mapping:
        absolute_mapping[display.index("f")] = cfpair[1]
    else:
        absolute_mapping[display.index("f")] = cfpair[0]


    # Find which of the inp/out are 2, 3, 5
    length5 = dict()
    length5[2] = []
    length5[3] = []
    length5[5] = []
    
    for inp in data_inputs:
        if len(inp) == len(two):
            # determine if it is 2 3 or 5
            if absolute_mapping[display.index("c")] in inp and absolute_mapping[display.index("f")] in inp:
                length5[3].append(inp)
            elif absolute_mapping[display.index("c")] in inp:
                length5[2].append(inp)
            else:
                length5[5].append(inp)
                
    for inp in data_outputs:
        if len(inp) == len(two):
            # determine if it is 2 3 or 5
            if absolute_mapping[display.index("c")] in inp and absolute_mapping[display.index("f")] in inp:
                length5[3].append(inp)
            elif absolute_mapping[display.index("c")] in inp:
                length5[2].append(inp)
            else:
                length5[5].append(inp)

    # Find out unique values for 2.
    if length5[2]:
        current = length5[2][0]

        # Compare with 3.
        if length5[3]:
            for digit in length5[3][0]:
                current = current.replace(digit, "")
            absolute_mapping[display.index("e")] = current
        # Compare with 5.        
        else:
            for digit in length5[5][0]:
                current = current.replace(digit, "")
            for digit in absolute_mapping:
                current = current.replace(digit, "")
            absolute_mapping[display.index("e")] = current
    # Find out unique values for 5.
    if length5[5]:
        current = length5[5][0]

        # Compare with 3.
        if length5[3]:
            for digit in length5[3][0]:
                current = current.replace(digit, "")
            absolute_mapping[display.index("b")] = current
        # Compare with 2.        
        else:
            for digit in length5[2][0]:
                current = current.replace(digit, "")
            for digit in absolute_mapping:
                current = current.replace(digit, "")
            absolute_mapping[display.index("b")] = current

    # Find which of the out are 0, 6, or 9
    length9 = dict()
    length9[0] = []
    length9[6] = []
    length9[9] = []

    for inp in data_outputs:
        if len(inp) == len(zero):
            if absolute_mapping[display.index("c")] in inp and absolute_mapping[display.index("e")] in inp:
                length9[0].append(inp)
            elif absolute_mapping[display.index("c")] in inp:
                length9[9].append(inp)
            else:
                length9[6].append(inp)
    # Find output.
    output = ""
    for value in data_outputs:
        # Uniques.
        if len(value) in unique:
            if len(value) == 2:
                output += "1"
            elif len(value) == 3:
                output += "7"
            elif len(value) == 4:
                output += "4"
            else:
                output += "8"

        # Other numbers.
        # if 2, 3 or 5.
        if value in length5[2]:
            output += "2"
        elif value in length5[3]:
            output += "3"
        elif value in length5[5]:
            output += "5"
        # if 0, 6, or 9.
        elif value in length9[0]:
            output += "0"
        elif value in length9[6]:
            output += "6"
        elif value in length9[9]:
            output += "9"

    total += int(output)
    
print(total)
    
