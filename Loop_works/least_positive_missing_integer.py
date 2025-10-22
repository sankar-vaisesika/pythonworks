lst=[1,2,3,5]

sum_of_lst=sum(lst) #11

maxi=max(lst)   #5

total=0

for i in range(1,maxi+1):

    total+=i

print(total)

if total==sum_of_lst:

    print("least",maxi+1)

else:

    print("least:",total-sum_of_lst)