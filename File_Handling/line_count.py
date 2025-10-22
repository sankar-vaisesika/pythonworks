f=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\word_count.txt")

line_count=0
word_count=0

for line in f:
    words=line.split(" ")
    word_count+=len(words)
    line_count+=1

print("Line count is:",line_count,"Word_count is:",word_count)