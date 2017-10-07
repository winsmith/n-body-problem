# coding: utf-8
from builtins import int
from typing import Tuple, List

import argparse
import math
import matplotlib.pyplot as plt
import time

from body import Body
from universe import BruteForceUniverse, BarnesHutUniverse

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


class RenderableUniverse:
    def get_solar_mass(self) -> float:
        raise NotImplementedError

    def get_x_limits(self) -> Tuple[int, int]:
        raise NotImplementedError

    def get_y_limits(self) -> Tuple[int, int]:
        raise NotImplementedError

    def get_bodies(self) -> List[Body]:
        raise NotImplementedError

    def step(self, elapsed_time):
        raise NotImplementedError


class UniverseRenderer:
    min_marker_size = 1
    max_marker_size = 100
    time_warp_factor = 1e12

    _background = None
    _body_dots = []
    _body_trailing_lines = []

    __last_step_time = None
    @property
    def _last_step_time(self):
        if self.__last_step_time is None:
            self.__last_step_time = time.process_time()
        return self.__last_step_time

    def __init__(self, universe: RenderableUniverse, trail_size: int = 0):
        self.universe = universe
        self.trail_size = trail_size

        self._fig, self._ax = plt.subplots(1, 1, figsize=(18, 8))
        self._ax.set_aspect('equal')
        self._ax.set_xlim(*self.universe.get_x_limits())
        self._ax.set_ylim(*self.universe.get_y_limits())

        # Uncomment in case we dont want to show the axes
        plt.axis('off')

        # Uncomment to enable the most important feature of matplotlib
        # plt.xkcd()

        # Setup Dots and Lines
        for body in self.universe.get_bodies():
            marker_size = math.floor(body.mass / self.universe.get_solar_mass()) + 1
            marker_size = min(marker_size, self.max_marker_size)
            marker_size = max(marker_size, self.min_marker_size)
            dot = plt.plot(body.rx, body.ry, 'o', markersize=marker_size)

            if body == self.universe.get_bodies()[0]:
                # Special Case for the sun
                dot[0].set_color('#FDB813')

            self._body_dots.append(dot)

            trailing_lines = []
            for _ in range(self.trail_size):
                trailing_line = plt.plot([0, 0], [0, 0], dot[0].get_color())
                # trailing_line[0].set_dashes([2, 1])
                trailing_lines.append(trailing_line)
            self._body_trailing_lines.append(trailing_lines)

    def run(self):
        print("Go")

        # Render
        plt.show(False)

        try:
            while True:
                self.step()
                time_since_previous_frame = time.process_time() - self._last_step_time
                waiting_time = max(1/60 - time_since_previous_frame, 0.000000000001)
                plt.pause(waiting_time)

        except KeyboardInterrupt:
            print("\nbye 🚀")
            exit(0)

    def step(self):
        last_step_time = self._last_step_time
        self.__last_step_time = time.process_time()
        frame_step_time = (self._last_step_time - last_step_time) * self.time_warp_factor

        # Run Universe step
        start_time = time.process_time()
        self.universe.step(frame_step_time)
        universe_step_time = time.process_time()

        # Update The Dots
        for i in range(len(self.universe.get_bodies())):
            dot = self._body_dots[i][0]
            body = self.universe.get_bodies()[i]

            old_xdata = dot.get_xdata()
            old_ydata = dot.get_ydata()
            xdata = [body.rx]
            ydata = [body.ry]

            # Update the Dot
            dot.set_xdata(xdata)
            dot.set_ydata(ydata)

            # Update the trailing line
            if self.trail_size < 1:
                continue
            trailing_line = self._body_trailing_lines[i].pop()
            trailing_line[0].set_xdata([old_xdata, xdata])
            trailing_line[0].set_ydata([old_ydata, ydata])
            self._body_trailing_lines[i].insert(0, trailing_line)

        universe_seconds_per_frame = universe_step_time - start_time
        step_seconds_per_frame = time.process_time() - last_step_time

        print(CURSOR_UP_ONE + ERASE_LINE)
        print('{:0.2f} FPS (in theory)'.format(
            1/universe_seconds_per_frame
        ), end='', flush=True)


class RenderableBruteForceUniverse(BruteForceUniverse, RenderableUniverse):
    def get_solar_mass(self):
        return self.solar_mass

    def get_x_limits(self):
        return -self.radius/6, self.radius/6

    def get_y_limits(self):
        return -self.radius/12, self.radius/12

    def get_bodies(self):
        return self.bodies

    def step(self, elapsed_time):
        self.calculate(elapsed_time)


class RenderableBarnesHutUniverse(BarnesHutUniverse, RenderableUniverse):
    def get_solar_mass(self):
        return self.solar_mass

    def get_x_limits(self):
        return -self.radius/8, self.radius/8

    def get_y_limits(self):
        return -self.radius/8, self.radius/8

    def get_bodies(self):
        return self.bodies

    def step(self, elapsed_time):
        self.calculate(elapsed_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simulate N-Body Problem')
    parser.add_argument("simulation_type", help="BruteForce or BarnesHut")
    parser.add_argument("bodies", help="The number of bodies to simulate")
    parser.add_argument("trail_size", help="Display a trail of length x while rendering")
    args = parser.parse_args()

    universe = None
    if args.simulation_type == 'BarnesHut':
        universe = RenderableBarnesHutUniverse()
    elif args.simulation_type == 'BruteForce':
        universe = RenderableBruteForceUniverse()
    else:
        exit(1)

    universe.start_the_bodies(int(args.bodies))
    renderer = UniverseRenderer(universe, trail_size=int(args.trail_size))

    renderer.run()
