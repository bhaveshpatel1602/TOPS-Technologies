#  Write a Python program to unzip a list of tuples into individual lists.

tuple_list = [(1, 'a'), (2, 'b'), (3, 'c')]

lst1, lst2 = zip(*tuple_list)

print(f"{list(lst1)} or {list(lst2)}")