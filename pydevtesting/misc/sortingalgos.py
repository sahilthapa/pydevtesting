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
    
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
    print alist

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

inp = raw_input("Enter element (add * to quit):")
y = []
while (inp != '*'):
    y.append(inp)
    print y
    inp = raw_input("Enter element (add * to quit):")
print "User Input:" 
print (y,' with length',len(y)) 
print "BubbleSort Output:"
bubbleSort(y)
print "SelectionSort Output:"
selectionSort(y)
print "InsertionSort Output:"
selectionSort(y)
print "MergeSort Output:"
mergeSort(y)
print "QuickSort Output:"
quickSort(y)