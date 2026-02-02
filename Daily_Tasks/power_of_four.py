# Determine if a number is a power of four.
 
def is_power_of_four(n):
    if n<=0:
        return False
    while n%4==0:
        n=n//4
    return n==1

print(is_power_of_four(16))
print(is_power_of_four(12))
print(is_power_of_four(1))