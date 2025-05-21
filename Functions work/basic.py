
# Function to add two numbers
def add(n1,n2):

    return n1+n2

print(add(100,200))
# Check if a number is even or odd
def even_or_odd(n):

    if n%2==0:
        return "Even"
    
    else:

        return "Odd"
    
print(even_or_odd(192))

# Find the maximum of three numbers

def maxi(n1,n2,n3):

    return max(n1,n2,n3)

print(maxi(2,1,4))

# Calculate the factorial of a number

def fact(num):
    result=1
    while num!=0:

        result=result*num
        num-=1

    return result

print(fact(5))

# Check if a number is prime

def is_prime(num):

    if num<2:

        return False

    for i in range(2,num):

        if num%i==0:

            return False

    return True

print(is_prime(12))

# Return the square of a number

def square(num):

    return num**2

print(square(9))

# Return the length of a string

def length(str):

    return len(str)

print(length("Hello"))

# Check if a string is a palindrome

def is_palindrome(str):

    if str==str[::-1]:
        return "Palindrome"
    
    else:
        return "Not Palindrome"
    
print(is_palindrome("monom"))

# Count vowels in a string

def vowels(string):

    vowels="aeiouAEIOU"
    count=0
    for i in string:

        if i in vowels:

            count+=1

    return count

print(vowels("malayalam"))

