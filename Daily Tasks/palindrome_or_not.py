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