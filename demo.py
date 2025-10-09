str1="malayalam"

str1=str1.split()

str1.reverse()

str1="".join(str1)

print(str1)

#method 2

if str1==str1[::-1]:

    print("palindrome")