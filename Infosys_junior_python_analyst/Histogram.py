from random import randint
from matplotlib import pyplot as plt

i = 0
a = 0
move = 0
actualFloor = 0
yFloorsScore = []
while a < 5000:
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
    print(actualFloor)
    yFloorsScore.append(actualFloor)
    actualFloor = 0
    i = 0

mean = sum(yFloorsScore)/len(yFloorsScore)
print(mean)

plt.title("5000 games")
plt.xlabel("Floors")
plt.ylabel("Games")
n, bins, patches = plt.hist(yFloorsScore, bins=30, histtype= 'step', align='mid')
plt.subplots_adjust(left=0.15)
plt.show()
