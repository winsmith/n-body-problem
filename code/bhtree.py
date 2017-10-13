from body import Body
from quad import Quad


class BHTree:
    body: Body = None
    nw: 'BHTree' = None
    ne: 'BHTree' = None
    sw: 'BHTree' = None
    se: 'BHTree' = None

    def __init__(self, quad: Quad):
        self.quad = quad

    def is_leaf(self) -> bool:
        """
        If all nodes of the BHTree are null, then the quadrant represents a single body and
        it is "external" or a leaf of the tree
        """
        return self.nw is None and self.ne is None and self.sw is None and self.se is None

    def insert(self, b: Body):
        """
        We have to populate the tree with bodies. We start at the current tree and
        recursively travel through the branches
        """
        # If there's not a b there already, put the b there.
        if not self.body:
            self.body = b

        # If there's already a body there, but it's not an external node
        # combine the two bodies and figure out which quadrant of the
        # tree it should be located in. Then recursively update the nodes below
        elif not self.is_leaf():
            # In this case, this means "add the acting forces together
            b.accelerate(self.body)

            northwest = self.quad.NW()
            if b.is_in(northwest):
                if self.nw is None:
                    self.nw = BHTree(northwest)
                self.nw.insert(b)
                return

            northeast = self.quad.NE()
            if b.is_in(northeast):
                if self.ne is None:
                    self.ne = BHTree(northeast)
                self.ne.insert(b)
                return

            southeast = self.quad.SE()
            if b.is_in(southeast):
                if self.se is None:
                    self.se = BHTree(northeast)
                self.se.insert(b)
                return

            southwest = self.quad.SW()
            if b.is_in(southwest):
                if self.sw is None:
                    self.sw = BHTree(southwest)
                self.sw.insert(b)
                return

        # If the node is a leaf and contains another body, create BHTrees
        # where the bodies should go, update the node, and end
        # (do not do anything recursively)
        else:
            c = self.body
            northwest = self.quad.NW()
            if c.is_in(northwest):
                if self.nw is None:
                    self.nw = BHTree(northwest)
                self.insert(c)
            northeast = self.quad.NE()
            if c.is_in(northeast):
                if self.ne is None:
                    self.ne = BHTree(northeast)
                self.insert(c)
            southwest = self.quad.SW()
            if c.is_in(southwest):
                if self.sw is None:
                    self.sw = BHTree(southwest)
                self.insert(c)
            southeast = self.quad.SE()
            if c.is_in(southeast):
                if self.se is None:
                    self.se = BHTree(southeast)
                self.insert(c)

    def update_force(self, b: Body):
        """
        Start at the main node of the tree. Then, recursively go each branch
        Until either we reach an leaf node or we reach a node that is sufficiently
        far away that the external nodes would not matter much.
        """

        if self.is_leaf():
            b.accelerate(self.body)
        elif self.body != b and self.quad.diameter / self.body.distance_to(b) < 2:
            # This check is not in the original paper, but it prevents a division by zero
            b.accelerate(self.body)
        else:
            for quadrant in [self.nw, self.ne, self.sw, self.se]:
                if quadrant is not None:
                    quadrant.update_force(b)

    def __str__(self):
        if self.ne is None or self.nw is None or self.se is None or self.sw is None:
            return f'* {self.body}\n{self.nw}{self.ne}{self.sw}{self.se}'
        else:
            return f'  {self.body}\n'







