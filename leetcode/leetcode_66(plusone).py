def plusOne(nums):
       
    for i in range(len(nums)-1,-1,-1):

        if nums[i]<9:

            nums[i]+=1

            return nums
        
        nums[i]=0


    return [1]+nums 
        


print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))


