# Find the nth Fibonacci number
def fibonacci(n):

    if n<=0:

        return "Invalid input"
    
    elif n==1:

        return 0
    
    elif n==2:

        return 1
    
    a,b=0,1

    for i in range(2,n):

        a,b=b,a+b

    return b
    
print(fibonacci(5))
#or

def fibonacci(n):

    if n<=0:

        return "Invalid input"
    
    elif n==1:

        return 0

    elif n==2:

        return 1

    else:

        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(5)) 
# Check if a number is an Armstrong number

# def is_armstrong(n):

#     original_num=n

#     digit_count=len(str(n))

#     total=0

#     while n!=0:

#         digit=n%10

#         exponent=digit**digit_count

#         total+=exponent

#         n=n//10

#     return original_num==n

# print(is_armstrong(153))

def is_armstrong(n):

    num_str=str(n)

    digit_count=len(str(n))

    total=sum(int(digit)**digit_count for digit in num_str)

    return total==n

print(is_armstrong(153))


# Sum of digits of a number

def sum_of_numbers(n):

    result=0

    while n!=0:

        digit=n%10
        result+=digit
        n=n//10

    print(result)

sum_of_numbers(190)

# Reverse a string without using slicing

def reverse_a_string(s):

    return "".join(reversed(s))

print(reverse_a_string("domino"))
    

# Check if two strings are anagrams

def are_anagrams(a,b):

    a=a.replace(" ","").lower()
    b=b.replace(" ","").lower()

    return sorted(a) == sorted(b)

print(are_anagrams("listen", "silent"))   
print(are_anagrams("hello", "world"))  

# Find the largest element in a list

def largest_in_lst(a):

    maxi=max(a)

    return maxi

print(largest_in_lst([3,1,5,7,4]))

# Create a function that accepts variable number of arguments using *args

# Create a function that accepts keyword arguments using **kwargs

# Return unique elements from a list

# Use recursion to calculate factorial or Fibonacci