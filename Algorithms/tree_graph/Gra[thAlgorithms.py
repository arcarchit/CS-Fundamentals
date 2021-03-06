class Algorithms:

    def DFS(g, u, discovered):
        """ Perform DFS of undiscovered portion of Graph G, starting at index u.

        discovered is a dictionary that is used to map each vertex with the edge that
        was used to discover it during DFS.
        Newly added vertexes will be added to dictonary as a result.

        Sample call :
        result = {u : None}
        DFS(g, u, result)
        """

        for e in g.incindent_edges(u):
            v = u.opposite(u)
            if v not in discovered:
                discover[v] = e
                DFS(g, v, discovered)


    def construct_path(u, v, discoverd):
        """ To identify the path from u to v in DFS """

        path = []
        if v in discoverd:
            # We build a path from v to u and then reverse it in the end.
            path.append(v)
            walk = v
            while walk is not u:
                e = discoverd[walk]
                parent = e.opposite(walk)
                path.append(parent)
                parent = walk
            path.reverse()
            return path


    def DFS_complete(g):
        """ Perform DFS for the entore graph and return forest as the dictioanry.
        We want to find out connected components of the graph.

        The number of cinnected component can be determined by the number of vetexes in discovery
        dictionary that has None as their discovery edges.
        """

        forest = {}

        for u in g.verteices():
            if u not in forest:
                forest[u] = None
                DFS(g, u , forest)

        return forest

    def BFS(g, s, discovered):

        level = [s]

        while len(level) > 0:
            next_level = []
            for u in level :
                for e in g.incindent_edges(u):
                    v = e.opposite(u)
                    if v not in discoverd:
                        discovered[v] = e
                        next_level.append(v)
            level = next_level


    def floyd_warshall(g):
        """ return a new graph that is transitive closure og g """


        closure = deepcopy(g)
        verts = list(closure.verteices)
        n = len(verts)

        for k in range(n):
            for i in range(n):
                if i!=k and closure.get_edge(verts[i], verts[k]) is not None:
                    for j in range(n):
                        if i != j != k and closure.get_edge(verts[j], verts[k]) is not None:
                            if closure.get_edge(verts[i], verts[j]) is not None:
                                closure.insert_edge(verts[i], verts[j])
        return closure
