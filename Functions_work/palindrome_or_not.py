def is_palindrome(s):
    s=s.lower()
    if s==s[::-1]:
        print("Is palindrome")
    else:
        print("Not a palindrome")
is_palindrome("Madam")

#method 2

str1="Mom".lower()
if list(str1)==list(reversed(str1)):
    print("Is palindrome")
else:
    print("not a palindrome")

#method 3

s="madam"
s=s.split()
s.reverse()
s="".join(s)
print(s)

#palindrome number

def palindrome(n):
    org_num=n
    rev=0
    while n!=0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return rev==org_num

print(palindrome(121))

