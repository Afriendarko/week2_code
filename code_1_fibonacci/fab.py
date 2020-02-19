def fab(xip):
    l = [1, 1]
    if xip == 1:
            print(l[0]) 
    elif xip <=0:
            print("Please enter some posative integer value" )
    else:
            print(l[0])
            print(l[1])
            for i in range(2, xip):
                ln = l[i-1] + l[i-2]
                l.append(ln)
            print(l)
        
xip = int(input("Upto: "))
fab(xip)