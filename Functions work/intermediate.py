# Find the nth Fibonacci number

# Check if a number is an Armstrong number

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