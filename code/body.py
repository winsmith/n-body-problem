from math import sqrt

G = 6.673e-11  # gravitational constant


class Body:
    # cartesian positions
    rx: float
    ry: float

    # velocity components
    vx: float
    vy: float

    # force components
    fx: float = 0.0
    fy: float = 0.0

    mass: float

    def __init__(self, rx: float, ry: float,
                 vx: float, vy: float,
                 mass: float):
        self.rx = rx
        self.ry = ry
        self.vx = vx
        self.vy = vy
        self.mass = mass

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(
            self.rx, self.ry, self.vx, self.vy, self.mass
        )

    def update(self, dt: float):
        """
        Update the velocity and position using a time step dt
        """
        self.vx += dt * self.fx / self.mass
        self.vy += dt * self.fy / self.mass
        self.rx += dt * self.vx
        self.ry += dt * self.vy

    def distance_to(self, other_body: 'Body') -> float:
        """'
        Return the distance between two bodies
        """
        dx = self.rx - other_body.rx
        dy = self.ry - other_body.ry
        return sqrt(dx*dx + dy*dy)

    def reset_force(self):
        """
        Reset the force to 0 for the next iteration
        """
        self.fx = 0.0
        self.fy = 0.0

    def add_force(self, other_body: 'Body'):
        """
        Compute the net force acting between this body and
        other_body and add to the net force acting on this
        body
        """
        # softening parameter (just to avoid infinities)
        eps = 3E4
        dx = other_body.rx - self.rx
        dy = other_body.ry - self.ry
        dist = sqrt(dx*dx + dy*dy)
        F = (G * self.mass * other_body.mass) / (dist*dist + eps*eps)
        self.fx = self.fx + F * dx / dist
        self.fy = self.fy + F * dy / dist

    def is_in(self, quad: 'Quad'):
        return quad.contains(self.rx, self.ry)


