# Create a list and print all elements

lst=[1,2,64,23,12,2,1,3]

print(lst)


#find the length of the list

print(len(lst))

# Access elements using index and slice

print(lst[1])

print(lst[:])

# Append an element to the list

lst.append(5)

print(lst)

# Insert an element at a specific position

lst.insert(2,100)

print(lst)

# Remove a specific element from a list

lst.remove(100)
print(lst)

# Remove an element using pop()

lst.pop(0)
print(lst)

# Sort a list in ascending and descending order
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)
# Reverse a list
lst.reverse()
#or
print(lst[::-1])

# Check if an element exists in a list
print(2 in lst)
#or
print(lst.count(2))

# Count the occurrences of an element
print(lst.count(2))

# Find the index of an element
print(lst.index(2))
# Concatenate two lists
lst1=[2,3,4,1]
lst3=lst+lst1
print(lst3)
# Repeat a list using multiplication
print(lst3*2)
# Convert a string to a list using split()

str="Hai good morning How are you"

str_lst=str.split(" ")

print(str_lst)

# How can you find the index of the last occurrence of a specific element in a list?

print(len(lst)-1-lst[::-1].index(2))
