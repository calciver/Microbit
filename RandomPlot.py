import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def createGraph(q):
    axisX = []
    axisY = []
    for i in range(1, 10):
        axisX.append(i)
        axisY.append(random.randint(1, 10))
    ax1.clear()
    ax1.plot(axisX, axisY)


ani = animation.FuncAnimation(fig, createGraph, interval=1000)
plt.show()
'''
for x in range(20):
  print random.randint(1,11)*5,

plt.plot([1, 2, 3], [5, 7, 4])  # plt.plot(x,y)

plt.show()
'''
'''
axisX = []
axisY = []
for i in range(1, 10):
    axisX.append(i)
    axisY.append(random.randint(1, 10))
    plt.plot(axisX, axisY)
    plt.show()
'''
