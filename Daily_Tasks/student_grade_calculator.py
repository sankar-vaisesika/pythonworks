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