"""
Binary Search Tree:
    init
    minimum
    maximum
    search
    insert
    transplant
    delete

    We are making every node as if it is a tree.
    It supports all the methods like traversals, finding minimum/maximum etc.
    Then tree class will have just one attribute called root.

"""
class Node:
    def __init__(self, payload, left=None, right=None, parent=None):
        self.payload=payload
        self.left=left
        self.right=right
        self.parent=parent

    def __repr__(self, payload):
        return self.payload

    def search(self, data):
        node=self
        while node and node.payload != data:
            if data < node.payload:
                node=node.left
            else:
                node=node.right
        return node

    def print_in_order(self):
        if(self == None):
            return
        if self.left:
            self.left.print_in_order()
        print self.payload
        if self.right:
            self.right.print_in_order()

    def __str__(self, depth=0):
        return "work in progress"

    def in_order_walk(self):
        if self.left:
            for node in self.left.in_order_walk():
                yield node
        yield self
        if self.right:
            for node in self.right.in_order_walk():
                yield node

    def minimum(self):
        """return minimum node of self"""

        node = self
        while node.left is not None:
            node=node.left
        return node

    def maximum(self):
        node = self
        while node.right is not None:
            node = node.right
        return node


class BinaryTree:

    def __init__(self, root_payload=None):
        self.root=None
        if root_payload:
            self.root=Node(root_payload)


    def minimum(self):
        return self.root.minimum()

    def maximum(self):
        return self.root.maximum()

    def search(self, data):
        return self.root.search(data)

    def insert(self, payload):
        if self.root is None:
            self.root = Node(payload)
            return

        previous_node=None
        node=self.root
        while node is not None:
            previous_node=node
            if payload < node.payload:
                node=node.left
            else:
                node=node.right

        if previous_node is None:
            self.root=Node(payload)
        elif payload < previous_node.payload:
            previous_node.left=Node(payload, parent=previous_node)
        else:
            previous_node.right=Node(payload, parent=previous_node)

        return


    def transplant(self, node_to_be_removed, succesor):
        """
        what transplant does?
        it takes two arguments, node_to_be_removed and succesor
        It makes parent of node_to_be_removed to point to succesor
        """
        parent = node_to_be_removed.parent
        if parent.right is node_to_be_removed:
            parent.right = succesor
        else:
            parent.left = succesor

    def delete(self, item):
        # item can be payload or Node
        node_to_be_removed = self.root.search(item) if type(item) is not Node else item

        # Look at the class node. We are also saving parent for each node.

        if node_to_be_removed.left is None:
            succesor = node_to_be_removed.right
            self.transplant(node_to_be_removed, succesor)
        elif node_to_be_removed.right is None:
            succesor = node_to_be_removed.left
            self.transplant(node_to_be_removed, succesor)
        else:
            succesor = node_to_be_removed.right.minimum()
            self.transplant(succesor, None)
            # succesor would always be a leaf node
            succesor.right = node_to_be_removed.right
            succesor.left = node_to_be_removed.left
            succesor.left.parent = succesor
            succesor.right.parent = succesor
            self.transplant(node_to_be_removed, succesor)





print "starting with the execution\n"

btree = BinaryTree(12)
for i in [5, 18, 2, 9, 15, 19, 13, 17]:
    btree.insert(i)
btree.root.print_in_order()
print "after deletation of 13"
btree.delete(13)
btree.root.print_in_order()
print "\nexecution completes"
