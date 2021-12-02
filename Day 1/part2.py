from math import inf

# Read through the file.
with open ("input.txt") as depths:
    total_increased = 0
    values = []
    previous_sum = inf

    for line_num, cur_depth in enumerate(depths):
        cur_depth = int(cur_depth.rstrip())
        # Adding initial values.
        if line_num < 2:
            values.insert(0, cur_depth)
            continue

        # insert to tail of queue.
        values.insert(0, cur_depth)

        # Calculate and compare new sum.
        new_sum = sum(values)
        if new_sum > previous_sum:
            total_increased += 1
        previous_sum = new_sum

        # Remove head of queue for new tail on next iteration. 
        values.pop()

    print(total_increased)
