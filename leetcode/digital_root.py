# The digital root of a non-negative integer is the single-digit 
# value obtained by an iterative process of summing digits. 
# This process continues until a single-digit number is reached. 


def digitalRoot(n):

    while n>=10:

        result=0

        while n>0:

            result+=n%10

            n=n//10

        n=result

    return n


print(digitalRoot(333))