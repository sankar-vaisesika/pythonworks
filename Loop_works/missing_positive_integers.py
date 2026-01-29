arr=[1,2,5,2,4,4]

arr=sorted(set(arr))

for i in range(0,len(arr)-1):

    j=i+1

    result=arr[j]-arr[i]

    if result!=1:

        print(arr[i]+1,"is missing")

        break

#another method

arr=[1,3,5,3,2]
arr=set(arr)
n=len(arr)+1

expected_sum=n*(n+1)//2
actual_sum=sum(arr)

print("Missing number is :",expected_sum-actual_sum)