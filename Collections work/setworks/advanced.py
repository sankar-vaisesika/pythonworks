# Count unique elements in a list using a set

lst=[1,2,1,3,4,5,6,4,2]

unique_elements=len(set(lst))

print(unique_elements)


# Get common elements from two lists using sets

lst1=[1,2,1,3,4,5,6,4,2]

lst2=[1,3,4,4,2]

common_elements=set()

for i in lst1:

    if i in lst2:

        common_elements.add(i)

print(common_elements)

#or

unique_elements=set(lst1) & set(lst2)

print(unique_elements)
# Find elements that are in either of two lists but not both

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]

result=set(lst1).symmetric_difference(set(lst2))

print(result)

# Filter out vowels from a string using a set

vowels=set("aeiouAEIOU")

string="His mind is lost by many things"

filtered="".join([char for char in string if char not in vowels])

print(filtered)

# Convert a string to a set of unique characters

string="His mind is lost by many things"

unique_chars=set(string)

print(unique_chars)

# Store unique words from a sentence in a set

string="hai hello how is hai hello good"

words=string.split(" ")

print(set(words))
# Get all unique digits from a number using set

num=4213440291

str_num=str(num)

unique_digits=set(d for d in str_num)

print(unique_digits)

# Create a frozen set and try modifying it (to learn immutability)

# Merge multiple sets using set.union()

st1={1,2,3,4}

st2={4,5,8,9}

merged_set=st1.union(st2)

print(merged_set)

# Write a program to simulate set operations (menu-driven)