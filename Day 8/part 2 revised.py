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

# PART 1 START

segments = list("abcdefg")
numbers = list("0123456789")
sizes = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
unique_sizes = [size for size in sizes if sizes.count(size) < 2]

# Get total segements used to display the number.
number_to_size = lambda num:sizes[numbers.index(num)]
size_to_number = lambda size:numbers[sizes.index(size)]
size = lambda segments:len(segments)

delim = "|"

# Fetch all unique values.
for line in data:
    # Parse the line.
    data_inputs, data_outputs = line.split(delim)
    data_inputs = [set(digit) for digit in data_inputs.rstrip().split(" ")]
    data_outputs = [set(digit) for digit in data_outputs.lstrip().split(" ")]

    # 4 digit display output.
    output = ["", "", "", ""]
    remaining = []

    unique_segment_count = [0, 0, 0, 0, 0, 0, 0]

    # Create mapping of original segments to new segments.
    faulty = ["" for _ in segments]
    segment_to_faulty = lambda segment:segments.index(segment)

    # Check if each output is unique.
    for out_index, digit in enumerate(data_outputs):
        num_segments = size(digit)
        
        # Add unique number directly to output.
        if num_segments in unique_sizes:
            output[out_index] = size_to_number(num_segments)
            # Store which segments the unique number uses.
            for segment in digit:
                unique_segment_count[segment_to_faulty(segment)] += 1
            
        # Add none unique numbers to remainder.
        else:
            remaining.append((out_index, digit))

    # Fetch unique numbers from the input.
    for index, digit in enumerate(data_inputs):
        if size(digit) in unique_sizes:
            for segment in digit:
                unique_segment_count[segment_to_faulty(segment)] += 1
                data_inputs[index] = size_to_number(size(digit))

    cfpair = set()
    highest = max(unique_segment_count)
    # Find out which segments map to c and f.
    for index, value in enumerate(unique_segment_count):
        if value == highest:
            cfpair.add(segments[index])
        if len(cfpair) == 2:
            break
        
    print(f"C and F pair = {list(cfpair)}")
    
    # Find a 6 (to determine which of the cf pair maps to f).
    for index, digit in enumerate(data_inputs):
        # Skip checked values.
        if isinstance(digit, str):
            continue
        # Find a 6.
        if size(digit) == number_to_size("6"):
            c = cfpair.difference(digit)
            # A 6 has been found.
            if len(c) == 1:
                faulty[segment_to_faulty("c")] = c.pop()
                data_inputs[index] = "6"
    
    # Find a 2 and (a 3 or a 5) (to determine the mapping of e).
    twos = []
    threes = []
    fives = []
    for index, digit in enumerate(data_inputs):
        # Skip checked values.
        if isinstance(digit, str):
            continue

        if size(digit) == number_to_size("2"):
            # 2's only have the c segment.
            difference = cfpair.difference(digit)
            # Check for a 3.
            if size(difference) == 0:
                threes.append(digit)
                data_inputs[index] = "3"
            # Check for a 2.
            elif size(difference) > 0 and difference.pop() == faulty[segment_to_faulty("c")]:
                twos.append(digit)
                data_inputs[index] = "2"
            # 5 otherwise.
            else:
                fives.append(digit)
                data_inputs[index] = "5"
    two = twos[0]
    three_or_five = None
    if threes:
        three_or_five = threes[0]
    else:
        three_or_five = fives[0]

    # Find difference between them.
    
                
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

    print(output)
    total += int(output)
    
print(total)
    
