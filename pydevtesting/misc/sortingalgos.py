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

def insertionSort(a):
    for i in range(len(a)-1):
        j =  i
        x = a[i]
        while j > 0 and a[j-1] > x : 
            a[j] = a[j-1]
            j = j-1
        a[j] = x
    print a    

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)   
    
inp = raw_input("Enter element (add * to quit):")
y = []
while (inp != '*'):
    y.append(inp)
    print y
    inp = raw_input("Enter element (add * to quit):")
print "User Input:" 
print y 
print "BubbleSort Output:"
bubbleSort(y)
print "SelectionSort Output:"
selectionSort(y)
print "InsertionSort Output:"
selectionSort(y)
print "MergeSort Output:"
mergeSort(y)