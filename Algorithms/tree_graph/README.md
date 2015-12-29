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
