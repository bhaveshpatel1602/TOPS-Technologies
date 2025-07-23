# Get number form user for get the Factorial number

num = int(input("Enter a number : "))

# Using if else and for loop get factorial number

if num < 0 :
    print("Factorial is not defined for negative numbers.")
elif (num == 0 or num == 1):
    print("Factorial is 1.")
else:
    Fac = 1
    for i in range(2,num + 1):
        Fac*=i
        # print(Fac)
    print(f"Factorial is {Fac}")
