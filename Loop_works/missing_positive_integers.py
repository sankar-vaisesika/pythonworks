arr=[1,2,5,2,4,4]

arr=sorted(set(arr))

for i in range(0,len(arr)-1):

    j=i+1

    result=arr[j]-arr[i]

    if result!=1:

        print(arr[i]+1,"is missing")

        break