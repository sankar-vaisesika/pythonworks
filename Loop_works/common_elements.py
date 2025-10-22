arr1=[10,13,8,11,20]

arr2=[2,20,8,7,13]

for i in range(0,len(arr1)):

    for j in range(0,len(arr2)):

        if arr1[i]==arr2[j]:

            print(arr1[i])

#method 2
         
for i in arr1:

    if i in arr2:

        print(i)
#or

# common=[i for i in arr1 if i in arr2]

# print(common)

#method 3

common_elements=set(arr1)&set(arr2)

print(common_elements)

#method 4

# Using filter() and lambda
arr1 = [10, 13, 8, 11, 20]
arr2 = [2, 20, 8, 7, 13]

common = list(filter(lambda x: x in arr2, arr1))
print(common)

#method 5

common=set(arr1).intersection(arr2)

print(common)

#method 6

arr1.sort()

arr2.sort()

p1,p2=0

while(p1<len(arr1) and p2<len(arr2)):

    if arr1[p1]==arr2[p2]:

        print(arr1[p1])

        p1+=1

        p2+=1

    elif arr1[p1]<arr2[p2]:

        p1+=1

    elif arr1[p1]>arr2[p2]:

        p2+=1

        