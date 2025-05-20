# Find the difference of elements in two lists

lst1=[2,1,4,6,3]

lst2=[4,2,1,2,1]

difference_1=[]

for num in lst1:

    if num not in lst2:

        difference_1.append(num)

print(difference_1)

# Flatten a nested list

nested_lst=[[1,2],[3,4],[5,6]]

flatten=[]

for sublst in nested_lst:

    for item in sublst:

        flatten.append(item)

print(flatten)


# Split a list into sublists of equal size (e.g., chunks of 3)
lst=[1, 2, 3, 4, 5, 6]

chunks=[]

for i in range(0,len(lst),3):
    chunks.append(lst[i:i+3])

print(chunks)

# Rotate a list to the left or right

lst=[1, 2, 3, 4, 5, 6]

last=lst.pop()

lst.insert(0,last)

print("right rotation:",lst)

lst1=[1,2,3,4,5,6]

first=lst1.pop(0)

lst1.append(first)

print(lst1)

# Find all pairs in a list that sum to a specific value

lst=[2,3,1,4,5,7]

sum=6

pairs=[]

for i in range(len(lst)):

    for j in range(i+1,len(lst)):

        if lst[i]+lst[j]==sum:

            pairs.append((lst[i],lst[j]))

print(pairs)

# Remove all None values from a list

lst=[1,2,None,4,None]

cleaned_lst=[item for item in lst if item is not None]

print(cleaned_lst)

# Filter only strings or numbers from a mixed list

lst=[1,'a',2,'b',None,'c',3.5]

# only_strings=[item for item in lst if type(item)==str]

only_strings=[item for item in lst if isinstance(item,str) ]

print(only_strings)

# only_numbers=[item for item in lst if type(item)==int ]

only_numbers=[item for item in lst if isinstance(item,(int,float))]

print(only_numbers)

# Transpose a 2D list (like a matrix)

matrix = [[1, 2, 3], [4, 5, 6]]

transposed=list(map(list,zip(*matrix)))

print(transposed)

# Zip two lists together (like key-value pairs)

keys = ['name', 'age', 'role']
values = ['Alice', 25, 'HR']

d=dict(zip(keys,values))

print(d)

# Convert list to string using join()

words = ['hello', 'world']

sentence=" ".join(words)

print(sentence)
