years_path=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\years.txt","r")

centuary_path=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\centuary_years.txt","w")

leap_year_path=open(r"C:\Users\jayasankar.km\Desktop\Vaisesika Internship\Python @ vaisesika\Datasets\leap_years.txt","w")

# for year in years_path:

#     if int(year)%100==0:

#         centuary_path.write(str(year))
    
#     elif int(year)%100==0 and int(year)%400==0 or int(year)%4==0 and int(year)%100!=0:
#         leap_year_path.write(str(year))

# or

def is_centuary_year(year):

    return True if year%100==0 else False

def is_leap_year(year):

    return True if year%100==0 and year%400==0 or year%4==0 and year%100!=0 else False

for year in years_path:

    year=int(year)

    if is_centuary_year(year):

        centuary_path.write(str(year)+"\n")

    elif is_leap_year(year):

        leap_year_path.write(str(year)+"\n")

centuary_path.close()

leap_year_path.close()

years_path.close()