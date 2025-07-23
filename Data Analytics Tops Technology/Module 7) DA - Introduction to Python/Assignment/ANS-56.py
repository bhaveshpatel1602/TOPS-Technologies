# Write a Python program to map two lists into a dictionary
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 

from collections import Counter

keys = ['a', 'b', 'c', 'd']
values = [400, 400, 300, 400]

mapped_dict = dict(zip(keys, values))

counter_result = Counter(mapped_dict)

print(counter_result)