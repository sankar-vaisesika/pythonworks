# Function with default arguments and keyword arguments
def configure_systems(username,status="active",timezone="UTC",**user_data):
    print(f"\n---User Profile:{username}---")
    print(f"Status:{status}")
    print(f"Timezone:{timezone}")

    if not user_data:
        print("Not data")

    if user_data:
        print("\nAdditional Datails:")
        for k,v in user_data.items():
            print(f"{k.capitalize()}:{v}")

configure_systems("John",role="Admin")

# Nested functions (function inside another function)

def outer_function(text):

    greeting="Hello"

    def inner_function():

        full_message=f"{greeting},{text}!"

        print(full_message)
    
    inner_function()

outer_function("World")
outer_function("Python user")



# Function to flatten a nested list

def flatten(nested_list):
    return [item for sublist in nested_list for item in sublist]
print(flatten([[1,2,3],[3,4,5]]))


# Lambda with map(), filter(), and reduce() 
#map()-The map() function applies a given function to every item in an iterable (like a list) and returns an iterator of the results.
numbers=1,2,3
squared_numbers=list(map(lambda x:x**2,numbers))
print(squared_numbers)

#filter()-The filter() function tests each item in an iterable against a function that returns either True or False, and returns an iterator of only the items for which the function returned True.
number=[1,2,3,4,5,6,7,8,9,10]

even_numbers=list(filter(lambda x:x%2==0,number))

print(even_numbers)

#reduce()-The reduce() function applies a rolling computation to sequential pairs of values in a list. It is part of the functools module and must be imported. It is commonly used to accumulate a single result from a list of values.
from functools import reduce
nums=[1,2,3,4,5]

sum_of_nums=reduce(lambda x,y:x+y,numbers)
print(sum_of_nums)
# Create a decorator that logs function execution

# Memoization using functions (e.g., for Fibonacci)

# Function to group items by category using dictionary

# Function to parse and clean text data

# Use function as a callback or pass it as an argument

# Closures and scope demonstration with nested functions

