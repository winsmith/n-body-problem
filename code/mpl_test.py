from random import randrange

import matplotlib.pyplot as plt

plt.xkcd()
plt.ion()
for _ in range(20):
    plt.plot([randrange(-200, 200), randrange(-200, 200)])
    plt.pause(0.0001)

# Show results for a second before exiting
plt.pause(1.0)

# uncomment to keep on screen
# plt.ioff()
# plt.show()
