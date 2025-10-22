

#types of error

#NameError

try:

    print(x)

except NameError as e:

    print("Error:",e)

#TypeError

try:

    print("5"+3)

except TypeError as e:

    print("Error:",e)

#ValueError

try:

    num=int("abx")

except ValueError as e:

    print("Error:",e)

#IndexError

try:

    lst=[1,2,3]
    print(lst[5])

except IndexError as e:

    print("Error:",e)

#KeyError

try:

    d1={'a':1}

    print(d1["b"])

except KeyError as e:

    print("Error:",e)

#AttributeError

try:

    x=10

    print(x.append(10))

except AttributeError as e:

    print("Error:",e)

#Zero Division Error

try :

    n=10/0
    

except ZeroDivisionError as e:

    print("Error:",e)

#ImportError or ModuleNotFoundError

try:

    import nonmodule

except ImportError as e:

    print("Error:",e)

#IndentationError

# try:

#     def hello()
        
# except IndentationError as e:

#     print("Error:",e)


#OverflowError

import math

try:
    x=math.exp(1000)

except OverflowError as e:

    print("Error:",e)

#MemoryError
try:
    x=1000*1000

except MemoryError as e:

    print("Error:",e)


#_________________________________________

class Above_age(Exception):

    pass
    
y=26

try:
    if y>18:
        raise Above_age("Above 18years old")

except Above_age as e:

    print("find exception",e)

#___________________________________________

class ShortPasswordError(Exception):
    pass

password = "sdwd"

try:
    if len(password) < 6:
        raise ShortPasswordError("password must be at least 6 characters long")
    else:
        print("password accepted")
except ShortPasswordError as e:
    print("Error:", e)

#__________________________________________
