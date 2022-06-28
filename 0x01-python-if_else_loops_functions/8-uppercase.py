#!/usr/bin/python3
def uppercase(str):
    strng = ""
    for i in str:
        if i >= 'a' and i <= 'z':
            strng = strng + chr((ord(i) - 32))
        else:
            strng = strng + i
print("{}".format(str))    
