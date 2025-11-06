# Unit Converter
# Description: Convert between different units — e.g., length (meters ↔ feet), weight (kg ↔ pounds), or time (hours ↔ minutes).
def metre_to_feet(m):

    return m*3.28084

def feet_to_metre(f):

    return f/3.28084

def kg_to_pounds(kg):
    return kg*2.20462

def pounds_to_kg(p):
    return p/2.20462

def hours_to_minutes(h):
    return h*60

def minutes_to_hours(m):
    return m/60

print("1) meters -> feet\n2) feet -> meters\n3) kg -> pounds\n4) pounds -> kg\n5) hours -> minutes\n6) minutes -> hours")
choice=input("Choose 1-6:")
val=float(input("Enter value to convert:"))
conversions = {
    "1": metre_to_feet,
    "2": feet_to_metre,
    "3": kg_to_pounds,
    "4": pounds_to_kg,
    "5": hours_to_minutes,
    "6": minutes_to_hours,
}

if choice in conversions:
    print("Result:",conversions[choice](val))
else:
    print("Invalid choice")