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
 
# 2.Top K Frequent Elements 
# Return the k most frequent elements in a list.

def top_k_frequent(nums, k):
    freq = {}

    
    for num in nums:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1

    sorted_items=sorted(freq.items())
    result=[]
    for i in range(k):
        result.append(sorted_items[i][0])

    return result


print(top_k_frequent([1,1,1,2,2,3],2))
 
# 3.Maximum Sum Subarray of Size K
# Find the maximum sum of any contiguous subarray of size k

def max_sum_subarray(arr,k):
    if len(arr)<k: return 0

    current_sum=sum(arr[:k])
    max_value=current_sum

    for i in range(len(arr)-k):     #6-2=4
        current_sum=current_sum-arr[i]+arr[i+k] #8-2+1
        max_value=max(max_value,current_sum)
    return max_value

print(max_sum_subarray([2,1,5,1,3,2],3))
 
# 4.Power of Four
# Determine if a number is a power of four.
 
def is_power_of_four(n):
    if n<=0:
        return False
    while n%4==0:
        n=n//4
    return n==1

print(is_power_of_four(16))
print(is_power_of_four(12))
print(is_power_of_four(1))

# 5.Find Median of Two Sorted Arrays

def find_median_sorted_arrays(nums1,nums2):
    merged=nums1+nums2
    merged.sort()
    mid=len(merged)//2
    if len(merged)%2==0:
        return (merged[mid]+merged[mid-1])/2
    else:
        return merged[mid]

print(find_median_sorted_arrays([1,3],[2]))
print(find_median_sorted_arrays([1,3],[2,4]))
