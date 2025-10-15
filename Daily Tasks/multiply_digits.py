#multiply digits

def multiply_digits(n):

    product=1

    while n!=0:

        digit=n%10

        product*=digit

        n=n//10

    return product

print(multiply_digits(1234))