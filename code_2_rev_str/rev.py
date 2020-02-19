# Reverse String

def reverse(string):
    rstri = ""
    for i in string:
        rstri = i + rstri
    return rstri

string = input()

reverse(string)