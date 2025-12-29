# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
#remove element and returns number of non-value element


def remove_element(nums,val):

    k=0

    for i in range(len(nums)):

        if nums[i]!=val:

            nums[k]=nums[i]

            k+=1

    return k

print(remove_element([3,2,2,3],3))
print(remove_element([0,1,2,2,3,0,4,2],2))