# arr=[2,3,4,5,6,8,9]

# l=0

# r=len(arr)-1

# sum=8

# while arr[l]<arr[r]:

#     cur_sum=arr[l]+arr[r]

#     if cur_sum==sum:

#         print(arr[l],arr[r])

#         l=l+1

#         r=r-1

#     elif cur_sum<sum:

#         l+=1

#     elif cur_sum>sum:

#         r-=1

# another method

arr=[2,3,4,5]

sum=7

count=0

for i in range(0,len(arr)-1):

    for j in range(i+1,len(arr)):

        cur_sum=arr[i]+arr[j]

        count+=1

        if cur_sum==sum:

            print(arr[i],arr[j])

            break

print(count)