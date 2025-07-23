# Get letter form user for test a passed letter is a vowel or not. 
letter = input("Enter a letter : ")

# List of vowels
list = ["a","e","i","o","u","A","E","I","O","U"]

# check is vowel or not
if letter in list:
    print("You passed letter is a vowel.")
else:
    print("You passed letter is not a vowel. ")


# Output
# Enter a letter : a
# You passed letter is a vowel.