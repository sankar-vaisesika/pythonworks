#method 1

arr=[1,2,5,3,5,6,4,2]

duplicate_number=[]

for i in arr:

    if arr.count(i)>1 and i not in duplicate_number:

        duplicate_number.append(i)

print(duplicate_number)

#method 2

arr=[1,2,5,3,5,6,4,2]

duplicate_number=[]

arr.sort()

for i in range(0,len(arr)-1):

    j=i+1

    result=arr[j]-arr[i]

    if result==0:

        if arr[i] not in duplicate_number:

            duplicate_number.append(arr[i])

print(duplicate_number)

#method 3 using sets

arr = [10, 20, 30, 10, 40, 20, 50]

seen=set()

duplicates=set()

for i in arr:

    if i in seen:

        duplicates.add(i)

    else:

        seen.add(i)

print(list(duplicates))