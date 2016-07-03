from copy import deepcopy;

print "hello one "

class Graph:
    """representaion of a simple graph using adjancy map
    This has two attributes namely outgoing and incoming, both are dictionaries.
    self._ougoing[u][v] = e (edge from u to v)
    self._incoming[a][b] = c (edge from b to a)
    so this is nested dictioanry. Passing vertexed to _outgoing return dictionary of all the adjacen vertexes as key
    and corresponding edge as value.
    """
    def __init__(self, directed = False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._outgoing is not self._incoming

    def vetex_count(self):
        return len(self._outgoing)

    def verteices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum (len (self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total//2

    def edges(self):
        result = set() #set avoids duplication in undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self , u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing = True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incindent_edges(self, v, outgoing = True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x= None):
        """ insert and return a new vertex with element x"""
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x= None):
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e


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
