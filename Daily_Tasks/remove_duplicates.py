#method 1
lst = [1, 2, 2, 3, 4, 4, 5]

print(list(set(lst)))

#method 2

print(list(dict.fromkeys(lst)))

#method 3

unique=[]

for i in lst:
    if i not in unique:
        unique.append(i)

print(unique)