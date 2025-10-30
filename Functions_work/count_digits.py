
#count digits

def count_digits(n):

    c=0

    # for i in str(n):

    #     c+=1


    #another method
    while n!=0:
        c+=1
        n=n//10

    return c

print(count_digits(1234))
