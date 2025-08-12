# Merge two dictionaries
d1={"id":101,"role":"hr"}

d2={"name":"sam"}

print(d1.update(d2))

print(d1)

# Create a dictionary from two lists (keys and values)

lst1=["id","role","name"]

lst2=[101,'hr','sam']


d=dict(zip(lst1,lst2))


# Count the frequency of elements in a list using a dictionary

lst=[1,2,1,3,5,3,2,1,1]

frequency={}

for item in lst:

    frequency[item]=frequency.get(item,0)+1

print(frequency)

# Sort a dictionary by keys

d = {'b': 2, 'a': 1, 'c': 3}

sorted_by_keys=dict(sorted(d.items()))

print(sorted_by_keys)

# Sort a dictionary by 

sorted_by_values=dict(sorted(d.items()))

print(sorted_by_values)

# Get the key with the maximum value

d = {'a': 5, 'b': 9, 'c': 3}

max_key = max(d, key=d.get)

print(max_key)

# Get the key with the minimum value

d = {'a': 5, 'b': 9, 'c': 3}

min_key=min(d,key=d.get)

print(min_key)

# Invert a dictionary (swap keys and values)

d = {'a': 1, 'b': 2, 'c': 3}

inverted={}

for k,v in d.items():

    inverted[v]=k

print(inverted)

# Use dictionary comprehension to filter data

d = {'a': 10, 'b': 5, 'c': 12}

filtered={k:v for k,v in d.items() if v>6}

print(filtered)

# Use nested dictionaries (dictionary inside dictionary)


students = {
    '1001': {'name': 'John', 'age': 21},
    '1002': {'name': 'Alice', 'age': 22}
}
print(students['1001']['name']) 