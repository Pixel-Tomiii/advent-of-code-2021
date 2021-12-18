import math

def get_data():
    """Opens a text file called "input.txt" and reads all the data into a list.

    Returns:
    A list object containing each line in "input.txt"
    """
    with open("input.txt") as file:
        lines = [line.rstrip() for line in file if line.rstrip() != ""]
    return lines
  
def result(result):
    """Displays the result"""
    print(f"Result found: {result}")

inp = get_data()[0]
pos1, pos2 = inp.removeprefix("target area: ").replace("x=", "").replace("y=", "").split(", ")
x1, x2 = map(int, pos1.split(".."))
y1, y2 = map(int, pos2.split(".."))

xVel, yVel = 0, 0
x, y = 0, 0

def calculateMinMaxXVel(x1, x2):
    initial1 = round(math.sqrt(2 * x1))
    initial2 = int(math.sqrt(2 * x2))
    return initial1, initial2

def withinTarget(intialX, initialY, x1, x2, y1, y2):
    xVel = initialX
    yVel = initialY
    x, y = 0, 0

    while x <= x2 and y >= y1 and not(xVel == 0 and not x1 <= x <= x2):
        x += xVel
        y += yVel
        
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True

        yVel -= 1
        xVel -= 1 if xVel > 0 else 0
        
    return False

"""23,-10  25,-9   27,-5   29,-6   22,-6   21,-7   9,0     27,-7   24,-5
25,-7   26,-6   25,-5   6,8     11,-2   20,-5   29,-10  6,3     28,-7
8,0     30,-6   29,-8   20,-10  6,7     6,4     6,1     14,-4   21,-6
26,-10  7,-1    7,7     8,-1    21,-9   6,2     20,-7   30,-10  14,-3
20,-8   13,-2   7,3     28,-8   29,-9   15,-3   22,-5   26,-8   25,-8
25,-6   15,-4   9,-2    15,-2   12,-2   28,-9   12,-3   24,-6   23,-7
25,-10  7,8     11,-3   26,-7   7,1     23,-9   6,0     22,-10  27,-6
8,1     22,-8   13,-4   7,6     28,-6   11,-4   12,-4   26,-9   7,4
24,-10  23,-8   30,-8   7,0     9,-1    10,-1   26,-5   22,-9   6,5
7,5     23,-6   28,-10  10,-2   11,-1   20,-9           29,-7   13,-3
23,-5   24,-8   27,-9   30,-7   28,-5   21,-10  7,9     6,6     21,-5
27,-10  7,2     30,-9   21,-8   22,-7   24,-9   20,-6   6,9     29,-5
8,-2    27,-8   30,-5   24,-7"""

min_x_updates = calculateMinMaxXVel(x1, x2)
initials = set()

for initialX in range(0, x2+1):
    for initialY in range(100, y1-1, -1):
        if withinTarget(initialX, initialY, x1, x2, y1, y2):
            initials.add((initialX, initialY))
            
print(initials)
result(len(initials))
    
