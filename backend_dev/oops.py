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
#         super().printname()
#         return f"{self.name}"
# s_intance=Student("Mani",24,"A")
# # print(Student.__mro__)
# print(s_intance.printname())


#multiple inheritance

# class Flyer:
#     def fly(self):
#         return "i can fly"

# class Swimmer:
#     def swim(self):
#         return "i can swim"
    
# class Duck(Swimmer,Flyer):
#     def duck(self):
#         return "quak"
    
# d=Duck()
# print(d.fly())

#diamond problem

# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         print("B")
#         super().show()

# class C(A):
#     def show(self):
#         print("C")
#         super().show()
        
# class D(B,C):
#     def show(self):
#         print("D")
#         super().show()
# obj=D()
# obj.show()

#multilevel inheritance

# class A():
#     def __init__(self):
#         super().__init__()
#         print("hai")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("hello")
    
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("Bye")
    
# p1=C()

#method overloading

# class Operations:
#     def add(self,num1,num2):
#         print(num1+num2)

#     def add(self,num1,num2,num3):
#         print(num1+num2+num3)

# obj_instance=Operations()
# obj_instance.add(1,2,3)

#using default parameter

# class Operations:
#     def add(self,num1,num2,num3=None):
#         if num3 is None:
#             print(num1+num2)
#         else:
#             print(num1+num2+num3)

# obj_instance=Operations()
# obj_instance.add(1,2,3)     #6
# obj_instance.add(1,2)       #3

#using *args

class Operations:
    def add(self,*args):
        total=0
        for num in args:
            total+=num
        print(total)
obj=Operations()

obj.add(1,2,3)  #6
obj.add(1,2)    #3
obj.add(1,2,3,4,5)#15


