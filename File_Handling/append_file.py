f=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\frame_works.txt","a")

frame_works=["wordpress","springboot","oodo","fastapi"]

for fw in frame_works:

    f.write(fw+"\n")

f.close()