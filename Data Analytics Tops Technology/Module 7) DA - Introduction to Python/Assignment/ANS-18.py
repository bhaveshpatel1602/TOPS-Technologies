# Write a Python program to count occurrences of a substring in a string.

# Get string and sub string form user
Str = input("Enter string : ")
Sub = input("Enter sub string : ")

# convert to lower case to check correct Occurrences
Str = Str.lower()
Sub = Sub.lower()

# Check count of substring in string
cnt = Str.count(Sub)

# Print count of substring in string
print(f"Count of subsrting is : {cnt}.")


