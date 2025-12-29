#using decorator to print something when a number gets divided by zero


def divisibility_checker(func):

    def wrapper(a,b):
        if b==0:
            return "Division by zero is not allowd"    
        return func(a,b)
    return wrapper

@divisibility_checker
def divide(a,b):
    return a/b

print(divide(9,0))
print(divide(9,3))
 
