## BubbleSort intuition: The list is sorted by sub sorting till sub index level k
## and iterating it till end of list 
def bubbleSort(a):
    for k in range(len(a)-1,0,-1):
        for j in range(k):
            if (a[j] > a[j+1]):
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp 
    print a
## Moves minimum to start of list and iteratively moving other list vals 
## iteratively in desc order
def selectionSort(a):
    for i in range(len(a)-1):
        imin =  i
        for k in range(i+1,len(a)):
            if (a[k] < a[imin]):
                imin = k
        if (imin!=i):
            tmp = a[i]
            a[i] = a[imin]
            a[imin] = tmp
    print a        
inp = raw_input("Enter element (add * to quit):")
y = []
while (inp != '*'):
    y.append(inp)
    print y
    inp = raw_input("Enter element (add * to quit):")
print "User Inputted:" 
print y 
print "BubbleSort Output:"
bubbleSort(y)
print "SelectionSort Output:"
selectionSort(y)