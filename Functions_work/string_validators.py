#return true if the validation is correct

def string_validators(s:str):

    print(f"{s.isalpha()}")
    print(f"{s.isalnum()}")
    print(f"{s.isdigit()}")
    print(f"{s.islower()}")
    print(f"{s.isupper()}")
string_validators("QA2")

#return true if the string has the given 

def string_validators_any(s:str):
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))

string_validators_any("qA2")