# coding: utf-8
from builtins import int
from random import randrange
from typing import Tuple, List

import math
import matplotlib.pyplot as plt


class RenderableBody:
    x_coordinate = 0.0
    y_coordinate = 0.0

    def __init__(self, mass: int):
        self.mass = mass

    def get_coordinates(self) -> Tuple[float, float]:
        return self.x_coordinate, self.y_coordinate


class RenderableUniverse:
    def __init__(self, bodies: List[RenderableBody]):
        self.bodies = bodies

    def get_x_limits(self) -> Tuple[int, int]:
        return -255, 255

    def get_y_limits(self) -> Tuple[int, int]:
        return -255, 255

    def get_bodies(self) -> List[RenderableBody]:
        return self.bodies

    def step(self):
        for body in bodies:
            body.x_coordinate = body.x_coordinate + randrange(-24, 25)
            body.y_coordinate = body.y_coordinate + randrange(-24, 25)


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

        # Enable the most important feature of matplotlib
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
        # cache the _background
        self._background = self._fig.canvas.copy_from_bbox(self._ax.bbox)

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
        self.universe.step()

        # restore _background
        # self._fig.canvas.restore_region(self._background)

        self._background = self._fig.canvas.copy_from_bbox(self._ax.bbox)

        # Update The Dots
        for i in range(len(self.universe.bodies)):
            dot = self._body_dots[i][0]
            body = self.universe.bodies[i]
            trailing_line = self._body_trailing_lines[i][0]

            old_ydata = dot.get_ydata()
            old_xdata = dot.get_xdata()
            ydata = [body.y_coordinate]
            xdata = [body.x_coordinate]
            dot.set_ydata(ydata)
            dot.set_xdata(xdata)

            # redraw just the points
            self._ax.draw_artist(dot)

            # Update the trailing line
            trailing_line.set_xdata([old_xdata, xdata])
            trailing_line.set_ydata([old_ydata, ydata])

        # fill in the axes rectangle
        self._fig.canvas.blit(self._ax.bbox)


if __name__ == '__main__':
    bodies = [RenderableBody(10000 * i) for i in range(2)]
    universe = RenderableUniverse(bodies)
    renderer = UniverseRenderer(universe)
    renderer.run()
