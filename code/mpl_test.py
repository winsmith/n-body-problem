# coding: utf-8
from random import randrange

import matplotlib.pyplot as plt

# Configuration
plt.xkcd()
fig, ax = plt.subplots(1, 1)
ax.set_aspect('equal')
ax.set_xlim(-255, 255)
ax.set_ylim(-255, 255)
# In case we dont want to show axis dots
# plt.axis('off')

# Setup
dots = [plt.plot(0, 0, 'o', markersize=3.5 * i) for i in range(10)]

# cache the background
background = fig.canvas.copy_from_bbox(ax.bbox)

# Render
plt.ion()
plt.show(False)
plt.draw()
for _ in range(200):
    # restore background
    fig.canvas.restore_region(background)

    # Update The Dot
    for dotdata in dots:
        dot = dotdata[0]
        old_ydata = dot.get_ydata()
        old_xdata = dot.get_xdata()
        ydata = [value + randrange(-19, 20) for value in old_ydata]
        xdata = [value + randrange(-19, 20) for value in old_xdata]
        dot.set_ydata(ydata)
        dot.set_xdata(xdata)
        # redraw just the points
        ax.draw_artist(dot)

        # Update the trailing line
        trailing_line = plt.plot([old_xdata, xdata], [old_ydata, ydata], dot.get_color())
        trailing_line[0].set_dashes([2, 1])

    # fill in the axes rectangle
    fig.canvas.blit(ax.bbox)

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