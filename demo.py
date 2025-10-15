

#sum of digits

def sum_of_digits(n):

    total=0

    while n!=0:

        digit=n%10

        total+=digit

        n=n//10

    return total

print(sum_of_digits(123))

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

