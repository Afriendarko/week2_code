# Anagram

x = input()
y = input()

def anagram(x , y):
    l1 = []
    for i in range(len(x)):
        l1.append(x[i])
    
    l2 = []
    for i in range(len(y)):
        l2.append(y[i])
    count = 0
    
    if len(l1)==len(l2):
        for i in range(len(l2)):
            if l1[i] not in l2:
                count = 1 
                break
    
        if count == 0:
            print("True")
        else:
            print("False")
    
    
    else:
        print("False")
        
anagram(x , y)