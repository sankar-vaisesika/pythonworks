# def reverse(x):

#     int_min=-2**31-1  #2147483647

#     int_max=2**31   #-2147483648

#     sign=-1 if x<0 else 1

#     x=abs(x)

#     rev=0

#     while x!=0:

#         digit=x%10


#         x=x//10

#         if rev > (int_max - digit) // 10:
#             return 0
        
#         rev=rev*10+digit

#     return sign*rev

# print(reverse(-123))


#another method
def reverse(x):

    t=str(x)

    if x<0:

        s=int(t[:0:-1])

        s=s*-1

    else:

        s=int(t[::-1])

    return s

print(reverse(-123))