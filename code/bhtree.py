from body import Body
from quad import Quad


class BHTree:
    body: Body
    nw: 'BHTree'
    ne: 'BHTree'
    sw: 'BHTree'
    se: 'BHTree'

    def __init__(self, quad: Quad):
        self.quad = quad

    def is_external(self, t: 'BHTree') -> bool:
        """
        If all nodes of the BHTree are null, then the quadrant represents a single body and
        it is "external" or a leaf of the tree
        """
        return t.nw is None and t.ne is None and t.sw is None and t.se is None

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
        elif not self.is_external(self):
            b.add_force(self.body)

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

        # If the node is external and contains another body, create BHTrees
        # where the bodies should go, update the node, and end
        # (do not do anything recursively)
        elif self.is_external(self):
            c = self.body
            northwest = self.quad.NW()
            if c.is_in(northwest):
                if self.nw is None:
                    self.nw = BHTree(northwest)
            northeast = self.quad.NE()
            if c.is_in(northeast):
                if self.ne is None:
                    self.ne = BHTree(northeast)
            southwest = self.quad.SW()
            if c.is_in(southwest):
                if self.sw is None:
                    self.sw = BHTree(southwest)
            southeast = self.quad.SE()
            if c.is_in(southeast):
                if self.se is None:
                    self.se = BHTree(southeast)

            # TODO: How is this recursive?
            self.insert(b)

        







