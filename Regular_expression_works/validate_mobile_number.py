from re import fullmatch

input_number=input("Enter number:")

pattern="(91)?[0-9]{10}" 

matcher=fullmatch(pattern,input_number)

if matcher==None:

    print("invalid number")

else:

    print("Valid number")