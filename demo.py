

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

def outer_function():

    message="hei"

    class LocalClass:

        def show(self):

            print(message)

    obj=LocalClass()

    obj.show()

outer_function()

