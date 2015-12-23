import ast
from Queue import Queue

class node:
    node_count = 0
    def __init__(self,val):
        self.val = val
        self.left = 0;
        self.right = 0;
        node.node_count +=1
    def displayNode(self):
        print self.val
    def preOrder(self):
            self.displayNode()
            if self.left: 
                self.left.preOrder()
            if self.right:
                self.right.preOrder()
    def postOrder(self):
            if self.left: 
                self.left.preOrder()
            if self.right:
                self.right.preOrder()        
            self.displayNode()
    def inOrder(self):
            if self.left: 
                self.left.inOrder()
            self.displayNode()
            if self.right:
                self.right.inOrder()        
    def breadthFirstOrder(self):
        a = [self]
        while a:
            b = list()
            for n in a:
                print n.val
                if n.left: b.append(n.left)
                if n.right: b.append(n.right)
            a = b;
root = node(10)
root.left = node(15)
root.right = node(20)
root.left.left = node(21)
root.left.right = node(26)
root.left.left.right = node(31)
print "number of nodes: " + str(node.node_count)
print 'preOrder'
root.preOrder()
print 'postOrder'
root.postOrder()
print 'inOrder'
root.inOrder()
print 'BreadthFirstOrder'
root.breadthFirstOrder()
