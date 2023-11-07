# Implementation of a B-Tree (https://en.wikipedia.org/wiki/B-tree) and a Van Emde Boas Tree (https://en.wikipedia.org/wiki/Van_Emde_Boas_tree)
# Created by Rodrigue G.

import itertools

'''
A B-Tree of order m has these properties: 
1) Each node has at most m children 
2) All non-leaf nodes except root (internal nodes) must have at least m/2 children 
3) All nodes except root must have at least [m/2]-1 keys and a maximum of m-1 keys 
4) A root node can have a single key 
5) If the root node is a non-leaf node, then it must have at least 1 key and 2 children  
6) A non-leaf node with t-1 keys must have  t number of children. (The number of subtrees below a nonleaf node is always one more than the number of keys in the node) 
7) All the key values within a node must be in ascending order 
8) All leaf nodes must be at the same level. (Thus, it ensures that a B-Tree avoids the problem of unbalanced tree) 
'''

class BTreeNode:
    UNIQUE_ID = itertools.count()
    def __init__(self, keys, children, parent, order):
        self.parent = parent
        self.children = children
        self.keys = keys
        self.order = order
        self.id = next(self.UNIQUE_ID)

    def isRootNode(self):
        return not self.parent

    def isLeafNode(self):
        return not self.children

    def isFull(self):
        return len(self.keys) >= self.order - 1

    def addChildren(self, children):
        self.children.append(children)

    def deleteChildren(self, children):
        self.children.remove(children)

    def printTree(self):
        print("(" + str(self.id) + ")[", end="")
        for key in self.keys[:-1]:
            print(key, end=",")
        print(str(self.keys[-1]) + "]", end=" ")
        if not self.isLeafNode():
            print("|", end="")
            for children in self.children:
                print(str(children.id), end = "|")
            print()
            for children in self.children:
                children.printTree()

    def splitNode(self, key):
        #Split the node in two parts (left node and right node), and keep the median
        self.keys.append(key)
        self.keys = sorted(self.keys)
        median_index = len(self.keys) // 2
        leftNode, rightNode = BTreeNode(self.keys[:median_index], [], self.parent, self.order), BTreeNode(self.keys[median_index:], [], self.parent, self.order)
        self.keys = [self.keys[median_index]]
        self.addChildren(leftNode)
        self.addChildren(rightNode)

    def insert(self, key):
        if self.isFull():
            if self.isLeafNode():
                self.splitNode(key)
            else:
                suitable_child = 0
                for i in range(0, len(self.children)):
                    if (key >= min(self.children[i].keys)):
                        suitable_child = i
                self.children[suitable_child].insert(key)
        else:
            if self.isLeafNode():
                self.keys.append(key)
                self.keys = sorted(self.keys)
            else:
                suitable_child = 0
                for i in range(0, len(self.children)):
                    if (key >= min(self.children[i].keys)):
                        suitable_child = i
                self.children[suitable_child].insert(key)


root = BTreeNode([1,10], [], None, 4)
root.insert(7)
root.insert(2)
root.insert(11)
root.insert(6)
root.insert(9)
root.insert(13)
root.insert(1)
root.insert(5)
root.insert(4)
root.insert(8)
root.printTree()
