'''Write a Python program to generate and print a list of first and last 5 elements 
where the values are square of numbers between 1 and 30. '''

lst = [i**2 for i in range(1,31)]
# print(lst)
first_5 = lst[:5]
last_5 = lst[-5:]

print(f"First five is {first_5} and Last five is {last_5} .")
# print(len(lst))