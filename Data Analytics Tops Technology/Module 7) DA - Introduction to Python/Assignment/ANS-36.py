# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def Unique_lst_elements(user_lst):
    unique_lst = []
    for item in user_lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

lst = [1,2,2,5,5,6,4,3,5,2,8,6,7,9]

unique_list = Unique_lst_elements(lst)
print(f"Unique list : {unique_list}")

print("Length of list : ",len(lst))
print("Length of unique list : ",len(unique_list))
