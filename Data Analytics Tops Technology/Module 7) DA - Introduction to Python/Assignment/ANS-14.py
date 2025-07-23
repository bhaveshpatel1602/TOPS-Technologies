# Write a python program to sum of the first n positive integers. 
n = int(input("Enter a positive integer : "))

if n < 0:
    print("You enter Negative integer.")
elif n == 0:
    print("You enter Zero.")
else:
    sum = n
    for i in range(n):
        n = n-1
        sum += n
    
    print(f"Sum of positive interger is {sum}")
