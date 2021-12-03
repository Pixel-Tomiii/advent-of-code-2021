forward = 0
depth = 0

with open("input.txt") as commands:
    # Read file, splitting each row into its command and value.
    for row in commands:
        command, value = row.rstrip().split()
        value = int(value)
        # Handle command.
        if command == "forward":
            forward += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value

print(forward * depth)
