# Write a Python program to get unique values from a list.

def unique_values_list(lst):
    return list(set(lst))

lst = [1,5,3,2,1,4,2,6,7,8,5,4,9,6,3]

unique_lst = unique_values_list(lst)
print(unique_lst)