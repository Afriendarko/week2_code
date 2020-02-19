# factorial
f = int(input("Enter number: "))

def fact(f):
    l = [f]
    res = 1

    for i in range(1,f):
        nf = f-i
        l.append(nf)

    for i in range(len(l)):
        res = l[i] * res
    
    print(res)

fact(f)
