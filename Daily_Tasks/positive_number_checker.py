def positive_only(func):

    def wrapper(*args):

        if any(a<=0 for a in args):

            return "All numbers must be positive"
        
        return func(*args)
    
    return wrapper


@positive_only
def multiply(a,b):

    return a*b

print(multiply(3,5))
print(multiply(-3,5))
