# def palindrome(x):

#     # x=str(x)
#     # return x[::]==x[::-1]


# print(palindrome(121))



# def palindrome(x):

#     return str(x)=="".join(reversed(x))

def palindrome(x):

    x=str(x)

    return x==x[::-1]

print(palindrome("1211"))


