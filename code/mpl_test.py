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

# Show results for a second before exiting
plt.pause(1.0)

# uncomment to keep on screen
# plt.ioff()
# plt.show()
