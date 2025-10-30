
source_file=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\word_count.txt","r")

destination_file=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\destination.file.txt","w")

content=source_file.read()

destination_file.write(content)

source_file.close()

destination_file.close()