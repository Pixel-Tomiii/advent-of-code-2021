def get_mode(binaries, *columns):
    """Finds the number of times 0 and 1 appear in each column of a binary
    number.
    
    Parameteres:
    binaries - A list of binary numbers, all of which are the same length.
    columns - Specify which columns to count the mode of.

    Returns:
    A dictionary containing the number of 0's
    and the number of 1's in each column of the binary
    numbers.

    Each key points to a list [x, y] where x is the number
    of 0s and y is the number of 1s.
    """
    mode = dict()
    # Adding the number of columns required.
    for index in (range(len(binaries[0])) if not columns else columns):
        mode[index] = [0, 0]

    # Calculating the mode.
    for binary in binaries:
        # Calculate mode of every digit.
        if not columns:
            for index, digit in enumerate(binary):
                mode[index][int(digit)] += 1
        # Calculate mode of every given column.
        else:
            for column in columns:
                mode[column][int(binary[column])] += 1
    return mode
                
def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines
            
def result(binaries, function):
    """Returns the value required for day 3 part 2.

    Parameters:
    binaries - A list of binary numbers, all of which are the same length.
    function - The function to determine whether the number in a specific
                column should be a 1 or a 0.

    Returns:
    The remaining binary number after the operation is complete."""
    column = 0
    while len(binaries) > 1:
        mode = get_mode(binaries, column)
        result = function(mode[column])
        # Remove not needed columns.
        new_binaries = []
        for number in binaries:
            if int(number[column]) == result:
                new_binaries.append(number)
        # Replace current set with new set.
        binaries = new_binaries
        column += 1
    return binaries[0]

# Convert binary numbers into a set.
lines = get_data()

oxygen = result(lines, lambda mode: 0 if mode[0] > mode[1] else 1)
co2 = result(lines, lambda mode: 1 if mode[0] > mode[1] else 0)

# Output the result of oxygen and co2.
# Also convert oxygen and co2 to integers from base 2.
print(f"Oxygen = {oxygen} -> {(oxygen:=int(oxygen, 2))}")
print(f"CO2    = {co2} -> {(co2:=int(co2, 2))}")

# Calculate Life support.
life = co2 * oxygen
print(f"Life   = {oxygen} x {co2}  -> {life}")
