# Write a Python function to reverses a string if its length is a multiple of 4.

Str = input("Enter a string : ")

if len(Str)%4==0:
    Str = Str[::-1]
    print(Str)
else:
    print("String length is not a multiple of 4.")