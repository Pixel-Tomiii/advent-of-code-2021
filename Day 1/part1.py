from math import inf

# Read through the file.
with open ("input.txt") as depths:
    total_increased = 0
    previous = inf

    # Converting each depth to an int.
    for cur_depth in depths:
        cur_depth = int(cur_depth.rstrip())
        
        # Searching for depths that increased after the previous depth.
        if cur_depth > previous:
            total_increased += 1
        previous = cur_depth

    print(total_increased)
