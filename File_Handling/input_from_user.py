# Write a program to take input from the user and write it to a file. 
# Then, read the content from the file and display it.

data_from_user=input("Enter the text:")

f_write=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\input_from_user.txt","w")

for text in data_from_user:

    f_write.write(text)

f_write.close()

f_read=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\input_from_user.txt","r")

for line in f_read:

    print(line.rstrip("\n"))