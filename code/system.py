from math import sqrt, exp, atan, pi, cos, copysign, sin, log
from random import random

from bhtree import BHTree
from body import Body
from quad import Quadrant


class System:
    """A container for orbital dynamics simulations"""
    bodies: [Body] = []
    solar_mass = 1.98892e30
    radius = 1e18  # the radius of the system
    time_warp_factor = 2e10

    def parent_body_color(self):
        return '#FDB813'

    @property
    def n(self):
        return len(self.bodies)

    def __init__(self):
        pass

    def calculate(self, elapsed_time):
        self.accelerate(self.n, elapsed_time)

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

        # Put some bodies around it
        for i in range(n):
            px = (self.radius + 1e8) * exp(-1.8)  * (.5-random())
            py = (self.radius + 1e8) * exp(-1.8) * (.5-random())
            magv = self.circular_velocity(px, py) * (0.7 + random() * 0.5)

            absangle = atan(abs(py / px))
            thetav = pi / 2 - absangle

            # https://finnaarupnielsen.wordpress.com/2011/05/18/where-is-the-sign-function-in-python/
            vx = -1 * copysign(1, py) * cos(thetav) * magv
            vy = copysign(1, px) * sin(thetav) * magv

            # Most objects should orbit in one direction, but there may be exceptions
            if random() <= 0.8:
                vx = -vx
                vy = -vy

            mass = random() * self.solar_mass * 30 + 1e20
            self.bodies.append(Body(px, py, vx, vy, mass))

    def accelerate(self, n, elapsed_time):
        """Override this method in your subclass"""
        raise NotImplementedError

    def exp(self, lmbda):
        """
        A function to return an exponential distribution for position
        """
        return -log(1 - random()) / lmbda


class BruteForceSystem(System):
    """
    Naive implementation of orbital dynamics
    """
    def accelerate(self, n, elapsed_time):
        for body in self.bodies:
            body.reset_force()

            # uh, oh a loop inside a loop
            # This'll get us n^2 complexity
            for other_body in self.bodies:
                if other_body != body:
                    body.accelerate(other_body)

        # Update the timestamps
        for body in self.bodies:
            body.update(elapsed_time)


class ApoapsisSystem(BruteForceSystem):
    def start_the_bodies(self, n: int):
        # Parent Body
        self.bodies.append(Body(0, 0, 0, 0, 1e6 * self.solar_mass))

        # Child body
        px = (self.radius + 1e8) * exp(-1.8) * (.5)
        py = (self.radius + 1e8) * exp(-1.8) * (.5)
        magv = self.circular_velocity(px, py) * 0.6

        absangle = atan(abs(py / px))
        thetav = pi / 2 - absangle

        # https://finnaarupnielsen.wordpress.com/2011/05/18/where-is-the-sign-function-in-python/
        vx = copysign(1, py) * cos(thetav) * magv
        vy = -1 * copysign(1, px) * sin(thetav) * magv

        mass = self.solar_mass * 1 + 1e20
        self.bodies.append(Body(px, py, vx, vy, mass))


class HohmannTransferSystemA(BruteForceSystem):
    time_warp_factor = 1e10
    radius = 4e17

    def start_the_bodies(self, n: int):
        # Parent Body
        self.bodies.append(Body(0, 0, 0, 0, 1e6 * self.solar_mass))

        # Child body
        px = self.radius/30
        py = self.radius/30
        magv = self.circular_velocity(px, py)

        absangle = atan(abs(py / px))
        thetav = pi / 2 - absangle

        # https://finnaarupnielsen.wordpress.com/2011/05/18/where-is-the-sign-function-in-python/
        vx = copysign(1, py) * cos(thetav) * magv
        vy = -1 * copysign(1, px) * sin(thetav) * magv

        mass = self.solar_mass * 10
        self.bodies.append(Body(px, py, vx, vy, mass))


class HohmannTransferSystemB(HohmannTransferSystemA):
    def start_the_bodies(self, n: int):
        # Parent Body
        self.bodies.append(Body(0, 0, 0, 0, 1e6 * self.solar_mass))

        # Child body
        px = self.radius/30
        py = self.radius/30
        magv = self.circular_velocity(px, py) * 1.2

        absangle = atan(abs(py / px))
        thetav = pi / 2 - absangle

        # https://finnaarupnielsen.wordpress.com/2011/05/18/where-is-the-sign-function-in-python/
        vx = copysign(1, py) * cos(thetav) * magv
        vy = -1 * copysign(1, px) * sin(thetav) * magv

        mass = self.solar_mass * 10
        self.bodies.append(Body(px, py, vx, vy, mass))


class HohmannTransferSystemC(HohmannTransferSystemA):
    def start_the_bodies(self, n: int):
        # Parent Body
        self.bodies.append(Body(0, 0, 0, 0, 1e6 * self.solar_mass))

        # Child body
        px = -4.331161870491374e+16
        py = -1.3449882048469356e+16
        magv = self.circular_velocity(px, py)

        absangle = atan(abs(py / px))
        thetav = pi / 2 - absangle

        # https://finnaarupnielsen.wordpress.com/2011/05/18/where-is-the-sign-function-in-python/
        vx = copysign(1, py) * cos(thetav) * magv
        vy = -1 * copysign(1, px) * sin(thetav) * magv

        mass = self.solar_mass * 10
        self.bodies.append(Body(px, py, vx, vy, mass))


class BarnesHutSystem(System):
    """
    System that uses a Barnes-Hut tree to calculte orbital dynamics
    """
    quad = Quadrant(0, 0, 2 * 1e18)

    def accelerate(self, n, elapsed_time):
        the_tree = BHTree(self.quad)

        # If the body is inside the current quad, add it to the tree
        for body in self.bodies:
            if body.is_in(self.quad):
                the_tree.insert(body)

        # Now, use our methods in BHTree to update the forces,
        # traveling recursively through the tree
        for body in self.bodies:
            body.reset_force()
            if body.is_in(self.quad):
                the_tree.update_force(body)
                # Calculate the new positions
                body.update(elapsed_time)
