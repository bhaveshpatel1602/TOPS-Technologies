#  Write a Python function to insert a string in the middle of a string.

sen = input("Enter a string : ")
sen2 = input("Enter a second string : ")

length = len(sen)
Mlength = int(length//2)

# print(Mlength)

newsen = sen[:Mlength]+" "+sen2+" "+sen[Mlength:]
print(newsen)