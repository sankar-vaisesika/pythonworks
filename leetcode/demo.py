# # Length of Last Word

# # Given a string s consisting of words and spaces, return the length of the last word in the string.

# # A word is a maximal substring consisting of non-space characters only.

 
# def lengthOfLastWord(s):

#     last=s.split()[-1]

#     return len(last)


# print(lengthOfLastWord("Hello World"))
# print(lengthOfLastWord("   fly me   to   the moon  "))
# print(lengthOfLastWord("luffy is still joyboy"))
# def plusOne(nums):
       
#     for i in range(len(nums)-1,-1,-1):

#         if nums[i]<9:

#             nums[i]+=1

#             return nums
        
#         nums[i]=0


#     return [1]+nums 
        


# print(plusOne([1,2,3]))
# print(plusOne([4,3,2,1]))
# print(plusOne([9]))


# def addBinary(a,b):  

#     num1=int(a,2)

#     num2=int(b,2)

#     total=num1+num2

#     return bin(total)[2:]

# print(addBinary("11","1"))
# print(addBinary("1010","1011"))
# def merge_sorted_arrays(m,n):
#     res=[]
#     i=j=0
#     while i<len(m) and j<len(n):
#         if m[i]<=n[j]:
#             res.append(m[i])
#             i+=1

#         else:
#             res.append(n[j])
#             j+=1
#     res.extend(m[i:])
#     res.extend(n[j:])

#     return res
# print(merge_sorted_arrays([1,2,3],[2,5,6]))
# print(merge_sorted_arrays([1],[]))
# print(merge_sorted_arrays([0],[1]))





#1)string concatenation and string replica
a="text"
print(a*3)

#2)flow control


#3)functions