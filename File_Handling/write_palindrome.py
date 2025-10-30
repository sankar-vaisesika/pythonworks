read_path=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\words.txt","r")

write_path=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\palinrome.txt","w")

for line in read_path:
    word=line.rstrip("\n")
    reversed_word=word[::-1]
    if reversed_word==word:
        write_path.write(word+"\n")

write_path.close()
read_path.close()
