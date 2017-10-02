class Quad:
    """
    A quadrant object that can self-subdivide. Important for creating a two-dimensional Barnes-Hut
    tree, since it  holds quadrants.
    """
    def __init__(self, xmid: float, ymid: float, length: float):
        self.xmid = xmid
        self.ymid = ymid
        self.length = length

    def contains(self, xmid, ymid):
        """
        Check if this Quadrant contains a point
        """
        if (xmid <= self.xmid + self.length/2.0) and \
           (xmid >= self.xmid - self.length/2.0) and \
           (ymid <= self.ymid + self.length/2.0) and \
           (ymid >= self.ymid - self.length/2.0):
            return True
        return False

    def NW(self) -> 'Quad':
        return Quad(self.xmid-self.length/4.0, self.ymid+self.length/4.0, self.length/2.0)

    def NE(self) -> 'Quad':
        return Quad(self.xmid+self.length/4.0, self.ymid+self.length/4.0, self.length/2.0)

    def SW(self) -> 'Quad':
        return Quad(self.xmid-self.length/4.0, self.ymid-self.length/4.0, self.length/2.0)

    def SE(self) -> 'Quad':
        return Quad(self.xmid+self.length/4.0, self.ymid-self.length/4.0, self.length/2.0)
