# #OOPs
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         return f"Hai, My name is {self.name} and i'am {self.age} years old"
    
# p1=Person("Mani",23)
# print(p1.greet())
# #abstraction
# #polimorphism
# #encapsulation
# class BankAccount:
#     def __init__(self,balance):
#         self.__balance=balance

#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#     def get_balance(self):
#         return self.__balance
# b=BankAccount(1000)
# b.deposit(50)
# print(b.get_balance())
# #inheritance
# class Person:

#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname

#     def printname(self):
#         print(self.fname,self.lname)

# class Student(Person):
#     pass

# student_instance=Student("Karn","SHarma")
# student_instance.printname()

# #Method overriding
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def printname(self):
#         return f"{self.name} - {self.age}"
# class Student(Person):
#     def __init__(self, name, age,grade):
#         super().__init__(name, age)     #super() connects child to parent constructor.
#         self.grade=grade
#     def printname(self):
#         return f"{self.name}"
# s_intance=Student("Mani",24,"A")
# print(Student.__mro__)
# print(s_intance.printname())

#Calling parent method after overriding
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
        return f"{self.name} - {self.age}"
class Student(Person):
    def __init__(self, name, age,grade):
        super().__init__(name, age)     #super() connects child to parent constructor.
        self.grade=grade
    def printname(self):
        super().printname()
        return f"{self.name}"
s_intance=Student("Mani",24,"A")
# print(Student.__mro__)
print(s_intance.printname())