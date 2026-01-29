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



#pagination

# Find the GCD and LCM of Two Numbers
# def gcd(n1,n2):
#     gcd=1
#     for i in range(1,min(n1,n2)+1):
#         if n1%i==0 and n2%i==0:
#             gcd=i
#     return gcd

# print(gcd(12,36))

# def lcm(a,b):
#     greater=max(a,b)

#     while True:
#         if greater%a==0 and greater%b==0:
#             lcm=greater
#             break
#         greater+=1

#     return lcm
# print(lcm(12,15))
# Find the Missing Number in an Array (1 to N)

arr=[1,3,5,3,2]

arr=sorted(set(arr))
print(arr)
for i in range(len(arr)-1):
    j=i+1

    res=arr[j]-arr[i]
    if res!=1:
        print("Missing number is",arr[i]+1)
# Remove Duplicate Elements from a List
lst=[1,3,5,3,2]

print(list(set(lst)))
# Check if Two Strings are Anagrams
def is_anagram(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    return sorted(s1)==sorted(s2)
print(is_anagram("listen","silent"))
# Reverse a String Without Using Built-in Functions

def rev(s):
    reversed_s=""
    for i in s:
        reversed_s=i+reversed_s 

    return reversed_s

print(rev("abcdefgh"))