# Write a Python program to check a list is empty or not.

def check_list_is_empty(user_list):
    if not user_list:
        return True
    else:
        return False
    
lst = []

if check_list_is_empty(lst):
    print("List is empty")
else:
    print("List is not empty")