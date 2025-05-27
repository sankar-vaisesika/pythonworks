def palindrome(x):

    # x=str(x)
    # return x[::]==x[::-1]

    return  str(x)=="".join(reversed(str(x))) 

print(palindrome(121))