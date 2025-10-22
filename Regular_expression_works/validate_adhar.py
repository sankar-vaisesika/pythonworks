import re

user_input=input("Enter number:")

x=re.fullmatch(r"[0-9]{4}\s[0-9]{4}\s[0-9]{4}",user_input)

if x==None:

    print("Invalid")

else:

    print("Valid")