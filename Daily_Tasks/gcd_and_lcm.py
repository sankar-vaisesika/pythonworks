#gcd of 2 numbers:
#method 1
def find_gcd(a,b):
    gcd=1
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    return f"gcd of numbers {a} and {b} is :{gcd}"

print(find_gcd(12,36))

#method 2
import math
a=12
b=36
gcd=math.gcd(a,b)

print(gcd)

#method 3

def recursive_gcd(a,b):
    if b==0:
        return a
    return recursive_gcd(b,a%b) #(36,12),(12,0) 
print(recursive_gcd(12,36))
    
#method 4

def gcd(a,b):
    while b:
        a,b=b,a%b

    return a
print(gcd(12,36))

#lcm of 2 numbers

#method 1

def lcm(a,b):
    greater=max(a,b)
    while True:
        if greater%a==0 and greater%b==0:
            lcm=greater
            break
        greater+=1
    return f"LCM of 2 numbers {a} and {b} is:{lcm}"
print(lcm(12,15))

#method 2

num1=12
num2=15

result=math.lcm(num1,num2)
print(result)