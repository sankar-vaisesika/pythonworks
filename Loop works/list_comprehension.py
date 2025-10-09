nums=[1,2,3,4,5]
#square
square=[num**2 for num in nums]

print(square)

#even numbers
even=[num for num in nums if num%2==0]

print(even)

#first_letter
words=["apple", "banana", "cherry"]

first_letter=[w[0] for w in words]

print(first_letter)

#to uppercase

uppercase=[w.upper() for w in words]

print(uppercase)

#divisile by 3

div_by_three=[i for i in range(1,31) if i%3==0]

print(div_by_three)

#List of tuples (number, square)

squares=[(num,num**2) for num in range(1,10)]

print(squares)

#Common elements between two lists

lst1=[1,2,4,5,6]
lst2=[2,3,4,7,8]

common=[i for i in lst1 if i in lst2]

print(common)

#filter vowels from string

text = "This is a test sentence"

vowels="aeiouAEIOU"

filtered_vowels=[ch for ch in text if ch in vowels]

print(filtered_vowels)

input=[1, 'a', 2, 'b', 3, 'c']

# filter_numbers=[i for i in input if isinstance(i,int)]

#or
filter_numbers=[i for i in input if type(i)==int]
print(filter_numbers)

#flattening 2D list

arr = [[1, 2], [3, 4], [5, 6]]

flattened=[item for sublist in arr for item in sublist]

print(flattened)
