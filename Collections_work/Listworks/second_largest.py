lst=[3,2,1,5,4,6]

lst.sort(reverse=True)

print("Second largest number is :", lst[1])

#method-2

largest=max(lst)
lst.remove(largest)
second_largest=max(lst)
print(second_largest)