def digitalRoot(n):

    while n>=10:

        result=0

        while n>0:

            result+=n%10

            n=n//10

        n=result

    return n


print(digitalRoot(17))
print(digitalRoot(942))


