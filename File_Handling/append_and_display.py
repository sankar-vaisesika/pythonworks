# Create a program that appends user input to an existing file
#  and then displays the entire content of the file.


user_input=input("Enter text: ")

f1=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\input_from_user.txt","a")

f1.write( user_input+"\n")

f1.close()

f2=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\input_from_user.txt","r")

content=f2.read()

print(content)

f2.close()