# Regular expression - re module
# opening and writing reading a file - contence manager like file operations
# django project 
# ai-paper
# ml-books

#string operation and string methods
# is and ==
#looping 
#list
#django project



#pagination


# 1. Longest Mountain Subarray
# A mountain increases strictly then decreases strictly.
# Return the length of the longest mountain.
# Example:
# [2,1,4,7,3,2,5] → 5 ([1,4,7,3,2])
 

def longest_mountain_subarray(nums):
    n=len(nums)
    longest=0
    i=1
    while i<n-1:
        if nums[i-1]<nums[i]>nums[i+1]:
            left=i-1
            right=i+1
            while left>0 and nums[left-1]<nums[left]:
                left-=1
            while right<n-1 and nums[right]>nums[right+1]:
                right+=1
            longest=max(longest,right-left+1)

        else:
            i+=1
    return longest

print(longest_mountain_subarray([2,1,4,7,3,2,5]))