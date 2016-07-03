class Edge:
    """ Edge has three attributes, origin, destination and element
    I still don't know the purpose of element here. """
    
    __slots__ = '_origin', '_destination', '_element'

    def __init__(self, u, v, x):
        self._origin = u
        self._destination = v
        self._element = x

    def endpoints(self):
        return (self._origin, self._destination)

    def opposite(self, v):
        return self._origin if v is self._destination else self._destination

    def element(self):
        return self._element

    def __hash__(self):
        return hash((self._origin, self._destination)
