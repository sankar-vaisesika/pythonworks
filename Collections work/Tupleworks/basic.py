# Create a tuple and print all elements

tp1=(1,2,3,'sam')

# Access elements using indexing and slicing

print(tp1[2])

print(tp1[2:])
# Find the length of a tuple using len()
print(len(tp1))
# Convert a list to a tuple
lst=[2,1,3,2,1,1]
print(tuple(lst))

# Convert a tuple to a list
print(list(lst))

# Check if an element exists in a tuple

if 2 in tp1:

    print("yes")

else:

    print("no")

# Count the occurrences of an element using .count()

print(tp1.count(1))

# Find the index of an element using .index()

print(tp1.index(2))
# Concatenate two tuples
tp2=(2,3,1,3,4)
tp3=tp1+tp2
print(tp3)
# Repeat a tuple using multiplication (*)

tp3*=3

print(tp3)