# Find Median of Two Sorted Arrays

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
