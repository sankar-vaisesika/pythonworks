# Find the union of two sets using union() or |

st1={1,2,4,9,5,3}

st2={5,3,2,4,6,8,1}

print(st1|st2)

#or

print(st1.union(st2))

# Find the intersection using intersection() or &

print(st1 & st2)
#or
print(st1.intersection(st2))
# Find the difference using difference() or -

print(st1 - st2)

#or

print(st1.difference(st2))

# Find the symmetric difference using symmetric_difference() or ^
print(st1.symmetric_difference(st2))
#or

print(st1^st2)
# Check if one set is a subset of another using issubset()

print(st1.issubset(st2))

# Check if one set is a superset of another using issuperset()

print(st1.issuperset(st2))

# Check if two sets are disjoint using isdisjoint()

print(st1.isdisjoint(st2))

# Iterate over a set using a loop

for i in st1:

    print(i)

# Copy a set using copy()

st2=st1.copy()

print(st2)

# Remove duplicates from a list using a set

lst=[3,1,1,3,5,6,7,9]

lst=list(set(lst))

print(lst)