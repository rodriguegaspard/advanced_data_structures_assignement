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

    def addChildren(self, kid):
        kid.parent = self
        position = 0
        if self.isLeafNode():
            self.children.append(kid)
        else:
            for child in self.children:
                if min(kid.keys) >= min(child.keys):
                    position = position + 1
            self.children.insert(position, kid)

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

    def printUMLNode(self):
        if self.isRootNode():
            print("object root")
            print("root : keys = [", end="")
            for key in self.keys[:-1]:
                  print(str(key), end=",")
            print(str(self.keys[-1]) + "]")
            for child in self.children:
                  print("root --> n" + str(child.id))
        else:
            print("n" + str(self.id) + " : keys = [", end="")
            for key in self.keys[:-1]:
                  print(str(key), end=",")
            print(str(self.keys[-1]) + "]")
            for child in self.children:
                  print("n" + str(self.id) + " --> n" + str(child.id))
        for child in self.children:
            child.printUMLNode()

    def printUML(self):
        print("@startuml")
        print("hide circle")
        self.printUMLNode()
        print("@enduml")

    def searchNode(self, value):
        for key in self.keys:
            if (key == value):
                return True
        return False

    def locateNeighbourKey(self, value):
        return None
    
    def delete(self, value):
        if self.isLeafNode():
            if self.searchNode(value):
                self.keys.remove(value)
                return
        else:
            if self.searchNode(value):
                return

root = BTreeNode([1,10], [], None, 3)
#root.insert(7)
#root.insert(2)
#root.insert(11)
#root.insert(6)
#root.insert(13)
#root.insert(9)
#root.insert(14)
#root.insert(5)
#root.insert(4)
#root.insert(8)
#root.insert(12)
root.printUML()
