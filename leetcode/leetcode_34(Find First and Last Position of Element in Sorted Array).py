# Find First and Last Position of Element in Sorted Array

def find_first_last(nums,target):
    first,last=-1,-1

    for i in range(len(nums)):
        if nums[i]==target:
            if first==-1:
                first=i
            last=i

    return [first,last]

nums = [2, 4, 4, 4, 6, 7, 9]
target = 4
print(find_first_last(nums, target))