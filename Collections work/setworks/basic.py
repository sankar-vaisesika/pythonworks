# Create a set and print all elements

st1={1,2,3,4}   

print(st1)

# Add a single element using add()

st1.add(10)

print(st1)

# Add multiple elements using update()

st2={'q','w','e','r','t','y'}

st1.update(st2)

print(st1)

#or

numbers={1,2,3,4}

numbers.update([5,6,71,23])

print(numbers)

# Remove an element using remove()
st1.remove('q')

print(st1)

# Remove an element using discard()
st1.discard('q')

print(st1)
# Remove and return a random element using pop()

x=st1.pop()
print(x)

# Clear all elements from a set using clear()

st1.clear()

print(st1)
# Find the length of a set using len()
print(len(st2))
# Check if an element exists in a set

if "q" in st2:

    print("yes")

else:
    print("no")

# Convert a list/tuple to a set

lst=[1,2,3,23,213,123,123,123,2312]

print(tuple(lst))