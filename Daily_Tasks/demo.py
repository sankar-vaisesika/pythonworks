# # 1. Longest Mountain Subarray
# # A mountain increases strictly then decreases strictly.

# # Return the length of the longest mountain.
# # Example:
# # [2,1,4,7,3,2,5] → 5 ([1,4,7,3,2])

# def longest_mountain(arr):
#     n=len(arr)  #7
#     longest=0
#     i=1
#     while i<n-1:
#         if arr[i-1]<arr[i]>arr[i+1]:    #3
#             left=i-1                    #2  
#             right=i+1                   #4

#             while left>0 and arr[left-1]<arr[left]:
#                 left-=1                 #1
#             while right<n-1 and arr[right]>arr[right+1]:
#                 right+=1                #5
#             longest=max(longest,right-left+1)
#             i=right
#         else:
#             i+=1
#     return longest


# print(longest_mountain([0,1,4,7,3,2,5]))
 
# # 2.Top K Frequent Elements 
# # Return the k most frequent elements in a list.

# def top_k_frequent(nums, k):
#     freq = {}    
#     for num in nums:
#         if num in freq:
#             freq[num]+=1
#         else:
#             freq[num]=1

#     sorted_items=sorted(freq.items(),key=lambda x:x[1],reverse=True)
#     result=[]
#     for i in range(k):
#         result.append(sorted_items[i][0])

#     return sorted_items


# print(top_k_frequent([1,1,1,2,2,3],2))
# print(top_k_frequent([4,1,-1,2,-1,2,3],2))

 
# # 3.Maximum Sum Subarray of Size K
# # Find the maximum sum of any contiguous subarray of size k

# def max_sum_subarray(arr,k):
#     if len(arr)<k: return 0

#     current_sum=sum(arr[:k])
#     max_value=current_sum

#     for i in range(len(arr)-k):     #6-2=4
#         current_sum=current_sum-arr[i]+arr[i+k] #8-2+1
#         max_value=max(max_value,current_sum)
#     return max_value

# print(max_sum_subarray([2,1,5,1,3,2],3))
 
# # 4.Power of Four
# # Determine if a number is a power of four.
 
# def is_power_of_four(n):
#     if n<=0:
#         return False
#     while n%4==0:
#         n=n//4
#     return n==1

# print(is_power_of_four(16))
# print(is_power_of_four(12))
# print(is_power_of_four(1))

# # 5.Find Median of Two Sorted Arrays

# def find_median_sorted_arrays(nums1,nums2):
#     merged=nums1+nums2
#     merged.sort()
#     mid=len(merged)//2
#     if len(merged)%2==0:
#         return (merged[mid]+merged[mid-1])/2
#     else:
#         return merged[mid]
    
# print(find_median_sorted_arrays([1,3],[2]))
# print(find_median_sorted_arrays([1,2],[3,4]))

# 1.Find Common Elements in Two Lists
# Return common elements without duplicates.

def common_elements(l1,l2):
    # result=[]
    # for i in l1:
    #     if i in l2:
    #         result.append(i)
    # return result

    return list(set(l1) & set(l2))
print(common_elements([1,2,4],[4,2,6,7]))


 
# 2. Swap Two Numbers (No Temp Variable)
def swap(n1,n2):
    # n1,n2=n2,n1
    # return n1,n2
    n1=n1+n2 #8
    n2=n1-n2 #3
    n1=n1-n2 #5
    return n1,n2
print(swap(3,5))
 
# 3.First Repeating Element
# Find the first element that repeats in a list.
# [10, 5, 3, 4, 3, 5, 6] → 5
def first_repeating_element(nums):
    seen=set()
    repeater=None
    for i in range(len(nums)-1,-1,-1):
        if nums[i] in seen:
            repeater=nums[i]
        else:
            seen.add(nums[i])
    return repeater
print(first_repeating_element([0, 5, 3, 4, 3, 5, 6]))
 
# 4.Check if Two Strings Are Rotations
# "abcd" & "cdab" → True

def is_rotation(s1,s2):
    if len(s1)!=len(s2) or not s1: return False
    return s2 in s1+s1

print(is_rotation("abcd","cdab"))
 
# 5. Move All Zeros to End
# Maintain order of non-zero elements.
# [0,1,0,3,12] → [1,3,12,0,0]
 
def move_zeroes(nums):
    last_non_zero=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[last_non_zero],nums[i]=nums[i],nums[last_non_zero] #nums[0],nums[1]=nums[1],nums[0]
            last_non_zero+=1
    return nums
print(move_zeroes([0,1,0,3,12]))