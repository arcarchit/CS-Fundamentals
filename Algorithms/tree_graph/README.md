Binary tree is any tree which has maximum two child.

Binary search tree has a property that left child is less than parent and right child is greater than parent.
This property of Binary Search tree tends to make it unbalanced if proper care is not taken while insertion/deletion. This proper care results in balanced trees like AVL, Red-Black Trees etc.


Binary Search Tree does not guarantee that payload at root is maximum or minimum. That is the property of Heaps. It can be max heap or min heap.

Heaps are generally used in priority queues. And in heap sort. Heap sort is available in sorting directory along with other sorting algorithms.

In order traversal of binary tree gives the sorted payload.

In order traversal of heaps does not give sorting. Constant removal of root does the sorting for heap.
Hence priority queue.

How to delete elements from Binary Search Tree?
If the element to be removed is leaf node or has one child then things are simpler.
But if it has two children then :
Find the node with minimum payload in right subtree. Place it where node is ti be removed.


TODO:
There are many interesting questions that DFS and BFS can answer.
For example DFS can answer questions like connected component, computing cycle, finding minimum spanning tree etc.
Transitive Closure and Floyd Warshall algorithms


Some graph vocabulary :
connected, strongly connected (in directed graph)
subgraph, spanning subgraph,
connected components,
forest, tree
spanning tree



How to check if graph is connected?
If after dfs each node is mark visited then graph is connected.
It is good implementation to build a dictionary key = node, value = edges

How to check if graph is strongly connected?
Two DFS searches. One with incoming edges and one with outgoing edges.


Defination of transitive closure :
The transitive closure of a directed graph G is itself a directed graph G∗ such that the
vertices of G∗ are the same as the vertices of G, and G∗ has an edge (u,v), whenever
G has a directed path from u to v (including the case where (u,v) is an edge of
the original G).

This quickly allows us to answer questions like whether u and v are connected or not.
Floyd Washall is one of the algorithms to compute transitive closure.


DAG = Directed acyclic path


DFS, BFS and Dijkrat's Algorithm:
Dijkrat's algorithms is more sophisticted flavour of BFS.
BFS can be used to find shortest path if graph is not weighted or all the edges have equal weight.
For finding shortest path we need to maintain two things for each node :
	Distance from source
	Prevous node
DFS is easy to implement, just like tree traversal.
While BFS is more complecated, it requires to maintain a queue. While DFS does not require any queue or stack, just recurson will do

What changes should be done to make graph directed?
I guess while adding edge we should do it for one vertex only, the originator.


Making a non weighted graph weighted requires following :
In vertex class we store the neighbour vertexes for each node, now we need to store distance to this neghbour vetexes as well.
A naive approach would be to think weigh is a property of edge, not a vetex and we should create a new edge class.
But as I see in most of the cases we don't create Edge class just add a list of neighbour vetexes in Vertex class only.
