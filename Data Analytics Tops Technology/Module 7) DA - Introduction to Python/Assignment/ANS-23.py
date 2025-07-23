'''Write a Python program to get a string made of the first 2 and the last 
2 chars from a given a string. If the string length is less than 2, return 
instead of the empty string. '''

Str = input("Enter String : ")

newStr = Str[:2]+ Str[-2:]

if len(Str)<=2:
    print(" ")
else:
    print(newStr)