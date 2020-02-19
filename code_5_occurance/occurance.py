# Count the occurance of character

s = input()
ch = input()

def con(s , ch):
    co = 0
    
    l1 = []
    for i in range(len(s)):
        l1.append(s[i])
    
    for i in range(len(l1)):
        if l1[i] == ch:
            co = co + 1
    
    if co%2==0:
        print("Count={} Value: True".format(co))
    else:
        print("Count={} Value: False".format(co))
    
con(s ,ch)