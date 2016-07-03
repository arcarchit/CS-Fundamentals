class Vertex:
    """ simple vetex clas
    This vertex has one attribute named _element.
    Having hash function will allow it to be a key of map/set """
    
    __slots__ = '_element'

    def __init__(self, X):
        self._element = x

    def element(self):
        return self._element

    def __hash__(self):
        return hash(id(self))
