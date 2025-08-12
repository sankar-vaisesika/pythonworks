

def singleNumber(nums):

    res=0

    for n in nums:

        res=n^res
    
    return res
        
   

print(singleNumber([2,2,1]))
res = 0
# res = 2 ^ 0     => 2
# res = 2 ^ 2     => 0 (because same numbers cancel each other)
# res = 1 ^ 0     => 1

print(singleNumber([4,1,2,1,2]))
# res = 0
# res = 4 ^ 0     => 4
# res = 1 ^ 4     => 5
# res = 2 ^ 5     => 7
# res = 1 ^ 7     => 6
# res = 2 ^ 6     => 4

print(singleNumber([1]))
# res = 0
# res = 1 ^ 0     => 1

