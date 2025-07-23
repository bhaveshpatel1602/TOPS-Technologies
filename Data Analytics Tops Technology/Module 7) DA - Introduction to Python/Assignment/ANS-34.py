# Write a Python function that takes two lists and returns true if they have at least one common member.

def common_number(lst1,lst2):
    for item in lst1:
        for item in lst2:
            return True
        return False
    
lst1 = [1,2,5,8,6,4,3,2]
lst2 = [8,6,5,4,2,3,9,7]

if common_number(lst1,lst2):
    print("List have common numbers.")
else:
    print("List have no any common numbers.")
    