from collections import deque
import commands
## Stack - > list with LIFO behavior
## Queue -> list with FIFO behavior 
## both implementations available in python list data struc. 

def cube(a): return a*a*a
def isOdd(a): return a%2==1 
def add(x,y): return x+y
def listFuncs():
    list_as_stack = [1, 2, 3, 4, 5, 6]
    list_as_stack.extend(list_as_stack)
    print list_as_stack.pop()#stack like behavior
    list_as_stack.remove(4)
    list_as_stack.insert(1, 8)
    list_as_stack.sort()
    a = commands.getoutput('mount -v').splitlines()
    n = -8
    n1 = 8 
    print (bin(n),bin(n1))
    print getattr(list_as_stack, 'append')
    print map(lambda x: x.split()[2], a )
    print filter(isOdd,list_as_stack)
    print map(cube,list_as_stack)
    print reduce(add,list_as_stack)
    print list_as_stack

def queueFuncs():
    queue = deque(['sahil', 'sahil1', 'sahil2'])
    queue.append('sahil3')
    queue.appendleft('sahil4')
    queue.extend([1, 3, 6]) ## adds a elements on a data type that is iterable 
    queue.rotate(2)
    print queue

def dictFuncs():
    d = {1:'sad',2:'happy'}
    print d.viewkeys()
    print d.get(5)
    print d
    for k,v in d.iteritems():
        print k,v

print 'listFuncs'
listFuncs()
print 'queueFuncs'   
queueFuncs()
print 'dictFuncs'   
dictFuncs()