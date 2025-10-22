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

d1 = {'id': 101, 'name': 'Ram', 'role': 'HR'}
d2 = {'id': 102, 'name': 'Sam', 'age': 25}

result=set(d1.keys())|set(d2.keys())
print(result)
# Remove keys with None or empty values

d={'id':None,'name':'sam','role':None,"age":24}

result={k:v for k,v in d.items() if v not in(None,{},'',[],())}

print(result)


# Count character frequency in a string using a dictionary

text = "hello world"

freq={}

for c in text:

    if c in freq:

        freq[c]+=1

    else:

        freq[c]=1

print(freq)

# Create a dictionary of word lengths from a sentence

sentence = "Python is a powerful programming language"

word_length={word:len(word) for word in sentence.split(" ")}

print(word_length)



# Store students’ marks in a nested dictionary and find average

students = {
    'Alice': {'Math': 85, 'Science': 90, 'English': 78},
    'Bob': {'Math': 75, 'Science': 80, 'English': 72},
    'Charlie': {'Math': 95, 'Science': 88, 'English': 91}
}

for name,marks in students.items():

    total=sum(marks.values())
    count=len(marks)
    average=total/count

    print(f"{name}'s average is {average:.2f}")

# Flatten a nested dictionary (one level)
