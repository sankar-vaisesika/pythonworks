def to_uppercase(func):

    def wrapper(res):
        result=func(res)
        return result.upper()
    
    return wrapper


@to_uppercase
def greet(res):

    return res

print(greet("hello world"))