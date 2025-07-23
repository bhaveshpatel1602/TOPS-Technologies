# get input from user.
num = int(input("Enter a number : "))

# first two default number of fibonacci series (0,1)
a = 0
b = 1

print("Fibonacci series : ")

#Using for loop generate fibonacci series

for i in range(num):
    print(a,end=" ")
    # generate next term
    c = a + b
    a = b
    b = c

