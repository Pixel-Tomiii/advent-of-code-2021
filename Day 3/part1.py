gamma = ""
epsilon = ""

mode = dict()

with open("input.txt") as file:
    # Calculate how many times a 1 or a 0 occurs in each column of the binary.
    for line in file:
        line = line.rstrip()
        for num, char in enumerate(line):
            # Create initial starting columns for each digit.
            if num not in mode:
                mode[num] = [0,0]
            # Add to the mode.
            if char == "1":
                mode[num][1] += 1
            else:
                mode[num][0] += 1

# Calculating gamma and epsilon.
# Gamma requires most common.
# Epsolin requires lease common.
key = 0
while key in mode:
    if mode[key][0] > mode[key][1]:
        gamma += "0"
        epsilon += "1"

    elif mode[key][0] < mode[key][1]:
        gamma += "1"
        epsilon += "0"

    key += 1
    
print("gamma",gamma)
print("epsilon",epsilon)

# Convertion of string binary to integer.
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

power = gamma * epsilon

print("\nPower",power)

