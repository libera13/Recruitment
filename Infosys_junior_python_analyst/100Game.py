from random import randint
from matplotlib import pyplot as plt

i = 0
a = 0
move = 0
actualFloor = 0
xThrows = []
yFloors = []
while a < 100:
    a += 1
    while i < 100:
        i += 1
        result = randint(1, 6)
        if result == 1 or result == 2:
            if actualFloor == 0:
                move = 0
            else:
                move = -1
        elif result == 3 or result == 4 or result == 5:
            move = 1
        else:
            extra = randint(1, 6)
            move = extra
        if actualFloor + move >= 101:
            actualFloor = 101
        else:
            actualFloor += move
        xThrows.append(i)
        yFloors.append(actualFloor)
    print(actualFloor)
    actualFloor = 0
    i = 0
    plt.plot(xThrows, yFloors, linewidth=0.3)

plt.title("100 games")
plt.xlabel("Throws")
plt.ylabel("Floors")
plt.show()
