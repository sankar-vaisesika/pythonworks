# Remove Duplicates from Sorted Array

def removeDuplicates(nums):

    l=1

    for r in range(1,len(nums)):

        if nums[r]!=nums[r-1]:

            nums[l]=nums[r]

            l+=1

    return l

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
