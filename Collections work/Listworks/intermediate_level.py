# Find the sum of all elements in a list
lst=[64, 3, 12, 50, 2, 2, 11]

print(sum(lst))

# Find the largest and smallest elements

max_num=max(lst)

print(max_num)

min_num=min(lst)

print(min_num)

# Find the second largest and second smallest

unique_lst=list(set(lst))

unique_lst.sort(reverse=True)

sec_largest=unique_lst[1]

print(sec_largest)

sec_smallest=unique_lst[-2]

print(sec_smallest)

# Remove duplicates from a list

print(unique_lst)

#or

lst=[64, 3, 12, 50, 2, 2, 11]

unique_lst=[]

for num in lst:

    if num not in unique_lst:

        unique_lst.append(num)

print(unique_lst)

#or

lst=[64, 3, 12, 50, 2, 2,3,12, 11]

unique_lst=list(dict.fromkeys(lst))

r=print(unique_lst)

# Print even and odd numbers separately

lst=[64, 3, 12, 50, 2, 2,3,12, 11]

odd_numbers=[]

even_numbers=[]

for num in lst:

    if num%2!=0:
        odd_numbers.append(num)

    else:
        even_numbers.append(num)

print("odd numbers:",odd_numbers,"Even numbers:",even_numbers)

# Separate positive and negative numbers

lst=[1,3,-2,1,-4,-6,3]

pos_numbers=[]

neg_numbers=[]

for num in lst:

    if num>0:

        pos_numbers.append(num)

    else:

        neg_numbers.append(num)

print(f"Positive numbers:{pos_numbers},Negative numbers:{neg_numbers}")

# Swap first and last elements in a list

lst=[1,3,-2,1,-4,-6,3]

lst[0],lst[-1]=lst[-1],lst[0]

print(lst)

# Shift elements circularly to the right by 1
lst=[1,3,-2,1,-4,-6,3]

last=lst.pop()
lst.insert(0,last)
print(lst)

# Check if a list is a palindrome

lst=['m','a','l','a','y','a','l','a','m']

if lst==lst[::-1]:

    print("list is palindrome")

else:
    print("list is not a palindrome")

# Create a list of squares from another list

lst=[1,2,3,4,5]

squares=[num**2 for num in lst]

print(squares)

# Merge two sorted lists into one sorted list

lst1=[543,234,2,234,124,1]

lst2=[123,412,3,223,412,12,1]

lst3=sorted(lst1+lst2)

print(lst3)

#or

def merge_sorted_list(a,b):

    result=[]

    i=j=0

    while i<len(a) and j<len(b):

        if a[i]<b[j]:

            result.append(a[i])

            i+=1

        else:

            result.append(b[j])

            j+=1

    # result.extend(a[i:])
    # result.extend(b[j:])

    return result    


a = [1, 2, 124, 234, 234, 543]
b = [1, 3, 12, 123, 223, 412, 412]

merged = merge_sorted_list(a, b)
print(merged)

# Find common elements in two lists

lst1=[2,4,2,1,5,6,7,54]

lst2=[12,42,21,1,5,16,27,524]

common_elements=[]

for i in range(0,len(lst1)):

    for j in range(0,len(lst2)):

        if lst1[i]==lst2[j]:

            common_elements.append(lst1[i])


print(common_elements)

# Find the difference of elements in two lists

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7]

diff_1=[num for num in lst1 if num not in lst2]

print(diff_1)

# Flatten a nested list

nested=[[1,2],[3,4],[5,6]]

flat=[]

for sublist in nested:

    for item in sublist:

        flat.append(item)

print(flat)
# Split a list into sublists of equal size (e.g., chunks of 3)

lst=[1, 2, 3, 4, 5, 6]

chunks=[]

for i in range(0,len(lst),3):
    
    chunks.append(lst[i:i+3])

print(chunks)

