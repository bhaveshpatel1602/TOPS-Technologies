'''Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given list of strings.'''

def count_matching_strings(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
    return count

# Example usage:
string_list = ['abc', 'xyz', 'aba', '1221', 'a', 'ab']
result = count_matching_strings(string_list)
print("Number of matching strings:", result)

