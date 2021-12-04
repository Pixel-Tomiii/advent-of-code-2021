def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file]
    return lines

data = get_data()

def check_winner(board):
    winner = False
    # check row.
    for row in board:
        winner = True
        for item in row:
            if not item.endswith("X"):
                winner = False
                break
        if winner:
            return winner
    
    # check column
    for x in range(len(board)):
        winner = True
        for y in range(len(board)):
            if not board[y][x].endswith("X"):
                winner = False
                break
        if winner:
            return winner
    
    return winner
            
# PART 1 START
numbers = data.pop(0).split(",")
print(numbers)

# Create boards.
boards = []

for row in data:
    if not row:
        boards.append([])
    else:
        boards[-1].append([x for x in row.split(" ") if x])

for call in numbers:
    for board_num, board in enumerate(boards):
        for y, row in enumerate(board):
            for x, item in enumerate(row):
                if item == call:
                    board[y][x] = call + "X"
        # Calculate            
        if check_winner(board):
            # output winning board.
            for row in board:
                for item in row:
                    print(item, end=" ")
                print()
            print()
            print("FINAL CALL WAS:", call)
            total = 0
            for row in board:
                for item in row:
                    if not item.endswith("X"):
                        total += int(item)
            total *= int(call)
            print("FINAL SCORE:", total)             
            break
        
    else:
        continue

    break   




            
            
