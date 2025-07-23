# Write a Python program to check multiple keys exists in a dictionary

def check_keys(dict,keys):
    return all(key in dict for key in keys)

dict = {
    'name': 'Alice',
    'age': 30,
    'country': 'USA',
    'email': 'alice@example.com'
}

keys = ['name', 'email']

keys_exists = check_keys(dict,keys)
print(keys_exists)