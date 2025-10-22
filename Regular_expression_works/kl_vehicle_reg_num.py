from re import fullmatch,IGNORECASE

user_input=input("Enter reg number:")

matcher=fullmatch(r"(KL)[0-9]{2}[A-Z]{0,2}[0-9]{4}",user_input,IGNORECASE)

if matcher==None:

    print("invalid")

else:

    print("Valid")