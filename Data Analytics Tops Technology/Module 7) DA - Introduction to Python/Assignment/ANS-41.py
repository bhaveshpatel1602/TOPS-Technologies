# Write a Python program to check whether a list contains a sub list

def contains_sublist(main_list, sub_list):
    sub_len = len(sub_list)
    if sub_len == 0:
        return True 
    for i in range(len(main_list) - sub_len + 1):
        if main_list[i:i+sub_len] == sub_list:
            return True
    return False

main_list = [1, 2, 3, 4, 5]
sub_list = [3, 4]

if contains_sublist(main_list, sub_list): 
    print("The list contains the sublist.")
else:
    print("The list does not contain the sublist.")