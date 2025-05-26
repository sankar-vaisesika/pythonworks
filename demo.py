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

class Person:

    def __init__(self,name,age):
        
        self.name=name
        self.age=age

    def greet(self):

        return "hai"

class Employee(Person):

    def __init__(self, role, salary):

        self.role=role

        self.salary=salary

    

    def greet(self):

        return "hello"

employee_instance=Employee('hr',21000)     

print(employee_instance.greet())



# person_instance=Person("ajay",21)

# person_2=Person("Mani",23)
# print(person_2.age)
# print(person_instance.name)

#Class is able to store memory whereas function can't
class Employee:
    def __init__(self,role):

        self.role=role
        
class Person:

    def __init__(self,name,age):

        self.name=name

        self.age=age

class Student(Person,Employee):

    def __init__(self, name, age,role,id):
        super().__init__(name, age,role)
        
        self.id=id

s=Student("mani",21,112,"hr")

print(s.role)
