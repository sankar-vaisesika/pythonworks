# Group elements by category using a dictionary
items = [
    ("apple", "fruit"),
    ("carrot", "vegetable"),
    ("banana", "fruit"),
    ("broccoli", "vegetable"),
    ("cherry", "fruit")
]

group={}

for item,category in items:

    if category not in group:

        group[category]=[]

    group[category].append(item)

print(group)

# Convert a list of tuples into a dictionary
list_of_tuples = [("id", 101), ("name", "Ram"), ("role", "HR")]

dictionary = dict(list_of_tuples)

print(dictionary)

# Find common keys between two dictionaries

d1 = {'id': 101, 'name': 'Ram', 'role': 'HR'}
d2 = {'id': 102, 'name': 'Sam', 'age': 25}

common_keys=set(d1.keys())&set(d2.keys())

print(common_keys)

# Find keys present in one dictionary but not in another
d1 = {'id': 101, 'name': 'Ram', 'role': 'HR'}
d2 = {'id': 102, 'name': 'Sam', 'age': 25}

result=set(d1.keys())-set(d2.keys())

print(result)


# Combine values of common keys in two dictionaries

# Remove keys with None or empty values

# Count character frequency in a string using a dictionary

# Create a dictionary of word lengths from a sentence

# Flatten a nested dictionary (one level)

# Store students’ marks in a nested dictionary and find average