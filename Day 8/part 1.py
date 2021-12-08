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

zero = "abcefg"
one = "cf"
two = "acdeg"
three = "acdfg"
four = "bcdf"
five = "abdfg"
six = "abdefg"
seven = "acf"
eight = "abcdefg"
nine = "abcdfg"

inputs = 10
delim = "|"
display = 4

unique = [len(one), len(four), len(seven), len(eight)]
total = 0

for line in data:
    data_inputs, data_outputs = line.split(delim)
    data_inputs = data_inputs.rstrip().split(" ")
    data_outputs = data_outputs.lstrip().split(" ")

##    for attempt in data_inputs:
##        if len(attempt) not in unique:
##            continue


    for output in data_outputs:
        if len(output) in unique:
            total += 1



print(total)


    
    
    
