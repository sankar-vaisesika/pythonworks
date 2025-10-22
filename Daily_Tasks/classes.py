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



class Employee:
    def __init__(self, role):
        self.role = role

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person, Employee):
    def __init__(self, name, age, role, id):
        Person.__init__(self, name, age)     
        Employee.__init__(self, role)        
        self.id = id

s = Student("mani", 21, "hr", 112)

print(s.name)   
print(s.age)    
print(s.role)   
print(s.id)     
