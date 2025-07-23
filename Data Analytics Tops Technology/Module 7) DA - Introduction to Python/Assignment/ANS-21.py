"""Write a Python program to add 'in' at the end of a given string (length 
should be at least 3). If the given string already ends with 'ing' then 
add 'ly' instead if the string length of the given string is less than 3, 
leave it unchanged."""

Str = input("Enter a string : ")

Str = Str.replace(".","")

if len(Str)<3:
    print(Str)
elif Str.endswith("ing"):
    Str = Str+"ly"
    print(Str)
else:
    Str = Str+"in"
    print(Str)