'''Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string.'''

# Get two string form user
Str1 = input("Enter first string : ")
Str2 = input("Enter second string : ")

# get a single string from two given strings, separated by a space and swap the first two characters

Str = (Str2[:2]+Str1[2:])+(" ")+(Str1[:2]+Str2[2:])

# print(f"{Str2[:2]+Str1[2:]} {Str1[:2]+Str2[2:]}")

# print string
print(Str)