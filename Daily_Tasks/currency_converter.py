# Currency Converter
# Description: Convert amounts between different currencies (e.g., USD ↔ EUR ↔ INR) using fixed or real-time exchange rates.

def usd_to_eur(usd):
    return usd/0.92
def eur_to_usd(eur):
    return eur*0.92
def usd_to_ind(usd):
    return usd*83
def ind_to_usd(ind):
    return ind/83
def eur_to_ind(eur):
    return eur*101.95
def ind_to_eur(ind):
    return ind/0.0098

print("1) USD -> EURO\n2) EURO -> USD\n3) USD -> IND\n4) IND -> USD\n5) EURO -> IND\n6) IND -> EURO")
choice=input("Choose 1-6:")
val=int(input("Enter the value :"))
conversions={
    "1":usd_to_eur,
    "2":eur_to_usd,
    "3":usd_to_ind,
    "4":ind_to_usd,
    "5":eur_to_ind,
    "6":ind_to_eur
}

if choice in conversions:
    print("Result:",conversions[choice](val))
else:
    print("Invalid choice")