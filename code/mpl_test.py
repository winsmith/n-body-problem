# coding: utf-8
from random import randrange
from typing import Tuple, List

from builtins import int

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
    body_dots = []
    mass_display_multiplicator = 0.002

    def __init__(self, universe: RenderableUniverse):
        self.universe = universe

        self.fig, self.ax = plt.subplots(1, 1)
        self.ax.set_aspect('equal')
        self.ax.set_xlim(*self.universe.get_x_limits())
        self.ax.set_ylim(*self.universe.get_y_limits())

        # Uncomment in case we dont want to show the axes
        # plt.axis('off')

        # Enable the most important feature of matplotlib
        # plt.xkcd()

        # Cache the Background
        self.background = self.fig.canvas.copy_from_bbox(self.ax.bbox)

        # Setup Dots
        for body in self.universe.get_bodies():
            marker_size = body.mass * self.mass_display_multiplicator
            coordinates = body.get_coordinates()
            self.body_dots.append(plt.plot(coordinates[0], coordinates[1], 'o', marker_size))

    def run(self):
        # cache the background
        self.background = self.fig.canvas.copy_from_bbox(self.ax.bbox)

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

        # restore background
        self.fig.canvas.restore_region(self.background)

        # Update The Dots
        for i in range(len(self.universe.bodies)):
            dotdata = self.body_dots[i]
            body = self.universe.bodies[i]
            dot = dotdata[0]
            old_ydata = dot.get_ydata()
            old_xdata = dot.get_xdata()
            ydata = [body.y_coordinate]
            xdata = [body.x_coordinate]
            dot.set_ydata(ydata)
            dot.set_xdata(xdata)

            # redraw just the points
            self.ax.draw_artist(dot)

            # Update the trailing line
            trailing_line = plt.plot([old_xdata, xdata], [old_ydata, ydata], dot.get_color())
            trailing_line[0].set_dashes([2, 1])

        # fill in the axes rectangle
        self.fig.canvas.blit(self.ax.bbox)


if __name__ == '__main__':
    bodies = [RenderableBody(10000 * i) for i in range(10)]
    universe = RenderableUniverse(bodies)
    renderer = UniverseRenderer(universe)
    renderer.run()