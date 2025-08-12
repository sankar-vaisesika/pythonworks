
# Longest Palindromic Substring

def is_valid_palindrome(s):

    lst=[]

    for i in s:

        if i.isalnum():

            lst.append(i.lower())

    a="".join(lst)

    return a==a[::-1]


print(is_valid_palindrome("A man, a plan, a canal: Panama"))

