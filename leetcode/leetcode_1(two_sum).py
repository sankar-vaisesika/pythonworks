
def twoSum(nums,target):

    for i in range(0,len(nums)):

        for j in range(i+1,len(nums)):

            if nums[i]+nums[j]==target:

                return ([i,j])
    


print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))
print(twoSum([3,3],6))




# def twoSum(nums,target):

#     num_dict={}

#     for i,num in enumerate(nums):

#         difference=target-num

#         if difference in num_dict:

#             return[num_dict[difference],i]
        
#         num_dict[num]=i

#     return []

# print(twoSum([2,7,11,15],9))
# print(twoSum([3,2,4],6))
# print(twoSum([3,3],6))


