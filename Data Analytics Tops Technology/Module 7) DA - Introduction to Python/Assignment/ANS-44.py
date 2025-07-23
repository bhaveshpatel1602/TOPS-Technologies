# Write a Python program to create a tuple with different data types. 

tuple = ("Alice", 30, 5.5, True, None, [1, 2, 3], {'key': 'value'})
print(tuple,"\n\n")
for item in tuple:
    print(f"'{item}' type is : {type(item)} \n")