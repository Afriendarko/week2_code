def rf(n):  
    if n <= 1:  
        return n  
    else:  
        return(rf(n-1) + rf(n-2))  
nterms = int(input("Upto: "))  
  
if nterms <= 0:  
    print("Plese enter a positive integer")  
else:    
    for i in range(1,nterms+1):  
        print(rf(i))