
def rotate_arrays(nums,k,direction):

    if not nums:
        return nums
    
    if direction=="left":
        return nums[k:]+nums[:k]
    elif direction=="right":
        return nums[-k:]+nums[:-k]
    else:
        return "Invalid direction"

print(rotate_arrays([1,2,3,4,5],2,"left"))
print(rotate_arrays([1,2,3,4,5],2,"right"))
