# coding: utf-8
from builtins import int
from typing import Tuple, List

import math
import matplotlib.pyplot as plt
import time

from body import Body
from universe import BruteForceUniverse

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


class RenderableUniverse:
    def get_x_limits(self) -> Tuple[int, int]:
        raise NotImplementedError

    def get_y_limits(self) -> Tuple[int, int]:
        raise NotImplementedError

    def get_bodies(self) -> List[Body]:
        raise NotImplementedError

    def step(self):
        raise NotImplementedError


class UniverseRenderer:
    mass_display_multiplicator = 0.002

    _background = None
    _body_dots = []
    _body_trailing_lines = []

    def __init__(self, universe: RenderableUniverse):
        self.universe = universe

        self._fig, self._ax = plt.subplots(1, 1)
        self._ax.set_aspect('equal')
        self._ax.set_xlim(*self.universe.get_x_limits())
        self._ax.set_ylim(*self.universe.get_y_limits())

        # Uncomment in case we dont want to show the axes
        plt.axis('off')

        # Uncomment to enable the most important feature of matplotlib
        # plt.xkcd()

        # Setup Dots and Lines
        for body in self.universe.get_bodies():
            marker_size = max(math.floor(body.mass * self.mass_display_multiplicator), 8)
            coordinates = body.get_coordinates()
            dot = plt.plot(coordinates[0], coordinates[1], 'o', markersize=marker_size)
            self._body_dots.append(dot)

            trailing_line = plt.plot([0, 0], [0, 0], dot[0].get_color())
            trailing_line[0].set_dashes([2, 1])
            self._body_trailing_lines.append(trailing_line)

    def run(self):
        print("Go")

        # Render
        plt.ion()
        plt.show(False)
        plt.draw()

        try:
            while True:
                self.step()
                plt.pause(0.0001)
        except KeyboardInterrupt:
            print("\nbye 🚀")
            exit(0)

    def step(self):
        # Run Universe step
        start_time = time.process_time()
        self.universe.step()
        seconds_per_frame = time.process_time() - start_time
        print(CURSOR_UP_ONE + ERASE_LINE)
        print('{:.2f} FPS'.format(1/seconds_per_frame), end='', flush=True)


        # Update The Dots
        for i in range(len(self.universe.bodies)):
            dot = self._body_dots[i][0]
            body = self.universe.get_bodies()[i]
            trailing_line = self._body_trailing_lines[i][0]

            old_xdata = dot.get_xdata()
            old_ydata = dot.get_ydata()
            xdata = [body.rx]
            ydata = [body.ry]

            # Update the Dot
            dot.set_xdata(xdata)
            dot.set_ydata(ydata)

            # Update the trailing line
            trailing_line.set_xdata([old_xdata, xdata])
            trailing_line.set_ydata([old_ydata, ydata])


class RenderableBruteForceUniverse(BruteForceUniverse, RenderableUniverse):
    def get_x_limits(self):
        return -self.radius, self.radius

    def get_y_limits(self):
        return -self.radius, self.radius

    def get_bodies(self):
        return self.bodies

    def step(self):
        self.calculate()


if __name__ == '__main__':
    universe = RenderableBruteForceUniverse()
    renderer = UniverseRenderer(universe)
    renderer.run()
