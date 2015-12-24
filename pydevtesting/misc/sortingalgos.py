def bubblesort(a):
    #print type(a)
    #tmp_l = []
    for k in range(len(a)-1,0,-1):
        #tmp_l[k] = a[k]
        for j in range(k):
            if (a[j] > a[j+1]):
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp 
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
bubblesort(y)