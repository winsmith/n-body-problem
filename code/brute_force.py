from math import sqrt, exp, atan, pi, cos, copysign, sin, log
from random import random

from body import Body


class BruteForceUniverse:
    """Naive implementation of orbital dynamics"""
    n = 100
    bodies: [Body] = []
    should_run = False
    solar_mass = 1.98892e30
    radius = 1e18  # the radius of the universe!!

    def __init__(self):
        pass

    def stop(self):
        self.should_run = False

    def calculate(self):
        if not self.should_run:
            return
        self.add_forces(self.n)

    def circular_velocity(self, rx: float, ry: float) -> float:
        """
        the bodies are initialized in circular orbits around the central mass.
        This is just some physics to do that
        """
        r2 = sqrt(rx*rx + ry*ry)
        numerator = 6.67e-11 * 1e6 * self.solar_mass
        return sqrt(numerator/r2)

    def start_the_bodies(self, n: int):
        """
        Initialize N bodies with random positions and circular velocities
        """

        # Put something heavy into the center
        self.bodies.append(Body(0, 0, 0, 0, 1e6 * self.solar_mass))

        for i in range(n):
            px = 1e18 * exp(-1.8) * (.5-random())
            py = 1e18 * exp(-1.8) * (.5-random())
            magv = self.circular_velocity(px, py)

            absangle = atan(abs(py / px))
            thetav = pi / 2 - absangle
            phiv = random() * pi
            # https://finnaarupnielsen.wordpress.com/2011/05/18/where-is-the-sign-function-in-python/
            vx = -1 * copysign(1, py) * cos(thetav) * magv
            vy = copysign(1, px) * sin(thetav) * magv

            # Orient a random 2D circular orbit
            if random() <= 0.5:
                vx = -vx
                vy = -vy

            mass = random() * self.solar_mass * 10 + 1e20
            self.bodies.append(Body(px, py, vx, vy, mass))

    def add_forces(self, n):
        for body in self.bodies:
            body.reset_force()

            # uh, oh a loop inside a loop
            # This'll get us n^2 complexity
            for other_body in self.bodies:
                if other_body != body:
                    body.add_force(other_body)

        # Update the timestamps
        for body in self.bodies:
            body.update(1e11)

    def exp(self, lmbda):
        return -log(1 - random()) / lmbda

    def action(self, event, object):
        # TODO
        pass

