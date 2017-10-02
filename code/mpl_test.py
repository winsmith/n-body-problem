# coding: utf-8
from random import randrange

import matplotlib.pyplot as plt

# TODO: Check out blitting
# https://stackoverflow.com/a/15724978/54547

plt.xkcd()
plt.ion()
for _ in range(20):
    plt.plot([randrange(-200, 200), randrange(-200, 200)],
             [randrange(-200, 200), randrange(-200, 200)],
             'o')
    plt.pause(0.0001)

# Pause without quitting to keep showing the graph, but listen
# to KeyboardInterrupt signals to quit on Ctrl-C
print("Hit Ctrl-C to exit")
while True:
    try:
        plt.pause(0.5)
    except KeyboardInterrupt:
        print("\nbye 🚀")
        break

# uncomment to keep on screen
# plt.ioff()
# plt.show()
