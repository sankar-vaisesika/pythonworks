# 1. Longest Mountain Subarray
# A mountain increases strictly then decreases strictly.

# Return the length of the longest mountain.
# Example:
# [2,1,4,7,3,2,5] → 5 ([1,4,7,3,2])
 
# 2.Top K Frequent Elements
# Return the k most frequent elements in a list.
 
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
 