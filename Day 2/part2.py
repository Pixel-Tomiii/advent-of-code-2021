aim = 0
depth = 0
forward = 0

with open("input.txt") as commands:
    # Split up commands.
    for row in commands:
        command, value = row.rstrip().split()
        value = int(value)

        # Handle commands.
        if command == "forward":
            forward += value
            depth += (value * aim)
            
        elif command == "down":
            aim += value

        elif command == "up":
            aim -= value

print(forward * depth)
