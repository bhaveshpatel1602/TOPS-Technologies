# Write a Python script to sort (ascending and descending) a dictionary by value.

dct = {'apple': 10, 'banana': 2, 'cherry': 7, 'date': 5}

asc = dict(sorted(dct.items(), key=lambda item: item[1]))

des = dict(sorted(dct.items(), key=lambda item: item[1], reverse=True))

print(f"Ascending : {asc} \nDescending : {des}")