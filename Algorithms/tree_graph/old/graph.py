from collections import deque

"""
This is undirected, non-weighted graph currently.

How can we make this graph directed? By modifying addEdge method.
But then we mgith also look at the logic of BFS and DFS

How can we make this graph weighted?
next attribute of vertex can be tupple instead of list. Second attribute of tupple being the cost.

We will be creating graph with adjancy list here.
We will create following classes and methods
Vertex
AdjList - addVetex, addEdge, removeVertex, removeEdge, traverseBFS, traverseDFS, DFS
            shortestPath, printPath, isDAG, copyGraph, stronglyConnectedComponents
"""

class Vertex:
    def __init__(self, name):
        self.name = name
        self.next = [] # this is basically adjancy list maintainig all the vertice directly connected to this one
        self.visit = None
        self.dist = float('inf')
        self.predecessor = None


class AdjList:
    def __init__(self, directed = False):
        self.directed = directed
        self.vertexList = {} # dictionary maps vertecName -> vertexClass
        self.cycleExists = False

    def __iter__(self):
        return iter(self.vertexList.keys())

    def addVertex(self, vertex):
        if vertex in self:
            print "vetex already exists"
        self.vertexList[vertex] = Vertex(vertex)

    def addEdge(self, vertexFrom, vertexTo):
        # assumption : graph is not directed

        vertexFromList = self.vertexList[vertexFrom].next
        vertexToList = self.vertexList[vertexTo].next
        vertexFromList.append(self.vertexList[vertexTo])
        vertexToList.append(self.vertexList[vertexFrom])

    def removeVirtex(self, virtex_to_remove):
        # remove vertex from dictionary
        removed = self.vertexList.pop(virtex_to_remove)
        # remove all edges to this vertex
        for key, vertex in self.vertexList.items():
            if removed in vertex.next:
                vertex.next.remove(removed)
        return True

    def removeEdge(self, vertexFrom, vertexTo):
        self.vertexList[vertexFrom].next.remove(vertexTo)
        self.vertexList[vertexTo].next.remove(vertexFrom)
        return True

    def traverseBFS(self, source):
        # mark all vertex as not visited and distance infinite
        for key, vertex in self.vertexList.items():
            vertex.visit = None
            vertex.dist = float('inf')

        current_vertex = self.vertexList[source]
        current_vertex.visit = False
        current_vertex.dist = 0

        bfsQ = deque()
        bfsQ.append(current_vertex)

        current_vertex = bfsQ.popleft()
        while current_vertex:
            for vertex in current_vertex.next:
                if vertex.visit is None:
                    vertex.visit = False
                    vertex.dist = current_vertex.dist + 1
                    bfsQ.append(vertex)
            print "vertex ", current_vertex.name, " is at distance ", current_vertex.dist
            current_vertex.visit = True
            if len(bfsQ) !=0:
                current_vertex = bfsQ.popleft()
            else:
                current_vertex = None

        return True

    def recurrenceDFS(self, current_vertex):
        """ This is a utility function to be used by traverseDFS function """

        # visit current_vertex
        print "Vertex ", current_vertex.name, " is at distance ", current_vertex.dist
        current_vertex.visit = True
        for vertex in current_vertex.next:
            if vertex.visit is not True:
                vertex.dist = current_vertex.dist + 1
                self.recurrenceDFS(vertex)

    def traverseDFS(self, source):
        # mark all invisted and distance infinite
        for key, vertex in self.vertexList.items():
            vertex.dist = float('inf')
            vertex.visit = None

        sourceVertex = self.vertexList[source]
        sourceVertex.dist = 0
        self.recurrenceDFS(sourceVertex)




print "Execution Starts \n"

graph = AdjList()
graph.addVertex("Ahmedabad")
graph.addVertex("Pune")
graph.addVertex("Mumbai")
graph.addVertex("Delhi")
graph.addVertex("Chennai")
graph.addEdge("Ahmedabad", "Pune")
graph.addEdge("Ahmedabad", "Delhi")
graph.addEdge("Ahmedabad", "Chennai")
graph.addEdge("Mumbai", "Pune")
graph.addEdge("Delhi", "Mumbai")
graph.addEdge("Delhi", "Chennai")

print "Breath First Search \n"
graph.traverseBFS("Delhi")

print "\nDepth First Search \n"
graph.traverseDFS("Delhi")

print "\nExecution Ends"
