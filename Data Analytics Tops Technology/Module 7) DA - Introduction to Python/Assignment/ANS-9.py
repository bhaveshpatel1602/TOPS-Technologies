# Get two numbers form user for swap two number Using temp variable

a = int(input("Enter a first number : "))
b = int(input("Enter a second number : "))

# Using temp variable swap numbers

temp = a
a = b
b = temp

# Print numbers

print(f"After swap your first number is {a} and second number is {b}")

# ------------------------------------------------------------------------------------------------------------------------

# Get two numbers form user for swap two number without temp variable

x = int(input("Enter a first number : "))
y = int(input("Enter a second number : "))

# Without temp variable

x = x + y
y = x - y
x = x - y

# print numbers

print(f"After swap your first number is {x} and second number is {y}")
