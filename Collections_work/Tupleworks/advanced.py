# Filter even/odd numbers from a tuple

tp=(1,2,3,4,5,6,7,8,9)
even_numbers=[]

odd_numbers=[]
for num in tp:

    if num%2==0:

        even_numbers.append(num)

    else:
        odd_numbers.append(num)

print(even_numbers)
print(odd_numbers)

# Remove duplicates from a tuple (convert to set then back)

tp=(2,1,2,4,3,2,2,1,2)

tp=tuple(set(tp))

print(tp)

#to prevent order also
tp=(2,1,2,4,3,2,2,1,2)

st=set()

unique=[]

for item in tp:

    if item not in st:

        st.add(item)

        unique.append(item)

tp=tuple(unique)

print(tp)

# Flatten a nested tuple

tp=((1,2,3),(4,5,6))

flatten=[]

for subitem in tp:

    for item in subitem:

        flatten.append(item)

flatten=tuple(flatten)

print(flatten)

# Find common elements in two tuples

tp1=(2,1,3,4,3,1,3,5)

tp2=(4,2,1,2,4,5,7,8,9)

common_elements=tuple(i for i in tp1 if i in tp2 )

print(common_elements)
# Convert a tuple of strings into a single string

tp=('ram','sam','sham')

string=" ".join(tp)

print(string)

# Find the element-wise sum of two numeric tuples

# Reverse a tuple
tp=(2, 1, 4, 1, 5)

tp=tp[::-1]

print(tp)

# Find unique elements in a tuple

tp=(2, 1, 4, 1, 5)

unique_elements=tuple(num for num in tp if tp.count(num)==1)

print(unique_elements)

# Count total characters in a tuple of strings

tp=(2,'c','r','q', 1, 4, 1, 5)
num=0
for i in tp:

    if isinstance(i,str):

        num+=1

print(num)

# Tuple comprehension using generator expressions

squares=tuple(x**2 for x in range(1,6))

print(squares)