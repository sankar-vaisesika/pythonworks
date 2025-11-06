# #Temperature Unit Converter (Celsius ↔ Fahrenheit ↔ Kelvin)

# print("1:C -> F, 2:F -> C,3:C -> K,4:K -> C,5:F -> K,6:K -> F")

# choice=input("Choose the conversion(1-6):")

# temp=float(input("Enter temperature:"))

# if choice=="1":
    
#     result=(temp*9/5)+32
    
#     print("Fahrenheit=",result)

# elif choice=="2":

#     result=(temp-32)*5/9

#     print("Celsius=",result)

# elif choice=="3":

#     result=temp+273.15

#     print("Kelvin=",result)

# elif choice=="4":
#     result=temp-273.15
#     print("Celsius=",result)

# elif choice=="5":
#     result=(temp-32)*5/9+273.15
#     print("Kelvin=",result)
# elif choice=="6":
#     result=(temp-273.15)*9/5+32
#     print("Fahrenheit=",result)

# else:

#     print("Invalid choice")

#another method

def celsius_to_fahrenheit(c):

    return (c*9/5)+32

def fahrenheit_to_celsius(f):

    return (f-32)*5/9

def celsius_to_kelvin(c):
    return c+273.15

def kelvin_to_celsius(k):
    return k-273.15

def fahrenheit_to_kelvin(f):
    return (f-32)*5/9+273.15

def kelvin_to_fahrenheit(k):
    return (k-273.15)*9/5+32

c=25
f=77
k=298.15

print("Celsius to Fahrenheit:", celsius_to_fahrenheit(c))    
print("Fahrenheit to Celsius:", fahrenheit_to_celsius(f))   
print("Celsius to Kelvin:", celsius_to_kelvin(c))           
print("Kelvin to Celsius:", kelvin_to_celsius(k))           
print("Fahrenheit to Kelvin:", fahrenheit_to_kelvin(f))     
print("Kelvin to Fahrenheit:", kelvin_to_fahrenheit(k))

