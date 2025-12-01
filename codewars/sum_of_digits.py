def sum_digits(number):
    sum=0
    # while number!=0:
    #     num=number%10
    #     sum+=num
    #     number=number//10

    s_number=str(abs(number))
    for digit in s_number:
        sum+=int(digit) 
    return sum

print(sum_digits(18))
print(sum_digits(99))
print(sum_digits(10))
print(sum_digits(-32))

