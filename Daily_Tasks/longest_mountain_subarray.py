# 1. Longest Mountain Subarray
# A mountain increases strictly then decreases strictly.

# Return the length of the longest mountain.
# Example:
# [2,1,4,7,3,2,5] → 5 ([1,4,7,3,2])

def longest_mountain(arr):
    n=len(arr)  #7
    longest=0
    i=1
    while i<n-1:
        if arr[i-1]<arr[i]>arr[i+1]:    #3
            left=i-1                    #2  
            right=i+1                   #4

            while left>0 and arr[left-1]<arr[left]:
                left-=1                 #1
            while right<n-1 and arr[right]>arr[right+1]:
                right+=1                #5
            longest=max(longest,right-left+1)
            i=right
        else:
            i+=1
    return longest

print(longest_mountain([2,1,4,7,3,2,5]))