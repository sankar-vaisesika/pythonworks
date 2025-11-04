import re

def check_password(pwd):
    checks={
        "length":len(pwd)>=8,
        "lower":bool(re.search(r"[a-z]",pwd)),
        "upper":bool(re.search(r"[A-Z]",pwd)),
        "digit":bool(re.search(r"[0-9]",pwd)),
        "special":bool(re.search(r"^[/w/s/d]",pwd)),
    }

    score=sum(checks.values())

    if score==5:
        strength="very strong"
    elif score==4:
        strength="Strong"
    elif score==3:
        strength="Medium"
    else:
        strength="Weak"

    return strength,checks

pwd = input("Enter password to check: ")
strength, details = check_password(pwd)
print("Strength:", strength)
print("Details:", details)
