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

    while x < x2 and y > y2 and not(xVel == 0 and not x1 <= x <= x2):
        x += xVel
        y += yVel
        
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True

        yVel -= 1
        xVel -= 1 if xVel > 0 else 0
    return False


min_x_updates = calculateMinMaxXVel(x1, x2)
max_y = -math.inf

for initialX in range(20, x2):
    for initialY in range(100, y2, -1):
        if withinTarget(initialX, initialY, x1, x2, y1, y2):
            total = 0
            while initialY > 0:
                total += initialY
                initialY -= 1

            if max_y < total:
                max_y = total
result(max_y)
    
