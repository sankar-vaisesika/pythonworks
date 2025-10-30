# method-1

num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))
operator=input("Enter operator (+,-,/,*):")

if operator == "+":

    print("Result :",num1 + num2)

elif operator == "-":

    print("Result :",num1 - num2)

elif operator == "*":

    print("Result :",num1 * num2)

elif operator == "/":
    if num2!=0:
        print("Result :",num1 / num2)
    else:
        print("Division by zero not possible")

else:

    print("Invalid operator")

#method -2

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b!=0:
        return a/b

    else:
        return "Division by zero is not possible"
    
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

op=input("Enter operator (+,-,*,/) :")


if op =="+":
    print("Result:",add(a,b))

elif op =="-":
    print("Result:",sub(a,b))

elif op =="*":
    print("Result:",multiply(a,b)) 

elif op =="/":
    print("Result:",divide(a,b))   

else:
    print("Invalid operator")