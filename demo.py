
# Regular expression - re module
# opening and writing reading a file - contence manager like file operations
# django project 
# ai-paper
# ml-books

#string operation and string methods
# is and ==
#looping 
#list
#django project
#Input marks for different subjects and calculate the total, average, and grade (A/B/C/D/F).

# maths=int(input("Enter marks for maths:"))
# english=int(input("Enter marks for english:"))
# science=int(input("Enter marks for science:"))
# social_science=int(input("Enter marks for social_science:"))
# hindi=int(input("Enter marks for hindi:"))




# total=maths+english+science+social_science+hindi
# n=5
# average=total/n

# if average>=90:
#     grade="A"
# elif average>=75:
#     grade="B"
# elif average>=65:
#     grade="C"
# elif average>=55:
#     grade="D"
# elif average>=40:
#     grade="E"
# else:
#     grade="F"

# print("Grade:",grade ,"\nAverage:",average,"\nTotal:",total)



def caluculate_grade(marks):
    total=sum(marks.values())
    n=len(marks)
    avg=total/n 

    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"

    return total, avg, grade

subjects=["Maths","Physics","Chemistry","Biology","English"]
marks={}
for s in subjects:
    marks[s]=int(input(f"Enter marks for {s}:"))

total,avg,grade=caluculate_grade(marks)
print(f"Total:{total}\nAverage:{avg}\nGrade:{grade}")


# Unit converter

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
val=float(input("Enter value:"))
conversions = {
    "1": metre_to_feet,
    "2": feet_to_metre,
    "3": kg_to_pounds,
    "4": pounds_to_kg,
    "5": hours_to_minutes,
    "6": minutes_to_hours,
}

if choice in conversions:
    print("Result:",conversions[choice])
else:
    print("Invalid choice")

#currency converter

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

#Word Counter

