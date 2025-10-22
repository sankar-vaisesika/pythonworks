f=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\students.txt","r")

print(f.read())

f=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\File_Handling\demo.txt")

print(f.readline())
f.close()

#or

with open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\File_Handling\demo.txt") as f:
    print(f.read())