from math import sqrt, exp, atan, pi, cos, copysign, sin, log
from random import random

from bhtree import BHTree
from body import Body
from quad import Quad


class Universe:
    """A container for orbital dynamics simulations"""
    bodies: [Body] = []
    solar_mass = 1.98892e30
    radius = 1e18  # the radius of the universe!!

    @property
    def n(self):
        return len(self.bodies)

    def __init__(self):
        pass

    def calculate(self):
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
        """Override this method in your subclass"""
        raise NotImplementedError

    def exp(self, lmbda):
        """
        A function to return an exponential distribution for position
        """
        return -log(1 - random()) / lmbda


class BruteForceUniverse(Universe):
    """
    Naive implementation of orbital dynamics
    """
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


class BarnesHutUniverse(Universe):
    """
    Universe that uses a Barnes-Hut tree to calculte orbital dynamics
    """
    quad = Quad(0, 0, 2*1e18)

    def add_forces(self, n):
        the_tree = BHTree(self.quad)

        # If the body is still on the screen, add it to the tree
        for body in self.bodies:
            if body.is_in(self.quad):
                the_tree.insert(body)

        # Now, use out methods in BHTree to update the forces,
        # traveling recursively through the tree
        for body in self.bodies:
            body.reset_force()
            if body.is_in(self.quad):
                the_tree.update_force(body)
                # Calculate the new positions on a time step dt (1e11 here)
                body.update(1e11)