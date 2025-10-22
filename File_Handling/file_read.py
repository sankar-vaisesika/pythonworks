# file_path = r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\students.txt.txt"

 

# import os
 
# if os.path.exists(file_path):
#     print("File exists!")
# else:
#     print("File NOT found at:", file_path)


with open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\students.txt.txt","a") as f:

   f.write("python java")

with open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\students.txt.txt","r") as f:
    content=f.read()
    print(content)
# f=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\students.txt.txt","r")

# for line in f:

#     print(line)

# f=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\students.txt.txt","r")

# for line in f:

#     print(line)