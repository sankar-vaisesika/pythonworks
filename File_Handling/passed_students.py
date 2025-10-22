f1=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\all_students.txt")

f2=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\failed_students.txt")


all_students=[]

for s in f1:

    s=s.rstrip("\n")

    all_students.append(s)

print(all_students)

failed_students=[]

for s in f2:

    s=s.strip("\n")

    failed_students.append(s)

print(failed_students)

# passed_students=set(all_students)-set(failed_students)

passed_students=[student for student in all_students if student not in failed_students]
print(passed_students)