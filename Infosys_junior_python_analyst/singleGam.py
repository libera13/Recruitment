from random import randint
from matplotlib import pyplot as plt

i = 0
move = 0
actualFloor = 0
xThrows = []
yFloor = []
while i < 100:
    i += 1
    resultDice = randint(1, 6)
    if resultDice == 1 or resultDice == 2:
        if actualFloor == 0:
            move = 0
        else:
            move = -1
    elif resultDice == 3 or resultDice == 4 or resultDice == 5:
        move = 1
    else:
        move = randint(1, 6)
    if actualFloor + move >= 101: actualFloor = 101
    else: actualFloor += move
    xThrows.append(i)
    yFloor.append(actualFloor)
if actualFloor >= 80: print("You win")
plt.title("Single game")
plt.xlabel("Throws")
plt.ylabel("Floors")
plt.plot(xThrows, yFloor)
plt.show()
