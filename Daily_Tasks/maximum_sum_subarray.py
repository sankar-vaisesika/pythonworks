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