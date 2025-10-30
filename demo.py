
# Regular expression - re module
# opening and writing reading a file - contence manager like file operations
# django project 
# ai-paper
# ml-books

#string operation and string methods
# is and ==
#looping 
#list
#django project

#Longest Palindromic Substring

def longest_palindrome_substring(s):
    best=s[0]

    for i in range(len(s)):

        for j in range(i+1,len(s)+1):

            x=s[i:j]

            if x==x[::-1] and len(x)>len(best):
                best=x

    return best

print(longest_palindrome_substring("babad"))
print(longest_palindrome_substring("cbbd"))
print(longest_palindrome_substring("c"))

# Reverse Integer

def rev_a_integer(num):

    return int(str(num)[::-1])

print(rev_a_integer(1234))

#regular expression matching

import re

pattern=input("Enter pattern:")
text=input("ENter text:")

match=re.search(pattern,text)

if match:
    print("Match found")
    print("Matched text:", match.group())

else:

    print("Match  not found")


#roman to integer

def romanToInteger(s):
    
    roman_mapping={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
    result=0

    for i in range(len(s)):

        if i<len(s)-1 and roman_mapping[s[i]]<roman_mapping[s[i+1]]:
            result-=roman_mapping[s[i]]

        else:
            result+=roman_mapping[s[i]]

    return result
print(romanToInteger("IV"))
print(romanToInteger("LVIII"))
print(romanToInteger("MCMXCIV"))

# Find First and Last Position of Element in Sorted Array

def find_first_last(nums,target):

    first,last=-1,-1

    for i in range(len(nums)):
        if nums[i]==target:
            if first==-1:
                first=i
            last=i

    return [first,last]

nums = [2, 4, 4, 4, 6, 7, 9]
target = 4
print(find_first_last(nums, target))