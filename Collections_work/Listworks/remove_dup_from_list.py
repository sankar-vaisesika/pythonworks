arr=[1,2,5,3,5,6,4,2]

#method 1

arr=list(set(arr))

print(arr)

#method 2

unique_arr=[]

for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)

print(unique_arr)

#method 3

unique_lst=list(dict.fromkeys(arr))

print(unique_lst)