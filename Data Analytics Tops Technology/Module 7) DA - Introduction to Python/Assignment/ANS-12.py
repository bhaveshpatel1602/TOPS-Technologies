#  Get numbers for sum of three integers.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter thied number : "))

#  if two values are equal sum will be zero.

# Using if else
if a == b  or a == c or b == c :
    print("Here two values are equal so sum will be zero")
else:
    print("Sum of three integers is ", (a+b+c))