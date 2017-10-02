# coding: utf-8
from random import randrange

import matplotlib.pyplot as plt

# TODO: Check out blitting
# https://stackoverflow.com/a/15724978/54547

plt.xkcd()
plt.ion()
plt.xlim(-200, 200)
plt.ylim(-200, 200)

# In case we dont want to show axis dots
# plt.axis('off')
dots = [plt.plot(0, 0, 'o', markersize=3.5 * i) for i in range(10)]

for _ in range(200):
    # Update The Dot
    for dotdata in dots:
        dot = dotdata[0]
        old_ydata = dot.get_ydata()
        old_xdata = dot.get_xdata()
        ydata = [value + randrange(-9, 10) for value in old_ydata]
        xdata = [value + randrange(-9, 10) for value in old_xdata]
        dot.set_ydata(ydata)
        dot.set_xdata(xdata)

        # Update the trailing line
        plt.plot([old_xdata, xdata], [old_ydata, ydata], dot.get_color())
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
