# Create a dictionary and print all key-value pairs
employee={"id":101,"name":"Manu","role":"hr"}

print(employee)
# Access values using keys

print(employee["name"])

# Add a new key-value pair to a dictionary
employee['age']=23

print(employee)

# Update an existing value

employee['age']=25

print(employee)

# Remove a key using pop()

employee.pop('age')

print(employee)
# Remove the last inserted item using popitem()

employee.popitem()
print(employee)

# Get all keys, values, and items using keys(), values(), items()
k=employee.keys()
print(k)

# Check if a key exists in a dictionary
v=employee.values()
print(v)
# Find the length of a dictionary
print(len(employee))
# Copy a dictionary using copy()

dict=employee.copy()

print(dict)