password=input("Enter password:")
hasUpper=False
hasDigit=False
hasLower=False
hasSpecial=False

if len(password)<8:
    print("Password must be atleast 8 characters") 
else:
    for ch in password:
        if ch.isupper():
            hasUpper=True
        if ch.isdigit():
            hasDigit=True
        if ch.islower():
            hasLower=True
        else:
            hasSpecial=True

if hasUpper and hasLower and hasDigit and hasSpecial:
    print("Valid password")
else:
    print("Invalid password")