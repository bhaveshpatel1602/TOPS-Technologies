# Write a Python program to find the highest 3 values in a dictionary

my_dict = {'a': 100, 'b': 300, 'c': 250, 'd': 400, 'e': 50}

top_3 = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top 3 highest values in the dictionary:")
for key, value in top_3:
    print(f"{key}: {value}")