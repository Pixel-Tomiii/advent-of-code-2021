from copy import deepcopy

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

def calc_score(board, call):
    total = 0
    for row in board:
        for item in row:
            if not item.endswith("X"):
                total += int(item)
    total *= int(call)
    print("FINAL SCORE:", total)
        
# PART 2 START
numbers = data.pop(0).split(",")
print(numbers)

# Create boards.
boards = []
last_winner = None
call_was = None

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
                    break
        # Calculate            
        if len(board) == 5 and check_winner(board):
            last_winner = deepcopy(board)
            call_was = call
            board.append("WINNER")


for row in last_winner:
    for item in row:
        print(item, end=" ")
    print()
print()
print("CALL",call_was)
calc_score(last_winner, call_was)




            
            
