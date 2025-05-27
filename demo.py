import copy

original=[[1,2],[3,4]]

shallow=copy.copy(original)

shallow[0][0]=99

print(original)

#or

lst1=[[1,2],[3,4]]

lst2=lst1.copy()

lst2[0][0]=99

print(lst1)


#_______________________________________


original=[[1,2],[3,4]]

deep=copy.deepcopy(original)

deep[0][0]=99

print(original)


#________________________________________

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = []

for x in fruits:

    if "a" in x:

        newlist.append(x)

print(newlist)

newlist=[x for x in fruits if "a" in x]

print(newlist)

#______________________________




lst=[1,1]

n=8

while len(lst)<n:

    c=lst[-1]+lst[-2]

    lst.append(c)

    

print(lst)
#_________________________________

def myFun(a,b,operator):

    if operator=='+':

        return a+b
    
    elif operator=='-':

        return a-b
    
    elif operator=='*':

        return a*b  
    
    elif operator=='/':

        return a/b
    
    
print(myFun(2,4,'+'))


#_________________________________

n = lambda x:"Divisible by 3" if x%3==0 else "Divisible by 5" if x%5==0 else "Not divisible by 3 or 5"

print(n(5))

#________________________________

# x=-1


# if type(x) is int:

#     raise TypeError("string is only allowed")

#________________________________________

class Above_age(Exception):

    pass
    
y=26

try:
    if y>18:
        raise Above_age("Above 18years old")

except Above_age as e:

    print("find exception",e)

#___________________________________________

class ShortPasswordError(Exception):
    pass

password = "sdwd"

try:
    if len(password) < 6:
        raise ShortPasswordError("password must be at least 6 characters long")
    else:
        print("password accepted")
except ShortPasswordError as e:
    print("Error:", e)

#__________________________________________