# Find All Prime Numbers in a Range

def is_prime(n):
    if n<=1:
        return False
    
    else:

        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
                break
        return True

start,end=2,20    
primes=[n for n in range(start,end+1) if is_prime(n)]

print("prime numbers between",start,"to",end,"are :",*primes)