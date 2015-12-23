import ast

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
        a = []
        a.append(self)
        while (len(a)!=0):
            k = a[0]
            k.displayNode()
            a.remove(k)
            #print k.val
            if k.left:
                a.append(k.left)
            if k.right:
                a.append(self.right)
            
root = node(10)
root.left = node(15)
root.right = node(20)
root.left.left = node(21)
root.left.right = node(26)
print "number of nodes: " + str(node.node_count)
print 'preOrder'
root.preOrder()
print 'postOrder'
root.postOrder()
print 'inOrder'
root.inOrder()
print 'BreadthFirstOrder'
root.breadthFirstOrder()
